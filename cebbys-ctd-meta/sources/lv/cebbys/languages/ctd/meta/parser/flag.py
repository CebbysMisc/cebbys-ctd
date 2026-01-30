import lv.cebbys.languages.ctd.meta.parser.typespec as TypeSpecModule
import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdFlagContextParser(Api.CtdDeclaractionContextParserBase[Api.CtdParser.FlagDeclarationContext, Meta.FlagMeta]):
    @staticmethod
    def instance() -> Api.CtdDeclaractionContextParser[Api.CtdParser.FlagDeclarationContext, Meta.FlagMeta]:
        return INSTANCE

    def parse(self, namespace: str, ctx: Api.CtdParser.FlagDeclarationContext) -> Meta.FlagMeta:
        """Parse flag declaration and create FlagMeta.

        Args:
            namespace: Namespace to which this flag belongs
            ctx: Flag declaration context
        """
        name = self.text(self.token(ctx, Api.CtdParser.IDENTIFIER))

        # Get base type
        typespec_ctx = self.optional_rule(ctx, Api.CtdParser.TypeSpecContext)
        base_type = TypeSpecModule.CtdTypeSpecContextParser.instance().parse(typespec_ctx) if typespec_ctx else None

        # Parse members
        members: list[Meta.FlagMemberMeta] = []
        member_list_ctx = self.optional_rule(ctx, Api.CtdParser.FlagMemberListContext)
        if member_list_ctx:
            for member_ctx in self.rules(member_list_ctx, Api.CtdParser.FlagMemberContext):
                member_name = self.text(self.token(member_ctx, Api.CtdParser.IDENTIFIER))
                member_value = self._parse_member_value(member_ctx)
                members.append(Meta.FlagMemberMeta(member_name, member_value))

        return Meta.FlagMeta(name, namespace, base_type, members)

    def _parse_member_value(self, ctx: Api.CtdParser.FlagMemberContext) -> int | None:
        """Parse optional member value (integer or hex literal)."""
        int_token = self.optional_token(ctx, Api.CtdParser.INTEGER_LITERAL)
        if int_token:
            return int(self.text(int_token))

        hex_token = self.optional_token(ctx, Api.CtdParser.HEX_LITERAL)
        if hex_token:
            return int(self.text(hex_token), 16)

        return None


INSTANCE = CtdFlagContextParser()
