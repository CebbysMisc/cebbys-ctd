import lv.cebbys.languages.ctd.meta.parser.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as Meta


class CtdTypeSpecContextParser(Api.CtdContextParserBase[Api.CtdGrammar.TypeSpecContext, Meta.TypespecMeta]):
    @staticmethod
    def instance() -> Api.CtdContextParser[Api.CtdGrammar.TypeSpecContext, Meta.TypespecMeta]:
        return INSTANCE

    def parse(self, ctx: Api.CtdGrammar.TypeSpecContext) -> Meta.TypespecMeta:
        """Extract type specification and create TypespecMeta.

        Args:
            ctx: Type spec context

        Returns:
            TypespecMeta object representing the type specification
        """
        signed: bool | None = None
        qualified_name: str
        base_type: Meta.TypespecMeta
        
        # Handle sign modifier
        sign_ctx = self.optional_rule(ctx, Api.CtdGrammar.SignModifierContext)
        if sign_ctx:
            sign_text: str = self.text(sign_ctx)
            signed = sign_text == "signed"

        # Handle type reference (required)
        type_ctx = self.optional_rule(ctx, Api.CtdGrammar.TypeReferenceContext)
        if not type_ctx:
            raise ValueError("TypeSpec must have a type reference")
            
        qualified_ctx = self.optional_rule(type_ctx, Api.CtdGrammar.QualifiedNameContext)
        if not qualified_ctx:
            raise ValueError("TypeReference must have a qualified name")
            
        qualified_name = self.text(qualified_ctx)
        
        # Create base typed typespec
        base_type = Meta.TypedTypespecMeta(qualified_name, signed)

        # Handle type extensions (multiple pointers and arrays in any order)
        extension_contexts = self.rules(type_ctx, Api.CtdGrammar.TypeExtensionContext)
        
        # Apply extensions in order, building nested TypespecMeta objects
        current_type: Meta.TypespecMeta = base_type
        for ext_ctx in extension_contexts:
            array_ctx = self.optional_rule(ext_ctx, Api.CtdGrammar.ArrayModifierContext)
            pointer_ctx = self.optional_rule(ext_ctx, Api.CtdGrammar.PointerModifierContext)
            
            if array_ctx:
                # Extract array size from [N]
                size_text: str = self.text(array_ctx)
                size_str: str = size_text.strip('[]')
                size: int = int(size_str)
                current_type = Meta.ArrayTypespecMeta(current_type, size)
            elif pointer_ctx:
                current_type = Meta.PointerTypespecMeta(current_type)
        
        return current_type


INSTANCE = CtdTypeSpecContextParser()
