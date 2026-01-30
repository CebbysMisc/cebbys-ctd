import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdIncludeContextParser(Api.CtdContextParserBase[Api.CtdGrammar.ImportDeclarationContext, Meta.IncludeMeta]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdGrammar.ImportDeclarationContext, Meta.IncludeMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdGrammar.ImportDeclarationContext):
        name: str = ctx.STRING_LITERAL().getText()[1:-1]  # type: ignore
        include = Meta.IncludeMeta()
        include.set_path(name)  # type: ignore
        return include


INSTANCE = CtdIncludeContextParser()
