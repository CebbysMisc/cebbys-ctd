import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.meta.parser.typedef as TypedefModule
import typing as Typing


class CtdNamespaceContextParser(Api.CtdContextParserBase[Api.CtdParser.NamespaceDeclarationContext, Meta.NamespaceMeta]):
    def __init__(
        self,
        mappers: dict[
            type[Api.Antlr4.ParserRuleContext],
            tuple[
                type[Api.CtdDeclaractionContextParser[Typing.Any, Typing.Any]],
                Typing.Callable[[Meta.NamespaceMeta], Typing.Callable[[Typing.Any], None]]
            ]
        ]
    ) -> None:
        super().__init__()
        self._mappers = {
            k: (v.instance(), c) for k, (v, c) in mappers.items()
        }

    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdParser.NamespaceDeclarationContext, Meta.NamespaceMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdParser.NamespaceDeclarationContext):
        out = Meta.NamespaceMeta()
        for use_ctx in self.rules(ctx, Api.CtdParser.UseDeclarationContext):
            out.add_use(self.qualified_name(self.rule(use_ctx, Api.CtdParser.QualifiedNameContext)))

        namespace: str = self.qualified_name(self.rule(ctx, Api.CtdParser.QualifiedNameContext))
        for declaration_ctx in self.rules(ctx, Api.CtdParser.DeclarationContext):
            for ctx_type, (ctx_mapper, meta_consumer) in self._mappers.items():
                typed_ctx = self.optional_rule(declaration_ctx, ctx_type)
                if typed_ctx:
                    meta_consumer(out)(
                        ctx_mapper.parse(namespace, typed_ctx)
                    )
                    break

        return out


INSTANCE = CtdNamespaceContextParser({
    Api.CtdParser.TypedefDeclarationContext: (
        TypedefModule.CtdTypedefContextParser,
        lambda namespace: namespace.add_typedef
    )
})
