import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.types.meta as Meta
from pathlib import (
    Path as _Path
)

__all__ = ['CtdMetaParser']


class CtdMetaParser:
    """Static utility class for parsing CTD ANTLR4 contexts into Meta objects."""

    def __init__(self) -> None: ...

    # Context parser methods

    @staticmethod
    def parse_module(root:_Path, path:_Path, name:str, ctx: Antlr4.CtdGrammar.ModuleDeclarationContext) -> Meta.ModuleMeta: ...

    @staticmethod
    def parse_namespace(ctx: Antlr4.CtdGrammar.NamespaceDeclarationContext) -> Meta.NamespaceMeta: ...

    @staticmethod
    def parse_include(ctx: Antlr4.CtdGrammar.ImportDeclarationContext) -> Meta.IncludeMeta: ...

    @staticmethod
    def parse_decorator(ctx: Antlr4.CtdGrammar.DecoratorContext) -> Meta.DecoratorMeta: ...

    @staticmethod
    def parse_typespec(ctx: Antlr4.CtdGrammar.TypeSpecContext) -> Meta.TypespecMeta: ...

    @staticmethod
    def parse_declaration(namespace: str, ctx: Antlr4.CtdGrammar.DeclarationContext) -> Meta.DeclarationMeta: ...

    # Declaration parser methods

    @staticmethod
    def parse_typedef(namespace: str, ctx: Antlr4.CtdGrammar.TypedefDeclarationContext) -> Meta.TypedefMeta: ...

    @staticmethod
    def parse_alias(namespace: str, ctx: Antlr4.CtdGrammar.AliasDeclarationContext) -> Meta.AliasMeta: ...

    @staticmethod
    def parse_enum(namespace: str, ctx: Antlr4.CtdGrammar.EnumDeclarationContext) -> Meta.EnumMeta: ...

    @staticmethod
    def parse_flag(namespace: str, ctx: Antlr4.CtdGrammar.FlagDeclarationContext) -> Meta.FlagMeta: ...

    @staticmethod
    def parse_structure(namespace: str, ctx: Antlr4.CtdGrammar.StructureDeclarationContext) -> Meta.StructureMeta: ...

    @staticmethod
    def parse_interface(namespace: str, ctx: Antlr4.CtdGrammar.InterfaceDeclarationContext) -> Meta.InterfaceMeta: ...

    @staticmethod
    def parse_function(namespace: str, ctx: Antlr4.CtdGrammar.FunctionDeclarationContext) -> Meta.FunctionMeta: ...
