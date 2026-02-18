"""Tests for CtdParser type specification parsing.

Validates that CtdParser correctly parses type specifications into ANTLR4 contexts.
These tests focus on the parser's ability to recognize valid syntax, not semantic validation.
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def _parse_typespec(ctd_string: str) -> Antlr4.CtdGrammar.TypeSpecContext:
    """Helper function to parse CTD typespec string into ANTLR4 context.
    
    Args:
        ctd_string: CTD typespec string
        
    Returns:
        TypeSpecContext from ANTLR4 parser
    """
    ctd_parser: Antlr4.CtdParser
    typespec_ctx: Antlr4.CtdGrammar.TypeSpecContext
    
    # Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    typespec_ctx = ctd_parser.typeSpec(ctd_string)
    
    assert typespec_ctx is not None
    assert isinstance(typespec_ctx, Antlr4.CtdGrammar.TypeSpecContext)
    
    return typespec_ctx


def test_parse_simple_type() -> None:
    """Test parsing a simple type."""
    TestLogger.header("CtdParser: Simple Type")

    ctx = _parse_typespec("Int4")
    
    # Verify context structure
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Int4"
    
    TestLogger.success("Simple type parsed correctly")
    TestLogger.complete()


def test_parse_primitive_type() -> None:
    """Test parsing primitive-named types (now treated as regular type references)."""
    TestLogger.header("CtdParser: Primitive-Named Types")

    primitives = ["char", "short", "int", "long", "void"]
    
    for primitive in primitives:
        ctx = _parse_typespec(primitive)
        assert ctx.typeReference() is not None
        assert ctx.typeReference().qualifiedName().getText() == primitive
        TestLogger.success(f"Primitive-named type '{primitive}' parsed correctly")
    
    TestLogger.complete()


def test_parse_signed_type() -> None:
    """Test parsing signed types."""
    TestLogger.header("CtdParser: Signed Types")

    ctx = _parse_typespec("signed int")
    
    assert ctx.signModifier() is not None
    assert ctx.signModifier().getText() == "signed"
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "int"
    
    TestLogger.success("Signed type parsed correctly")
    TestLogger.complete()


def test_parse_unsigned_type() -> None:
    """Test parsing unsigned types."""
    TestLogger.header("CtdParser: Unsigned Types")

    ctx = _parse_typespec("unsigned int")
    
    assert ctx.signModifier() is not None
    assert ctx.signModifier().getText() == "unsigned"
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "int"
    
    TestLogger.success("Unsigned type parsed correctly")
    TestLogger.complete()


def test_parse_signed_custom_type() -> None:
    """Test parsing signed modifier with custom type."""
    TestLogger.header("CtdParser: Signed Custom Type")

    ctx = _parse_typespec("signed Int4")
    
    assert ctx.signModifier() is not None
    assert ctx.signModifier().getText() == "signed"
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Int4"
    
    TestLogger.success("Signed custom type parsed correctly")
    TestLogger.complete()


def test_parse_unsigned_custom_type() -> None:
    """Test parsing unsigned modifier with custom type."""
    TestLogger.header("CtdParser: Unsigned Custom Type")

    ctx = _parse_typespec("unsigned Int4")
    
    assert ctx.signModifier() is not None
    assert ctx.signModifier().getText() == "unsigned"
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Int4"
    
    TestLogger.success("Unsigned custom type parsed correctly")
    TestLogger.complete()


def test_parse_pointer_type() -> None:
    """Test parsing a pointer type."""
    TestLogger.header("CtdParser: Pointer Type")

    ctx = _parse_typespec("Void*")
    
    # Verify type reference
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Void"
    
    # Verify single pointer extension
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 1
    assert extensions[0].pointerModifier() is not None
    assert extensions[0].pointerModifier().getText() == "*"
    
    TestLogger.success("Pointer type parsed correctly")
    TestLogger.complete()


def test_parse_double_pointer_type() -> None:
    """Test parsing a double pointer type."""
    TestLogger.header("CtdParser: Double Pointer Type")

    ctx = _parse_typespec("Int4**")
    
    # Verify type reference
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Int4"
    
    # Verify two pointer extensions
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 2
    assert extensions[0].pointerModifier() is not None
    assert extensions[0].pointerModifier().getText() == "*"
    assert extensions[1].pointerModifier() is not None
    assert extensions[1].pointerModifier().getText() == "*"
    
    TestLogger.success("Double pointer type parsed correctly")
    TestLogger.complete()


def test_parse_array_type() -> None:
    """Test parsing an array type."""
    TestLogger.header("CtdParser: Array Type")

    ctx = _parse_typespec("Unt1[8]")
    
    # Verify type reference
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "Unt1"
    
    # Verify array extension
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 1
    assert extensions[0].arrayModifier() is not None
    assert extensions[0].arrayModifier().getText() == "[8]"
    
    TestLogger.success("Array type parsed correctly")
    TestLogger.complete()


def test_parse_pointer_to_array() -> None:
    """Test parsing pointer to array type."""
    TestLogger.header("CtdParser: Pointer to Array")

    ctx = _parse_typespec("int[3]*")
    
    # Verify type reference
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "int"
    
    # Verify extensions: [3] then *
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 2
    assert extensions[0].arrayModifier() is not None
    assert extensions[0].arrayModifier().getText() == "[3]"
    assert extensions[1].pointerModifier() is not None
    assert extensions[1].pointerModifier().getText() == "*"
    
    TestLogger.success("Pointer to array parsed correctly")
    TestLogger.complete()


def test_parse_array_of_pointers() -> None:
    """Test parsing array of pointers type."""
    TestLogger.header("CtdParser: Array of Pointers")

    ctx = _parse_typespec("int*[4]")
    
    # Verify type reference
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "int"
    
    # Verify extensions: * then [4]
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 2
    assert extensions[0].pointerModifier() is not None
    assert extensions[0].pointerModifier().getText() == "*"
    assert extensions[1].arrayModifier() is not None
    assert extensions[1].arrayModifier().getText() == "[4]"
    
    TestLogger.success("Array of pointers parsed correctly")
    TestLogger.complete()


def test_parse_complex_multi_extensions() -> None:
    """Test parsing complex multi-extension types."""
    TestLogger.header("CtdParser: Complex Multi-Extensions")

    test_cases = [
        ("int[3]**", ["[3]", "*", "*"]),
        ("int[3]**[4]", ["[3]", "*", "*", "[4]"]),
        ("int[3]**[4]*", ["[3]", "*", "*", "[4]", "*"]),
        ("int[3]**[4]*[12]", ["[3]", "*", "*", "[4]", "*", "[12]"]),
    ]
    
    for type_str, expected_exts in test_cases:
        ctx = _parse_typespec(type_str)
        
        # Verify type reference
        assert ctx.typeReference() is not None
        assert ctx.typeReference().qualifiedName().getText() == "int"
        
        # Verify extensions match expected pattern
        extensions = ctx.typeReference().typeExtension()
        assert len(extensions) == len(expected_exts), \
            f"Expected {len(expected_exts)} extensions for '{type_str}', got {len(extensions)}"
        
        for i, expected_ext in enumerate(expected_exts):
            ext = extensions[i]
            ext_text = ext.getText()
            assert ext_text == expected_ext, \
                f"Extension {i} of '{type_str}': expected '{expected_ext}', got '{ext_text}'"
        
        TestLogger.success(f"Complex type '{type_str}' parsed correctly")
    
    TestLogger.complete()


def test_parse_qualified_type() -> None:
    """Test parsing a qualified type."""
    TestLogger.header("CtdParser: Qualified Type")

    ctx = _parse_typespec("std::lib::Int4")
    
    # Verify type reference with qualified name
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName() is not None
    assert ctx.typeReference().qualifiedName().getText() == "std::lib::Int4"
    
    TestLogger.success("Qualified type parsed correctly")
    TestLogger.complete()


def test_parse_qualified_type_with_extensions() -> None:
    """Test parsing qualified type with extensions."""
    TestLogger.header("CtdParser: Qualified Type with Extensions")

    ctx = _parse_typespec("std::lib::Int4*[5]")
    
    # Verify qualified name
    assert ctx.typeReference() is not None
    assert ctx.typeReference().qualifiedName().getText() == "std::lib::Int4"
    
    # Verify extensions
    extensions = ctx.typeReference().typeExtension()
    assert len(extensions) == 2
    assert extensions[0].pointerModifier() is not None
    assert extensions[1].arrayModifier() is not None
    assert extensions[1].arrayModifier().getText() == "[5]"
    
    TestLogger.success("Qualified type with extensions parsed correctly")
    TestLogger.complete()
