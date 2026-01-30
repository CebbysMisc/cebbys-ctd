import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdFunctionContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdParser.FunctionDeclarationContext, Meta.FunctionMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdParser.FunctionDeclarationContext, Meta.FunctionMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdParser.FunctionDeclarationContext) -> Meta.FunctionMeta:
        """Parse function declaration and create FunctionMeta.

        Args:
            namespace: Namespace to which this function belongs
            ctx: Function declaration context
        """
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))

        # Get return type
        typespec_ctx = self.rule(ctx, Api.CtdParser.TypeSpecContext)
        return_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx)

        # Parse decorators
        decorators: list[Meta.DecoratorMeta] = []
        decorator_parser = DecoratorModule.CtdDecoratorContextParser.instance()
        for decorator_ctx in self.rules(ctx, Api.CtdParser.DecoratorContext):
            decorators.append(decorator_parser.parse(decorator_ctx))

        # Parse parameters
        parameters: list[Meta.ParameterMeta] = []
        param_list_ctx = self.optional_rule(ctx, Api.CtdParser.ParameterListContext)
        if param_list_ctx:
            for param_ctx in self.rules(param_list_ctx, Api.CtdParser.ParameterContext):
                param_name = self.text(self.token(param_ctx, Api.CtdParser.IDENTIFIER))
                param_typespec_ctx = self.rule(param_ctx, Api.CtdParser.TypeSpecContext)
                param_typespec = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(param_typespec_ctx)

                # Parse parameter decorators
                param_decorators: list[Meta.DecoratorMeta] = []
                for param_decorator_ctx in self.rules(param_ctx, Api.CtdParser.DecoratorContext):
                    param_decorators.append(decorator_parser.parse(param_decorator_ctx))

                parameters.append(Meta.ParameterMeta(
                    param_name,
                    param_typespec,
                    param_decorators
                ))

        return Meta.FunctionMeta(
            name,
            namespace,
            return_type,
            parameters,
            decorators
        )


INSTANCE = CtdFunctionContextParser()
