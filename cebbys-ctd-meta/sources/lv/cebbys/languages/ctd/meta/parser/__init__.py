import lv.cebbys.languages.ctd.meta.parser.module as _ModuleModule
import lv.cebbys.languages.ctd.meta.parser.namespace as _NamespaceModule
import lv.cebbys.languages.ctd.meta.parser.include as _IncludeModule
import lv.cebbys.languages.ctd.meta.parser.decorator as _DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.typespec as _TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.typedef as _TypedefModule
import lv.cebbys.languages.ctd.meta.parser.alias as _AliasModule
import lv.cebbys.languages.ctd.meta.parser.enum as _EnumModule
import lv.cebbys.languages.ctd.meta.parser.flag as _FlagModule
import lv.cebbys.languages.ctd.meta.parser.structure as _StructureModule
import lv.cebbys.languages.ctd.meta.parser.interface as _InterfaceModule
import lv.cebbys.languages.ctd.meta.parser.function as _FunctionModule
import lv.cebbys.languages.ctd.antlr4 as _Antlr4

__all__ = ['CtdParser']


class CtdParser:
    """Static utility class for parsing CTD ANTLR4 contexts into Meta objects."""

    def __init__(self) -> None:
        raise TypeError("CtdParser is a static utility class and cannot be instantiated")

    # Context parser methods

    @staticmethod
    def parse_module(ctx: _Antlr4.CtdParser.ModuleDeclarationContext):
        return _ModuleModule.CtdModuleContextParser.instance().parse(ctx)

    @staticmethod
    def parse_namespace(ctx: _Antlr4.CtdParser.NamespaceDeclarationContext):
        return _NamespaceModule.CtdNamespaceContextParser.instance().parse(ctx)

    @staticmethod
    def parse_include(ctx: _Antlr4.CtdParser.ImportDeclarationContext):
        return _IncludeModule.CtdIncludeContextParser.instance().parse(ctx)

    @staticmethod
    def parse_decorator(ctx: _Antlr4.CtdParser.DecoratorContext):
        return _DecoratorModule.CtdDecoratorContextParser.instance().parse(ctx)

    @staticmethod
    def parse_typespec(ctx: _Antlr4.CtdParser.TypeSpecContext):
        return _TypeSpecModule.CtdTypeSpecContextParser.instance().parse(ctx)

    # Declaration parser methods

    @staticmethod
    def parse_typedef(namespace: str, ctx: _Antlr4.CtdParser.TypedefDeclarationContext):
        return _TypedefModule.CtdTypedefContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_alias(namespace: str, ctx: _Antlr4.CtdParser.AliasDeclarationContext):
        return _AliasModule.CtdAliasContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_enum(namespace: str, ctx: _Antlr4.CtdParser.EnumDeclarationContext):
        return _EnumModule.CtdEnumContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_flag(namespace: str, ctx: _Antlr4.CtdParser.FlagDeclarationContext):
        return _FlagModule.CtdFlagContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_structure(namespace: str, ctx: _Antlr4.CtdParser.StructureDeclarationContext):
        return _StructureModule.CtdStructureContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_interface(namespace: str, ctx: _Antlr4.CtdParser.InterfaceDeclarationContext):
        return _InterfaceModule.CtdInterfaceContextParser.instance().parse(namespace, ctx)

    @staticmethod
    def parse_function(namespace: str, ctx: _Antlr4.CtdParser.FunctionDeclarationContext):
        return _FunctionModule.CtdFunctionContextParser.instance().parse(namespace, ctx)
