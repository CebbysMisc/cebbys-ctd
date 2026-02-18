"""Single test case for meta typespec mapping.

Tests the complete typespec mapping pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → TypespecMeta object (via Parser.CtdMetaParser)
3. TypespecMeta validation

Run with:
    uv run pytest cebbys-ctd-meta/tests/test_parse_typespec.py -v -s
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def test_typespec_mapping() -> None:
    """Test typespec mapping from CTD string to TypespecMeta object."""
    ctd_parser: Antlr4.CtdParser
    typespec_ctx: Antlr4.CtdGrammar.TypeSpecContext
    typespec_meta: Meta.TypespecMeta
    
    TestLogger.header("MetaParser: Typespec Mapping Test")
    
    # Test case: multi-extension type int[3]**[4]*
    # Structure: Pointer -> Array[4] -> Pointer -> Pointer -> Array[3] -> TypedTypespec(int)
    ctd_string: str = "int[3]**[4]*"
    
    # Step 1: Parse CTD string into ANTLR4 context
    TestLogger.info(f"Parsing CTD string: '{ctd_string}'")
    ctd_parser = Antlr4.CtdParser()
    typespec_ctx = ctd_parser.typeSpec(ctd_string)
    
    assert typespec_ctx is not None, "Failed to create ANTLR4 context"
    assert isinstance(typespec_ctx, Antlr4.CtdGrammar.TypeSpecContext), "Invalid context type"
    TestLogger.success("✓ Step 1: ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to TypespecMeta object
    TestLogger.info("Mapping ANTLR4 context to TypespecMeta")
    typespec_meta = Parser.CtdMetaParser.parse_typespec(typespec_ctx)
    
    assert typespec_meta is not None, "Failed to create TypespecMeta"
    assert isinstance(typespec_meta, Meta.TypespecMeta), "Invalid TypespecMeta type"
    TestLogger.success(f"✓ Step 2: TypespecMeta created: {type(typespec_meta).__name__}")
    
    # Step 3: Validate TypespecMeta structure
    # Expected: Pointer -> Array[4] -> Pointer -> Pointer -> Array[3] -> TypedTypespec(int)
    TestLogger.info("Validating TypespecMeta structure")
    
    # Outermost: pointer
    assert isinstance(typespec_meta, Meta.PointerTypespecMeta), "Expected outermost to be PointerTypespecMeta"
    TestLogger.success("  ✓ Level 0: PointerTypespecMeta (*)")
    
    # Next: array[4]
    assert isinstance(typespec_meta.base, Meta.ArrayTypespecMeta), "Expected next to be ArrayTypespecMeta"
    assert typespec_meta.base.size == 4, f"Expected array size 4, got {typespec_meta.base.size}"
    TestLogger.success("  ✓ Level 1: ArrayTypespecMeta ([4])")
    
    # Next: pointer
    assert isinstance(typespec_meta.base.base, Meta.PointerTypespecMeta), "Expected next to be PointerTypespecMeta"
    TestLogger.success("  ✓ Level 2: PointerTypespecMeta (*)")
    
    # Next: pointer
    assert isinstance(typespec_meta.base.base.base, Meta.PointerTypespecMeta), "Expected next to be PointerTypespecMeta"
    TestLogger.success("  ✓ Level 3: PointerTypespecMeta (*)")
    
    # Next: array[3]
    assert isinstance(typespec_meta.base.base.base.base, Meta.ArrayTypespecMeta), "Expected next to be ArrayTypespecMeta"
    assert typespec_meta.base.base.base.base.size == 3, f"Expected array size 3, got {typespec_meta.base.base.base.base.size}"
    TestLogger.success("  ✓ Level 4: ArrayTypespecMeta ([3])")
    
    # Base: int
    assert isinstance(typespec_meta.base.base.base.base.base, Meta.TypedTypespecMeta), "Expected base to be TypedTypespecMeta"
    assert typespec_meta.base.base.base.base.base.qualified_name == "int", \
        f"Expected qualified_name 'int', got '{typespec_meta.base.base.base.base.base.qualified_name}'"
    assert typespec_meta.base.base.base.base.base.signed is None, "Expected signed to be None"
    TestLogger.success("  ✓ Level 5: TypedTypespecMeta (int)")
    
    TestLogger.complete()


if __name__ == "__main__":
    """Run the test directly with: python test_parse_typespec.py"""
    test_typespec_mapping()
    print("\n✅ Test passed successfully!")
