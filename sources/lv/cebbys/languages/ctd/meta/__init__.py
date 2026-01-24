"""Meta Package

This package contains metadata types, loader, and resolver for CTD language.
"""
from lv.cebbys.languages.ctd.meta.loader import *
from lv.cebbys.languages.ctd.meta.resolver import MetaResolver, ResolutionError

__all__ = [
    # API
    'ModulePath',
    # Typedef
    'TypedefMeta',
    # Enum
    'EnumMemberMeta',
    'EnumMeta',
    # Flag
    'FlagMemberMeta',
    'FlagMeta',
    # Structure
    'StructureMemberMeta',
    'StructureMeta',
    # Function
    'ParameterMeta',
    'FunctionMeta',
    # Collection
    'DefinitionCollectionMeta',
    # Loader
    'MetaLoader',
    # Resolver
    'MetaResolver',
    'ResolutionError',
]
