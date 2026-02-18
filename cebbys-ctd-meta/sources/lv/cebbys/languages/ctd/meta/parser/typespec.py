import lv.cebbys.languages.ctd.meta.parser.__api__ as Api


class CtdTypeSpecContextParser(Api.CtdContextParserBase[Api.CtdGrammar.TypeSpecContext, str]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdGrammar.TypeSpecContext, str]:
        return INSTANCE

    def parse(self, ctx: Api.CtdGrammar.TypeSpecContext):
        """Extract type specification as string.

        Args:
            ctx: Type spec context

        Returns:
            Type specification string
        """
        parts: list[str] = []

        # Handle sign modifier
        sign_ctx = self.optional_rule(ctx, Api.CtdGrammar.SignModifierContext)
        if sign_ctx:
            parts.append(self.text(sign_ctx))

        # Handle type reference
        type_ctx = self.optional_rule(ctx, Api.CtdGrammar.TypeReferenceContext)
        if type_ctx:
            qualified_ctx = self.optional_rule(type_ctx, Api.CtdGrammar.QualifiedNameContext)
            if qualified_ctx:
                parts.append(self.text(qualified_ctx))

        # Handle type extensions (multiple pointers and arrays in any order)
        # Check in typeSpec first, then in typeReference
        extension_contexts = self.rules(ctx, Api.CtdGrammar.TypeExtensionContext)
        if not extension_contexts and type_ctx:
            extension_contexts = self.rules(type_ctx, Api.CtdGrammar.TypeExtensionContext)

        for ext_ctx in extension_contexts:
            parts.append(self.text(ext_ctx))

        return ' '.join(parts)


INSTANCE = CtdTypeSpecContextParser()
