"""Typedef Resolver

This module handles resolution of typedef definitions.
"""
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api

__all__ = ['TypedefResolver']


class TypedefResolver(Api.BaseResolver):
    """Resolver for typedef definitions."""
    
    def create_instances(self) -> None:
        """Create typedef instances and add them to the type cache."""
        typedef_meta: Types.TypedefMeta
        qualified_name: str
        
        for typedef_meta in self._context.meta_collection.typedefs:
            qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
            typedef_instance = Define.TypedefDefinition(
                typedef_meta.name,
                typedef_meta.namespace
                # type_spec will be set in resolve phase
            )
            self._context.type_cache[qualified_name] = typedef_instance
    
    def resolve_instances(self) -> None:
        """Resolve typedef type specifications."""
        typedef_meta: Types.TypedefMeta
        qualified_name: str
        typedef_instance: Define.BaseDefinition
        type_spec: Define.TypeSpec
        
        for typedef_meta in self._context.meta_collection.typedefs:
            qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
            typedef_instance = self._context.type_cache[qualified_name]
            if isinstance(typedef_instance, Define.TypedefDefinition):
                type_spec = self.parse_type_spec(
                    typedef_meta.type_spec, typedef_meta.namespace)
                typedef_instance.set_type_spec(type_spec)
