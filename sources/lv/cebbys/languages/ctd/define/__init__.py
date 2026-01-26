"""Define Package

This package contains definition types for resolved CTD definitions.
"""
from lv.cebbys.languages.ctd.define.__api__ import *
from lv.cebbys.languages.ctd.define.decorator import *
from lv.cebbys.languages.ctd.define.typedef import *
from lv.cebbys.languages.ctd.define.enum import *
from lv.cebbys.languages.ctd.define.flag import *
from lv.cebbys.languages.ctd.define.structure import *
from lv.cebbys.languages.ctd.define.function import *
from lv.cebbys.languages.ctd.define.interface import *
from lv.cebbys.languages.ctd.define.collection import *

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
