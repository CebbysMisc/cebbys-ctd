import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.meta.parser.namespace as NamespaceModule
import lv.cebbys.languages.ctd.meta.parser.include as IncludeModule
import lv.cebbys.languages.ctd.utility.logging as Logging
import lv.cebbys.languages.ctd.types.meta as Meta


LOGGER = Logging.get_logger(__name__)
LOGGER.set_level(Logging.LogLevel.DEBUG)


class CtdModuleContextParser(Api.CtdContextParserBase[Api.CtdGrammar.ModuleDeclarationContext, Meta.ModuleMeta]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdGrammar.ModuleDeclarationContext, Meta.ModuleMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdGrammar.ModuleDeclarationContext):
        LOGGER.debug("Parsing module declaration")
        
        module = Meta.ModuleMeta()

        namespace_parser = NamespaceModule.CtdNamespaceContextParser.instance()
        import_parser = IncludeModule.CtdIncludeContextParser.instance()

        import_contexts = self.rules(ctx, Api.CtdGrammar.ImportDeclarationContext)
        namespace_contexts = self.rules(ctx, Api.CtdGrammar.NamespaceDeclarationContext)
        
        LOGGER.debug(f"Found {len(import_contexts)} import(s) and {len(namespace_contexts)} namespace(s)")

        for import_ctx in import_contexts:
            module.add_include(import_parser.parse(import_ctx))
        for namespace_ctx in namespace_contexts:
            module.add_namespace(namespace_parser.parse(namespace_ctx))
            
        LOGGER.debug(f"Module parsing complete: {len(module.includes)} include(s), {len(module.namespaces)} namespace(s)")
        
        return module


INSTANCE = CtdModuleContextParser()
