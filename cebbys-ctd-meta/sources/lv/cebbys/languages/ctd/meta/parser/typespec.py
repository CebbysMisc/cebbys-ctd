import lv.cebbys.languages.ctd.meta.parser.__api__ as Api


class CtdTypeSpecContextParser(Api.CtdContextParserBase[Api.CtdParser.TypeSpecContext, str]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdParser.TypeSpecContext, str]:
        return INSTANCE

    def parse(self, ctx: Api.CtdParser.TypeSpecContext):
        """Extract type specification as string.

        Args:
            ctx: Type spec context

        Returns:
            Type specification string
        """
        parts: list[str] = []

        # Handle sign modifier
        sign_ctx = self.optional_rule(ctx, Api.CtdParser.SignModifierContext)
        if sign_ctx:
            parts.append(self.text(sign_ctx))

        primitive_ctx = self.optional_rule(ctx, Api.CtdParser.PrimitiveTypeContext)
        if primitive_ctx:
            parts.append(self.text(primitive_ctx))

        # Handle type reference
        type_ctx = self.optional_rule(ctx, Api.CtdParser.TypeReferenceContext)
        if type_ctx:
            qualified_ctx = self.optional_rule(type_ctx, Api.CtdParser.QualifiedNameContext)
            if qualified_ctx:
                parts.append(self.text(qualified_ctx))

        # Handle array modifier - check in typeSpec first, then in typeReference
        array_ctx = self.optional_rule(ctx, Api.CtdParser.ArrayModifierContext)
        if array_ctx is None and type_ctx:
            array_ctx = self.optional_rule(type_ctx, Api.CtdParser.ArrayModifierContext)

        if array_ctx:
            parts.append(self.text(array_ctx))

        # Handle pointer modifier - check in typeSpec first, then in typeReference
        pointer_ctx = self.optional_rule(ctx, Api.CtdParser.PointerModifierContext)
        if pointer_ctx is None and type_ctx:
            pointer_ctx = self.optional_rule(type_ctx, Api.CtdParser.PointerModifierContext)

        if pointer_ctx:
            parts.append(self.text(pointer_ctx))

        return ' '.join(parts)


INSTANCE = CtdTypeSpecContextParser()
