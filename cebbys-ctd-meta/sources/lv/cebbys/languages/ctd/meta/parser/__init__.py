import lv.cebbys.languages.ctd.meta.parser.module as _ModuleModule
import lv.cebbys.languages.ctd.meta.parser.namespace as _NamespaceModule
import lv.cebbys.languages.ctd.meta.parser.include as _IncludeModule
import lv.cebbys.languages.ctd.meta.parser.decorator as _DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.typespec as _TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.declaration as _DeclarationModule
import lv.cebbys.languages.ctd.meta.parser.typedef as _TypedefModule
import lv.cebbys.languages.ctd.meta.parser.alias as _AliasModule
import lv.cebbys.languages.ctd.meta.parser.enum as _EnumModule
import lv.cebbys.languages.ctd.meta.parser.flag as _FlagModule
import lv.cebbys.languages.ctd.meta.parser.structure as _StructureModule
import lv.cebbys.languages.ctd.meta.parser.interface as _InterfaceModule
import lv.cebbys.languages.ctd.meta.parser.function as _FunctionModule
import lv.cebbys.languages.ctd.antlr4 as _Antlr4

__all__ = ['CtdMetaParser']


class CtdMetaParser:
    """Static utility class for parsing CTD ANTLR4 contexts into Meta objects."""

    def __init__(self) -> None:
        raise TypeError("CtdMetaParser is a static utility class and cannot be instantiated")

    # Context parser methods

    @staticmethod
    def parse_module(ctx: _Antlr4.CtdGrammar.ModuleDeclarationContext):
        return _ModuleModule.CtdModuleContextParser.instance().parse(ctx)

    @staticmethod
    def parse_namespace(ctx: _Antlr4.CtdGrammar.NamespaceDeclarationContext):
        return _NamespaceModule.CtdNamespaceContextParser.instance().parse(ctx)

    @staticmethod
    def parse_include(ctx: _Antlr4.CtdGrammar.ImportDeclarationContext):
        return _IncludeModule.CtdIncludeContextParser.instance().parse(ctx)

    @staticmethod
    def parse_decorator(ctx: _Antlr4.CtdGrammar.DecoratorContext):
        return _DecoratorModule.CtdDecoratorContextParser.instance().parse(ctx)

    @staticmethod
    def parse_typespec(ctx: _Antlr4.CtdGrammar.TypeSpecContext):
        return _TypeSpecModule.CtdTypeSpecContextParser.instance().parse(ctx)

    @staticmethod
    def parse_declaration(namespace: str, ctx: _Antlr4.CtdGrammar.DeclarationContext):
        return _DeclarationModule.CtdDeclarationContextParser.instance().parse(namespace, ctx)

    # Declaration parser methods

    @staticmethod
    def parse_typedef(namespace: str, ctx: _Antlr4.CtdGrammar.TypedefDeclarationContext):
        return _TypedefModule.CtdTypedefContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_alias(namespace: str, ctx: _Antlr4.CtdGrammar.AliasDeclarationContext):
        return _AliasModule.CtdAliasContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_enum(namespace: str, ctx: _Antlr4.CtdGrammar.EnumDeclarationContext):
        return _EnumModule.CtdEnumContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_flag(namespace: str, ctx: _Antlr4.CtdGrammar.FlagDeclarationContext):
        return _FlagModule.CtdFlagContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_structure(namespace: str, ctx: _Antlr4.CtdGrammar.StructureDeclarationContext):
        return _StructureModule.CtdStructureContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_interface(namespace: str, ctx: _Antlr4.CtdGrammar.InterfaceDeclarationContext):
        return _InterfaceModule.CtdInterfaceContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_function(namespace: str, ctx: _Antlr4.CtdGrammar.FunctionDeclarationContext):
        return _FunctionModule.CtdFunctionContextParser.instance().parse(namespace, ctx)
