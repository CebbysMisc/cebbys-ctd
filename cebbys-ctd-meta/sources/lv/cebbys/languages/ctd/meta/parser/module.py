import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.meta.parser.namespace as NamespaceModule
import lv.cebbys.languages.ctd.meta.parser.include as IncludeModule
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdModuleContextParser(Api.CtdContextParserBase[Api.CtdParser.ModuleDeclarationContext, Meta.ModuleMeta]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdParser.ModuleDeclarationContext, Meta.ModuleMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdParser.ModuleDeclarationContext):
        module = Meta.ModuleMeta()

        namespace_parser = NamespaceModule.CtdNamespaceContextParser.instance()
        import_parser = IncludeModule.CtdIncludeContextParser.instance()

        for import_ctx in self.rules(ctx, Api.CtdParser.ImportDeclarationContext):
            module.add_include(import_parser.parse(import_ctx))
        for namespace_ctx in self.rules(ctx, Api.CtdParser.NamespaceDeclarationContext):
            module.add_namespace(namespace_parser.parse(namespace_ctx))
        return module


INSTANCE = CtdModuleContextParser()
