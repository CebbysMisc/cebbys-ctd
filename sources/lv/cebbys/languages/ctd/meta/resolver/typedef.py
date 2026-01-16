"""Typedef Resolver

This module handles resolution of typedef definitions.
"""
import typing as Typing
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api

__all__ = ['create_typedef_instances', 'resolve_typedefs']


def create_typedef_instances(context: Api.ResolverContext) -> None:
    """Create typedef instances and add them to the type cache.
    
    Args:
        context: Resolver context with type cache and metadata
    """
    typedef_meta: Types.TypedefMeta
    qualified_name: str
    
    for typedef_meta in context.meta_collection.typedefs:
        qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
        typedef_instance = Define.TypedefDefinition(
            typedef_meta.name,
            typedef_meta.namespace
            # type_spec will be set in resolve phase
        )
        context.type_cache[qualified_name] = typedef_instance


def resolve_typedefs(
    context: Api.ResolverContext,
    parse_type_spec: Typing.Callable[[str, str], Define.TypeSpec]
) -> None:
    """Resolve typedef type specifications.
    
    Args:
        context: Resolver context with type cache and metadata
        parse_type_spec: Function to parse type specification strings
    """
    typedef_meta: Types.TypedefMeta
    qualified_name: str
    typedef_instance: Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition
    type_spec: Define.TypeSpec
    
    for typedef_meta in context.meta_collection.typedefs:
        qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
        typedef_instance = context.type_cache[qualified_name]
        if isinstance(typedef_instance, Define.TypedefDefinition):
            type_spec = parse_type_spec(
                typedef_meta.type_spec, typedef_meta.namespace)
            typedef_instance.set_type_spec(type_spec)
