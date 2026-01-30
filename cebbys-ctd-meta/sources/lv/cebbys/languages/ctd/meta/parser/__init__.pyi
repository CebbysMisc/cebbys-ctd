import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.types.meta as Meta

__all__ = ['CtdParser']


class CtdParser:
    """Static utility class for parsing CTD ANTLR4 contexts into Meta objects."""

    def __init__(self) -> None: ...

    # Context parser methods

    @staticmethod
    def parse_module(ctx: Antlr4.CtdParser.ModuleDeclarationContext) -> Meta.ModuleMeta: ...

    @staticmethod
    def parse_namespace(ctx: Antlr4.CtdParser.NamespaceDeclarationContext) -> Meta.NamespaceMeta: ...

    @staticmethod
    def parse_include(ctx: Antlr4.CtdParser.ImportDeclarationContext) -> Meta.IncludeMeta: ...

    @staticmethod
    def parse_decorator(ctx: Antlr4.CtdParser.DecoratorContext) -> Meta.DecoratorMeta: ...

    @staticmethod
    def parse_typespec(ctx: Antlr4.CtdParser.TypeSpecContext) -> str: ...

    # Declaration parser methods

    @staticmethod
    def parse_typedef(namespace: str, ctx: Antlr4.CtdParser.TypedefDeclarationContext) -> Meta.TypedefMeta: ...

    @staticmethod
    def parse_alias(namespace: str, ctx: Antlr4.CtdParser.AliasDeclarationContext) -> Meta.AliasMeta: ...

    @staticmethod
    def parse_enum(namespace: str, ctx: Antlr4.CtdParser.EnumDeclarationContext) -> Meta.EnumMeta: ...

    @staticmethod
    def parse_flag(namespace: str, ctx: Antlr4.CtdParser.FlagDeclarationContext) -> Meta.FlagMeta: ...

    @staticmethod
    def parse_structure(namespace: str, ctx: Antlr4.CtdParser.StructureDeclarationContext) -> Meta.StructureMeta: ...

    @staticmethod
    def parse_interface(namespace: str, ctx: Antlr4.CtdParser.InterfaceDeclarationContext) -> Meta.InterfaceMeta: ...

    @staticmethod
    def parse_function(namespace: str, ctx: Antlr4.CtdParser.FunctionDeclarationContext) -> Meta.FunctionMeta: ...
