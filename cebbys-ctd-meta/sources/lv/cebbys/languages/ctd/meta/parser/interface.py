import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.function as FunctionModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdInterfaceContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdGrammar.InterfaceDeclarationContext, Meta.InterfaceMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdGrammar.InterfaceDeclarationContext, Meta.InterfaceMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdGrammar.InterfaceDeclarationContext) -> Meta.InterfaceMeta:
        """Parse interface declaration and create InterfaceMeta.

        Args:
            namespace: Namespace to which this interface belongs
            ctx: Interface declaration context
        """
        name = self.text(self.token(ctx, Api.CtdGrammar.IDENTIFIER))

        # Get optional base type (after colon)
        typespec_ctx = self.optional_rule(ctx, Api.CtdGrammar.TypeSpecContext)
        base_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx) if typespec_ctx else None

        # Parse decorators
        decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
            self.rules(ctx, Api.CtdGrammar.DecoratorContext)
        )

        # Parse methods
        methods: list[Meta.FunctionMeta] = []
        method_list_ctx = self.optional_rule(ctx, Api.CtdGrammar.InterfaceMethodListContext)
        if method_list_ctx:
            function_parser = FunctionModule.CtdFunctionContextParser.instance()
            for method_ctx in self.rules(method_list_ctx, Api.CtdGrammar.FunctionDeclarationContext):
                methods.append(function_parser.parse(namespace, method_ctx))

        return Meta.InterfaceMeta(name, namespace, ctx, base_type, methods, decorators)


INSTANCE = CtdInterfaceContextParser()
