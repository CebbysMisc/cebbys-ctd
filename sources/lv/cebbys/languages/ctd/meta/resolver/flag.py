"""Flag Resolver

This module handles resolution of flag definitions.
"""
import typing as Typing
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api

__all__ = ['create_flag_instances', 'resolve_flags']


def create_flag_instances(context: Api.ResolverContext) -> None:
    """Create flag instances and add them to the type cache.
    
    Args:
        context: Resolver context with type cache and metadata
    """
    flag_meta: Types.FlagMeta
    qualified_name: str
    
    for flag_meta in context.meta_collection.flags:
        qualified_name = f"{flag_meta.namespace}::{flag_meta.name}"
        flag_instance = Define.FlagDefinition(
            flag_meta.name,
            flag_meta.namespace
            # base_type and members will be set in resolve phase
        )
        context.type_cache[qualified_name] = flag_instance


def resolve_flags(
    context: Api.ResolverContext,
    parse_type_spec: Typing.Callable[[str, str], Define.TypeSpec]
) -> None:
    """Resolve flag base types and members.
    
    Args:
        context: Resolver context with type cache and metadata
        parse_type_spec: Function to parse type specification strings
    """
    flag_meta: Types.FlagMeta
    qualified_name: str
    flag_instance: Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition
    base_type: Define.TypeSpec | None
    members: list[Define.FlagMemberDefinition]
    
    for flag_meta in context.meta_collection.flags:
        qualified_name = f"{flag_meta.namespace}::{flag_meta.name}"
        flag_instance = context.type_cache[qualified_name]
        if isinstance(flag_instance, Define.FlagDefinition):
            # Resolve base type if specified
            base_type = None
            if flag_meta.base_type:
                base_type = parse_type_spec(
                    flag_meta.base_type, flag_meta.namespace)
            flag_instance.set_base_type(base_type)
            
            # Resolve members with bit-shifting
            members = _resolve_flag_members(flag_meta.members)
            flag_instance.set_members(members)


def _resolve_flag_members(
    members_meta: list[Types.FlagMemberMeta]
) -> list[Define.FlagMemberDefinition]:
    """Resolve flag members with bit-shifting value assignment.
    
    Flags start at 0x1 and each subsequent member is bit-shifted left:
    - First: 0x1 (1)
    - Second: 0x2 (2)
    - Third: 0x4 (4)
    - Fourth: 0x8 (8)
    - etc.
    
    Manual offsets can be specified (e.g., 0x20), and bit-shifting
    continues from that value for subsequent members.
    
    Args:
        members_meta: List of flag member metadata
        
    Returns:
        List of resolved flag member definitions
    """
    members: list[Define.FlagMemberDefinition]
    member_meta: Types.FlagMemberMeta
    current_value: int
    value: int
    
    members = []
    current_value = 0x1  # Start at 0x1 (1)
    
    for member_meta in members_meta:
        if member_meta.value is not None:
            # Explicit value specified
            value = member_meta.value
            current_value = value << 1  # Next value is this value bit-shifted left
        else:
            # Auto-assign bit-shifted value
            value = current_value
            current_value = current_value << 1  # Bit-shift left for next member
        
        members.append(Define.FlagMemberDefinition(
            member_meta.name, value))
    
    return members
