"""Meta Loader Package

This package contains metadata types and the loader for CTD files.
"""
from lv.cebbys.languages.ctd.meta.loader.__api__ import *
from lv.cebbys.languages.ctd.meta.loader.decorator import *
from lv.cebbys.languages.ctd.meta.loader.typedef import *
from lv.cebbys.languages.ctd.meta.loader.alias import *
from lv.cebbys.languages.ctd.meta.loader.enum import *
from lv.cebbys.languages.ctd.meta.loader.flag import *
from lv.cebbys.languages.ctd.meta.loader.structure import *
from lv.cebbys.languages.ctd.meta.loader.interface import *
from lv.cebbys.languages.ctd.meta.loader.function import *
from lv.cebbys.languages.ctd.meta.loader.collection import *
from lv.cebbys.languages.ctd.meta.loader.loader import MetaLoader

__all__ = [
    # API
    'ModulePath',
    # Decorator
    'DecoratorMeta',
    # Typedef
    'TypedefMeta',
    # Alias
    'AliasMeta',
    # Enum
    'EnumMemberMeta',
    'EnumMeta',
    # Flag
    'FlagMemberMeta',
    'FlagMeta',
    # Structure
    'StructureMemberMeta',
    'StructureMeta',
    # Interface
    'InterfaceMeta',
    # Function
    'ParameterMeta',
    'FunctionMeta',
    # Collection
    'DefinitionCollectionMeta',
    # Loader
    'MetaLoader',
]
