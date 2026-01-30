import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdAliasContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdParser.AliasDeclarationContext, Meta.AliasMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdParser.AliasDeclarationContext, Meta.AliasMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdParser.AliasDeclarationContext) -> Meta.AliasMeta:
        """Parse alias declaration and create AliasMeta.

        Args:
            namespace: Namespace to which this alias belongs
            ctx: Alias declaration context
        """
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))
        typespec_rule = self.rule(ctx, Api.CtdParser.TypeSpecContext)
        typespec = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_rule)
        # Parse decorators
        decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
            self.rules(ctx, Api.CtdParser.DecoratorContext)
        )
        return Meta.AliasMeta(name, typespec, namespace, decorators)


INSTANCE = CtdAliasContextParser()
