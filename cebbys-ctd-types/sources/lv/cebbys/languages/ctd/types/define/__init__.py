"""Define Package

This package contains definition types for resolved CTD definitions.
"""
from lv.cebbys.languages.ctd.types.define.__api__ import *
from lv.cebbys.languages.ctd.types.define.decorator import *
from lv.cebbys.languages.ctd.types.define.typedef import *
from lv.cebbys.languages.ctd.types.define.enum import *
from lv.cebbys.languages.ctd.types.define.flag import *
from lv.cebbys.languages.ctd.types.define.structure import *
from lv.cebbys.languages.ctd.types.define.function import *
from lv.cebbys.languages.ctd.types.define.interface import *
from lv.cebbys.languages.ctd.types.define.collection import *

__all__ = [
    # API
    'BaseDefinition',
    'BaseType',
    'PrimitiveType',
    'TypeReference',
    'TypeSpec',
    # Decorator
    'DecoratorDefinition',
    # Typedef
    'TypedefDefinition',
    # Enum
    'EnumMemberDefinition',
    'EnumDefinition',
    # Flag
    'FlagMemberDefinition',
    'FlagDefinition',
    # Structure
    'StructureMemberDefinition',
    'StructureDefinition',
    # Interface,
    'InterfaceDefinition',
    # Function
    'ParameterDefinition',
    'FunctionDefinition',
    # Collection
    'DefinitionCollection',
]
