from lv.cebbys.languages.ctd.meta.parser.__api__ import CtdDeclaractionContextParser
from lv.cebbys.languages.ctd.meta.parser.__api__ import CtdContextParser
import lv.cebbys.languages.ctd.meta.parser.module as ModuleModule
import lv.cebbys.languages.ctd.meta.parser.namespace as NamespaceModule
import lv.cebbys.languages.ctd.meta.parser.include as IncludeModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.parser.alias as AliasModule
import lv.cebbys.languages.ctd.meta.parser.enum as EnumModule
import lv.cebbys.languages.ctd.meta.parser.flag as FlagModule
import lv.cebbys.languages.ctd.meta.parser.structure as StructureModule
import lv.cebbys.languages.ctd.meta.parser.interface as InterfaceModule
import lv.cebbys.languages.ctd.meta.parser.function as FunctionModule
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import typing as Typing

C = Typing.TypeVar("C", bound=Antlr4.ParserRuleContext)
M = Typing.TypeVar("M")


def parser(parser: type[CtdContextParser[C, M]]) -> type[CtdContextParser[C, M]]:
    return parser


def declaration_parser(parser: type[CtdDeclaractionContextParser[C, M]]) -> type[CtdDeclaractionContextParser[C, M]]:
    return parser


# Context parsers (no namespace required)
CtdModuleContextParser = parser(ModuleModule.CtdModuleContextParser)
CtdNamespaceContextParser = parser(NamespaceModule.CtdNamespaceContextParser)
CtdIncludeContextParser = parser(IncludeModule.CtdIncludeContextParser)
CtdDecoratorContextParser = parser(DecoratorModule.CtdDecoratorContextParser)
CtdTypeSpecContextParser = parser(TypeSpecModule.CtdTypeSpecContextParser)

# Declaration context parsers (namespace required)
CtdTypedefContextParser = declaration_parser(TypedefModule.CtdTypedefContextParser)
CtdAliasContextParser = declaration_parser(AliasModule.CtdAliasContextParser)
CtdEnumContextParser = declaration_parser(EnumModule.CtdEnumContextParser)
CtdFlagContextParser = declaration_parser(FlagModule.CtdFlagContextParser)
CtdStructureContextParser = declaration_parser(StructureModule.CtdStructureContextParser)
CtdInterfaceContextParser = declaration_parser(InterfaceModule.CtdInterfaceContextParser)
CtdFunctionContextParser = declaration_parser(FunctionModule.CtdFunctionContextParser)

__all__ = [
    # Base interfaces
    'CtdContextParser',
    'CtdDeclaractionContextParser',
    # Context parsers
    'CtdModuleContextParser',
    'CtdNamespaceContextParser',
    'CtdIncludeContextParser',
    'CtdDecoratorContextParser',
    'CtdTypeSpecContextParser',
    # Declaration context parsers
    'CtdTypedefContextParser',
    'CtdAliasContextParser',
    'CtdEnumContextParser',
    'CtdFlagContextParser',
    'CtdStructureContextParser',
    'CtdInterfaceContextParser',
    'CtdFunctionContextParser',
]
