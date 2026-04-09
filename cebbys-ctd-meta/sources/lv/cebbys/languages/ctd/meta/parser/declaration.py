import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.meta.parser.structure as StructureModule
import lv.cebbys.languages.ctd.meta.parser.interface as InterfaceModule
import lv.cebbys.languages.ctd.meta.parser.function as FunctionModule
import lv.cebbys.languages.ctd.meta.parser.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.parser.alias as AliasModule
import lv.cebbys.languages.ctd.meta.parser.enum as EnumModule
import lv.cebbys.languages.ctd.meta.parser.flag as FlagModule
import lv.cebbys.languages.ctd.meta.parser.clazz as ClazzModule
import lv.cebbys.languages.ctd.types.meta as Meta
import typing as Typing


class CtdDeclarationContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdGrammar.DeclarationContext, Meta.DeclarationMeta]):
    def __init__(
        self,
        mappers: dict[
            type[Api.Antlr4.ParserRuleContext],
            type[Api.CtdDeclaractionContextParser[Typing.Any, Typing.Any]]
        ]
    ) -> None:
        super().__init__()
        self._mappers = {
            k: v.instance() for k, v, in mappers.items()
        }

    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdGrammar.DeclarationContext, Meta.DeclarationMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdGrammar.DeclarationContext) -> Meta.DeclarationMeta:
        for ctx_type, ctx_mapper in self._mappers.items():
            typed_ctx = self.optional_rule(ctx, ctx_type)
            if typed_ctx:
                return ctx_mapper.parse(namespace, typed_ctx)
        raise BaseException(f"Parser not found for '{type(ctx)}'")


INSTANCE = CtdDeclarationContextParser({
    Api.CtdGrammar.TypedefDeclarationContext: TypedefModule.CtdTypedefContextParser,
    Api.CtdGrammar.AliasDeclarationContext: AliasModule.CtdAliasContextParser,
    Api.CtdGrammar.EnumDeclarationContext: EnumModule.CtdEnumContextParser,
    Api.CtdGrammar.FlagDeclarationContext: FlagModule.CtdFlagContextParser,
    Api.CtdGrammar.StructureDeclarationContext: StructureModule.CtdStructureContextParser,
    Api.CtdGrammar.InterfaceDeclarationContext: InterfaceModule.CtdInterfaceContextParser,
    Api.CtdGrammar.FunctionDeclarationContext: FunctionModule.CtdFunctionContextParser,
    Api.CtdGrammar.ClassDeclarationContext: ClazzModule.CtdClassContextParser,
})
