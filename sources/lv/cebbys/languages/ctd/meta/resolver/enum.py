"""Enum Resolver

This module handles resolution of enum definitions.
"""
import lv.cebbys.languages.ctd.meta.loader as Types
import lv.cebbys.languages.ctd.define as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api

__all__ = ['EnumResolver']


class EnumResolver(Api.BaseResolver):
    """Resolver for enum definitions."""
    
    def create_instances(self) -> None:
        """Create enum instances and add them to the type cache."""
        enum_meta: Types.EnumMeta
        qualified_name: str
        
        for enum_meta in self._context.meta_collection.enums:
            qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
            enum_instance = Define.EnumDefinition(
                enum_meta.name,
                enum_meta.namespace
                # base_type and members will be set in resolve phase
            )
            self._context.type_cache[qualified_name] = enum_instance
    
    def resolve_instances(self) -> None:
        """Resolve enum base types and members."""
        enum_meta: Types.EnumMeta
        qualified_name: str
        enum_instance: Define.BaseDefinition
        base_type: Define.TypeSpec | None
        members: list[Define.EnumMemberDefinition]
        
        for enum_meta in self._context.meta_collection.enums:
            qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
            enum_instance = self._context.type_cache[qualified_name]
            if isinstance(enum_instance, Define.EnumDefinition):
                # Resolve base type if specified
                base_type = None
                if enum_meta.base_type:
                    base_type = self.parse_type_spec(
                        enum_meta.base_type, enum_meta.namespace)
                enum_instance.set_base_type(base_type)
                
                # Resolve members
                members = self._resolve_enum_members(enum_meta.members)
                enum_instance.set_members(members)
    
    def _resolve_enum_members(
        self,
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
