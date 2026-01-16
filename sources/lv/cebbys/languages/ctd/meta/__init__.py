"""Meta Package

This package contains metadata types, loader, and resolver for CTD language.
"""
from lv.cebbys.languages.ctd.meta.types import *
from lv.cebbys.languages.ctd.meta.loader import MetaLoader
from lv.cebbys.languages.ctd.meta.resolver import MetaResolver, ResolutionError

__all__ = [
    # Types from types module
    'TypedefMeta',
    'EnumMemberMeta',
    'EnumMeta',
    'FlagMemberMeta',
    'FlagMeta',
    'FieldMeta',
    'StructureMeta',
    'ParameterMeta',
    'FunctionMeta',
    'DefinitionCollectionMeta',
    # Loader
    'MetaLoader',
    # Resolver
    'MetaResolver',
    'ResolutionError',
]
