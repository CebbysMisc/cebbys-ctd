from lv.cebbys.languages.ctd.meta.parser.__api__ import CtdDeclaractionContextParser
from lv.cebbys.languages.ctd.meta.parser.__api__ import CtdContextParser
import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import typing as Typing

C = Typing.TypeVar("C", bound=Antlr4.ParserRuleContext)
M = Typing.TypeVar("M")


def parser(ctx: type[C], meta: type[M]) -> type[CtdContextParser[C, M]]:
    return CtdContextParser[ctx, meta]


def declaration_parser(ctx: type[C], meta: type[M]) -> type[CtdDeclaractionContextParser[C, M]]:
    return CtdDeclaractionContextParser[ctx, meta]


# Context parsers (no namespace required)
CtdModuleContextParser = parser(Antlr4.CtdParser.ModuleDeclarationContext, Meta.ModuleMeta)
CtdNamespaceContextParser = parser(Antlr4.CtdParser.NamespaceDeclarationContext, Meta.NamespaceMeta)
CtdIncludeContextParser = parser(Antlr4.CtdParser.ImportDeclarationContext, Meta.IncludeMeta)
CtdDecoratorContextParser = parser(Antlr4.CtdParser.DecoratorContext, Meta.DecoratorMeta)
CtdTypeSpecContextParser = parser(Antlr4.CtdParser.TypeSpecContext, str)

# Declaration context parsers (namespace required)
CtdTypedefContextParser = declaration_parser(Antlr4.CtdParser.TypedefDeclarationContext, Meta.TypedefMeta)
CtdAliasContextParser = declaration_parser(Antlr4.CtdParser.AliasDeclarationContext, Meta.AliasMeta)
CtdEnumContextParser = declaration_parser(Antlr4.CtdParser.EnumDeclarationContext, Meta.EnumMeta)
CtdFlagContextParser = declaration_parser(Antlr4.CtdParser.FlagDeclarationContext, Meta.FlagMeta)
CtdStructureContextParser = declaration_parser(Antlr4.CtdParser.StructureDeclarationContext, Meta.StructureMeta)
CtdInterfaceContextParser = declaration_parser(Antlr4.CtdParser.InterfaceDeclarationContext, Meta.InterfaceMeta)
CtdFunctionContextParser = declaration_parser(Antlr4.CtdParser.FunctionDeclarationContext, Meta.FunctionMeta)

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
