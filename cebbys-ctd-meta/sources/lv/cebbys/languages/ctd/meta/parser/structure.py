import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdStructureContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdGrammar.StructureDeclarationContext, Meta.StructureMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdGrammar.StructureDeclarationContext, Meta.StructureMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdGrammar.StructureDeclarationContext) -> Meta.StructureMeta:
        """Parse structure declaration and create StructureMeta.

        Args:
            namespace: Namespace to which this structure belongs
            ctx: Structure declaration context
        """
        name = self.text(self.token(ctx, Api.CtdGrammar.IDENTIFIER))

        # Get optional base type (after colon)
        typespec_ctx = self.optional_rule(ctx, Api.CtdGrammar.TypeSpecContext)
        base_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx) if typespec_ctx else None

        # Parse decorators
        decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
            self.rules(ctx, Api.CtdGrammar.DecoratorContext)
        )

        # Parse members
        members: list[Meta.StructureMemberMeta] = []
        member_list_ctx = self.optional_rule(ctx, Api.CtdGrammar.StructureMemberListContext)
        if member_list_ctx:
            for member_ctx in self.rules(member_list_ctx, Api.CtdGrammar.StructureMemberContext):
                member_name = self.text(self.token(member_ctx, Api.CtdGrammar.IDENTIFIER))
                member_typespec_ctx = self.rule(member_ctx, Api.CtdGrammar.TypeSpecContext)
                member_typespec = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(member_typespec_ctx)
                members.append(Meta.StructureMemberMeta(member_name, member_typespec))

        return Meta.StructureMeta(name, namespace, base_type, members, decorators)


INSTANCE = CtdStructureContextParser()
