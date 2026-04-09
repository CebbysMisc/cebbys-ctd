import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.function as FunctionModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdClassContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdGrammar.ClassDeclarationContext, Meta.ClassMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdGrammar.ClassDeclarationContext, Meta.ClassMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdGrammar.ClassDeclarationContext) -> Meta.ClassMeta:
        """Parse class declaration and create ClassMeta.

        Args:
            namespace: Namespace to which this class belongs
            ctx: Class declaration context
        """
        name = self.text(self.token(ctx, Api.CtdGrammar.IDENTIFIER))

        # Get all base types (comma-separated after colon)
        bases: list[Meta.TypespecMeta] = [
            TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx)
            for typespec_ctx in self.rules(ctx, Api.CtdGrammar.TypeSpecContext)
        ]

        # Parse decorators
        decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
            self.rules(ctx, Api.CtdGrammar.DecoratorContext)
        )

        # Parse members (properties) from classMemberList
        members: list[Meta.ClassMemberMeta] = []
        member_list_ctx = self.optional_rule(ctx, Api.CtdGrammar.ClassMemberListContext)
        if member_list_ctx:
            for member_ctx in self.rules(member_list_ctx, Api.CtdGrammar.ClassMemberContext):
                member_name = self.text(self.token(member_ctx, Api.CtdGrammar.IDENTIFIER))
                member_typespec_ctx = self.rule(member_ctx, Api.CtdGrammar.TypeSpecContext)
                member_typespec = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(member_typespec_ctx)
                member_decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
                    self.rules(member_ctx, Api.CtdGrammar.DecoratorContext)
                )
                members.append(Meta.ClassMemberMeta(member_name, member_typespec, member_decorators))

        # Parse methods from classMethodList (reuses functionDeclaration)
        methods: list[Meta.FunctionMeta] = []
        method_list_ctx = self.optional_rule(ctx, Api.CtdGrammar.ClassMethodListContext)
        if method_list_ctx:
            function_parser = FunctionModule.CtdFunctionContextParser.instance()
            for method_ctx in self.rules(method_list_ctx, Api.CtdGrammar.FunctionDeclarationContext):
                methods.append(function_parser.parse(namespace, method_ctx))

        return Meta.ClassMeta(name, namespace, ctx, bases, members, methods, decorators)


INSTANCE = CtdClassContextParser()
