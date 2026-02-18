"""Meta Loader Package

This package contains metadata types and the loader for CTD files.
"""
from lv.cebbys.languages.ctd.types.meta.__api__ import ModulePath
from lv.cebbys.languages.ctd.types.meta.__api__ import DeclarationMeta
from lv.cebbys.languages.ctd.types.meta.collection import DefinitionCollectionMeta
from lv.cebbys.languages.ctd.types.meta.namespace import NamespaceMeta
from lv.cebbys.languages.ctd.types.meta.structure import StructureMemberMeta
from lv.cebbys.languages.ctd.types.meta.structure import StructureMeta
from lv.cebbys.languages.ctd.types.meta.interface import InterfaceMeta
from lv.cebbys.languages.ctd.types.meta.__api__ import DecoratorMeta
from lv.cebbys.languages.ctd.types.meta.function import ParameterMeta
from lv.cebbys.languages.ctd.types.meta.function import FunctionMeta
from lv.cebbys.languages.ctd.types.meta.include import IncludeMeta
from lv.cebbys.languages.ctd.types.meta.typedef import TypedefMeta
from lv.cebbys.languages.ctd.types.meta.module import ModuleMeta
from lv.cebbys.languages.ctd.types.meta.alias import AliasMeta
from lv.cebbys.languages.ctd.types.meta.enum import EnumMemberMeta
from lv.cebbys.languages.ctd.types.meta.enum import EnumMeta
from lv.cebbys.languages.ctd.types.meta.flag import FlagMemberMeta
from lv.cebbys.languages.ctd.types.meta.flag import FlagMeta
from lv.cebbys.languages.ctd.types.meta.typespec import (
    PointerTypespecMeta,
    ArrayTypespecMeta,
    TypedTypespecMeta,
    TypespecMeta
)

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
    'IncludeMeta',
    'NamespaceMeta',
    'ModuleMeta',
    'DeclarationMeta',
    'PointerTypespecMeta',
    'ArrayTypespecMeta',
    'TypedTypespecMeta',
    'TypespecMeta'
]
