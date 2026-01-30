import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.function as FunctionModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdInterfaceContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdParser.InterfaceDeclarationContext, Meta.InterfaceMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdParser.InterfaceDeclarationContext, Meta.InterfaceMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdParser.InterfaceDeclarationContext) -> Meta.InterfaceMeta:
        """Parse interface declaration and create InterfaceMeta.

        Args:
            namespace: Namespace to which this interface belongs
            ctx: Interface declaration context
        """
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))

        # Get optional base type (after colon)
        typespec_ctx = self.optional_rule(ctx, Api.CtdParser.TypeSpecContext)
        base_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx) if typespec_ctx else None

        # Parse methods
        methods: list[Meta.FunctionMeta] = []
        method_list_ctx = self.optional_rule(ctx, Api.CtdParser.InterfaceMethodListContext)
        if method_list_ctx:
            function_parser = FunctionModule.CtdFunctionContextParser.instance()
            for method_ctx in self.rules(method_list_ctx, Api.CtdParser.FunctionDeclarationContext):
                methods.append(function_parser.parse(namespace, method_ctx))

        return Meta.InterfaceMeta(name, namespace, base_type, methods if methods else None)


INSTANCE = CtdInterfaceContextParser()
