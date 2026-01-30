import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdTypedefContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdParser.TypedefDeclarationContext, Meta.TypedefMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdParser.TypedefDeclarationContext, Meta.TypedefMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdParser.TypedefDeclarationContext) -> Meta.TypedefMeta:
        """Visit typedef declaration and create TypedefMeta.

        Args:
            namespace:  Namespace to which this datatype belongs to
            ctx:        Typedef declaration context
        """
        # Get typedef name
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))
        # Get type specification
        typespec_rule = self.rule(ctx, Api.CtdParser.TypeSpecContext)
        typespec = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_rule)
        # Create and add typedef metadata
        return Meta.TypedefMeta(name, typespec, namespace)


INSTANCE = CtdTypedefContextParser()
