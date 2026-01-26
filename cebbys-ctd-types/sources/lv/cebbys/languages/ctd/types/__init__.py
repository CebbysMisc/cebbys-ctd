"""CTD Types Package

This package contains type definitions and metadata structures for CTD language.
"""
from lv.cebbys.languages.ctd.types.define import (
    BaseDefinition,
    BaseType,
    PrimitiveType,
    TypeSpec,
    TypeReference,
    TypedefDefinition,
    EnumMemberDefinition,
    EnumDefinition,
    FlagMemberDefinition,
    FlagDefinition,
    StructureMemberDefinition,
    StructureDefinition,
    InterfaceDefinition,
    ParameterDefinition,
    FunctionDefinition,
    DecoratorDefinition,
    DefinitionCollection,
)

__all__ = [
    # define/__api__.py
    'BaseDefinition',
    'BaseType',
    'PrimitiveType',
    'TypeSpec',
    'TypeReference',
    # define
    'TypedefDefinition',
    'EnumMemberDefinition',
    'EnumDefinition',
    'FlagMemberDefinition',
    'FlagDefinition',
    'StructureMemberDefinition',
    'StructureDefinition',
    'InterfaceDefinition',
    'ParameterDefinition',
    'FunctionDefinition',
    'DecoratorDefinition',
    'DefinitionCollection',
]
