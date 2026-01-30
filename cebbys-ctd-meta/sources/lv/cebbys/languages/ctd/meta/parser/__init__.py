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
    def __init__(self) -> None:
        # Context parsers
        self._module_parser = _ModuleModule.CtdModuleContextParser.instance()
        self._namespace_parser = _NamespaceModule.CtdNamespaceContextParser.instance()
        self._include_parser = _IncludeModule.CtdIncludeContextParser.instance()
        self._decorator_parser = _DecoratorModule.CtdDecoratorContextParser.instance()
        self._typespec_parser = _TypeSpecModule.CtdTypeSpecContextParser.instance()
        # Declaration parsers
        self._typedef_parser = _TypedefModule.CtdTypedefContextParser.instance()
        self._alias_parser = _AliasModule.CtdAliasContextParser.instance()
        self._enum_parser = _EnumModule.CtdEnumContextParser.instance()
        self._flag_parser = _FlagModule.CtdFlagContextParser.instance()
        self._structure_parser = _StructureModule.CtdStructureContextParser.instance()
        self._interface_parser = _InterfaceModule.CtdInterfaceContextParser.instance()
        self._function_parser = _FunctionModule.CtdFunctionContextParser.instance()

    # Context parser methods

    def parse_module(self, ctx: _Antlr4.CtdParser.ModuleDeclarationContext):
        return self._module_parser.parse(ctx)

    def parse_namespace(self, ctx: _Antlr4.CtdParser.NamespaceDeclarationContext):
        return self._namespace_parser.parse(ctx)

    def parse_include(self, ctx: _Antlr4.CtdParser.ImportDeclarationContext):
        return self._include_parser.parse(ctx)

    def parse_decorator(self, ctx: _Antlr4.CtdParser.DecoratorContext):
        return self._decorator_parser.parse(ctx)

    def parse_typespec(self, ctx: _Antlr4.CtdParser.TypeSpecContext):
        return self._typespec_parser.parse(ctx)

    # Declaration parser methods

    def parse_typedef(self, namespace: str, ctx: _Antlr4.CtdParser.TypedefDeclarationContext):
        return self._typedef_parser.parse(namespace, ctx)

    def parse_alias(self, namespace: str, ctx: _Antlr4.CtdParser.AliasDeclarationContext):
        return self._alias_parser.parse(namespace, ctx)

    def parse_enum(self, namespace: str, ctx: _Antlr4.CtdParser.EnumDeclarationContext):
        return self._enum_parser.parse(namespace, ctx)

    def parse_flag(self, namespace: str, ctx: _Antlr4.CtdParser.FlagDeclarationContext):
        return self._flag_parser.parse(namespace, ctx)

    def parse_structure(self, namespace: str, ctx: _Antlr4.CtdParser.StructureDeclarationContext):
        return self._structure_parser.parse(namespace, ctx)

    def parse_interface(self, namespace: str, ctx: _Antlr4.CtdParser.InterfaceDeclarationContext):
        return self._interface_parser.parse(namespace, ctx)

    def parse_function(self, namespace: str, ctx: _Antlr4.CtdParser.FunctionDeclarationContext):
        return self._function_parser.parse(namespace, ctx)
