import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdImportContextParser(Api.CtdDeclaractionContextParser[Api.CtdParser.TypedefDeclarationContext, Meta.TypedefMeta]):
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
        name = self._parseGetText(ctx.IDENTIFIER)
        # Get type specification
        type_spec = self._parseTypeSpec(ctx.typeSpec)
        # Create and add typedef metadata
        return Meta.TypedefMeta(name, type_spec, namespace)


INSTANCE = CtdImportContextParser()
