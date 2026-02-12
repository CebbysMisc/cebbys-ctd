import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.decorator as DecoratorModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


class CtdEnumContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdGrammar.EnumDeclarationContext, Meta.EnumMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdGrammar.EnumDeclarationContext, Meta.EnumMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdGrammar.EnumDeclarationContext) -> Meta.EnumMeta:
        """Parse enum declaration and create EnumMeta.

        Args:
            namespace: Namespace to which this enum belongs
            ctx: Enum declaration context
        """
        LOGGER.trace("Parsing enum declaration")

        name = self.text(self.token(ctx, Api.CtdGrammar.IDENTIFIER))

        # Get base type
        typespec_ctx = self.optional_rule(ctx, Api.CtdGrammar.TypeSpecContext)
        base_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx) if typespec_ctx else None

        # Parse decorators
        decorators = DecoratorModule.CtdDecoratorContextParser.instance().parse_all(
            self.rules(ctx, Api.CtdGrammar.DecoratorContext)
        )

        # Parse members
        members: list[Meta.EnumMemberMeta] = []
        member_list_ctx = self.optional_rule(ctx, Api.CtdGrammar.EnumMemberListContext)
        if member_list_ctx:
            for member_ctx in self.rules(member_list_ctx, Api.CtdGrammar.EnumMemberContext):
                member_name = self.text(self.token(member_ctx, Api.CtdGrammar.IDENTIFIER))
                member_value = self._parse_member_value(member_ctx)
                members.append(Meta.EnumMemberMeta(member_name, member_value))

        return Meta.EnumMeta(name, namespace, base_type, members, decorators)

    def _parse_member_value(self, ctx: Api.CtdGrammar.EnumMemberContext) -> int | None:
        """Parse optional member value (integer or hex literal)."""
        int_token = self.optional_token(ctx, Api.CtdGrammar.INTEGER_LITERAL)
        if int_token:
            return int(self.text(int_token))

        hex_token = self.optional_token(ctx, Api.CtdGrammar.HEX_LITERAL)
        if hex_token:
            return int(self.text(hex_token), 16)

        return None


INSTANCE = CtdEnumContextParser()
