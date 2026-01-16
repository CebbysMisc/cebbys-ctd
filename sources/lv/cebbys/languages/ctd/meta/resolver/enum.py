"""Enum Resolver

This module handles resolution of enum definitions.
"""
import typing as Typing
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api

__all__ = ['create_enum_instances', 'resolve_enums']


def create_enum_instances(context: Api.ResolverContext) -> None:
    """Create enum instances and add them to the type cache.
    
    Args:
        context: Resolver context with type cache and metadata
    """
    enum_meta: Types.EnumMeta
    qualified_name: str
    
    for enum_meta in context.meta_collection.enums:
        qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
        enum_instance = Define.EnumDefinition(
            enum_meta.name,
            enum_meta.namespace
            # base_type and members will be set in resolve phase
        )
        context.type_cache[qualified_name] = enum_instance


def resolve_enums(
    context: Api.ResolverContext,
    parse_type_spec: Typing.Callable[[str, str], Define.TypeSpec]
) -> None:
    """Resolve enum base types and members.
    
    Args:
        context: Resolver context with type cache and metadata
        parse_type_spec: Function to parse type specification strings
    """
    enum_meta: Types.EnumMeta
    qualified_name: str
    enum_instance: Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition
    base_type: Define.TypeSpec | None
    members: list[Define.EnumMemberDefinition]
    
    for enum_meta in context.meta_collection.enums:
        qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
        enum_instance = context.type_cache[qualified_name]
        if isinstance(enum_instance, Define.EnumDefinition):
            # Resolve base type if specified
            base_type = None
            if enum_meta.base_type:
                base_type = parse_type_spec(
                    enum_meta.base_type, enum_meta.namespace)
            enum_instance.set_base_type(base_type)
            
            # Resolve members
            members = _resolve_enum_members(enum_meta.members)
            enum_instance.set_members(members)


def _resolve_enum_members(
    members_meta: list[Types.EnumMemberMeta]
) -> list[Define.EnumMemberDefinition]:
    """Resolve enum members with automatic value assignment.
    
    Args:
        members_meta: List of enum member metadata
        
    Returns:
        List of resolved enum member definitions
    """
    members: list[Define.EnumMemberDefinition]
    current_value: int
    member_meta: Types.EnumMemberMeta
    value: int
    
    members = []
    current_value = 0
    
    for member_meta in members_meta:
        if member_meta.value is not None:
            value = member_meta.value
            current_value = value + 1
        else:
            value = current_value
            current_value += 1
        
        members.append(Define.EnumMemberDefinition(
            member_meta.name, value))
    
    return members
