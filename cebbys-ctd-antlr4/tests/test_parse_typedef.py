"""Tests for CtdParser typedef declaration parsing.

Validates that CtdParser correctly parses typedef declarations into ANTLR4 contexts.
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def _parse_typedef(ctd_string: str) -> Antlr4.CtdGrammar.TypedefDeclarationContext:
    """Helper function to parse typedef declaration.
    
    Args:
        ctd_string: CTD typedef declaration string
        
    Returns:
        TypedefDeclarationContext from ANTLR4 parser
    """
    ctd_parser: Antlr4.CtdParser
    typedef_ctx: Antlr4.CtdGrammar.TypedefDeclarationContext
    
    # Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    typedef_ctx = ctd_parser.typedefDeclaration(ctd_string)
    
    assert typedef_ctx is not None
    assert isinstance(typedef_ctx, Antlr4.CtdGrammar.TypedefDeclarationContext)
    
    return typedef_ctx


def test_parse_simple_typedef() -> None:
    """Test parsing a simple typedef."""
    TestLogger.header("CtdParser: Simple Typedef")

    ctx = _parse_typedef("typedef int Int4")
    
    # Verify typedef keyword
    assert ctx.getText().startswith("typedef")
    
    # Verify type spec
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.typeReference() is not None
    assert type_spec.typeReference().qualifiedName().getText() == "int"
    
    # Verify target name
    assert ctx.IDENTIFIER() is not None
    assert ctx.IDENTIFIER().getText() == "Int4"
    
    TestLogger.success("Simple typedef parsed correctly")
    TestLogger.complete()


def test_parse_signed_typedef() -> None:
    """Test parsing a signed typedef."""
    TestLogger.header("CtdParser: Signed Typedef")

    ctx = _parse_typedef("typedef signed int Snt4")
    
    # Verify type spec
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.signModifier() is not None
    assert type_spec.signModifier().getText() == "signed"
    assert type_spec.typeReference() is not None
    assert type_spec.typeReference().qualifiedName().getText() == "int"
    
    # Verify target name
    assert ctx.IDENTIFIER().getText() == "Snt4"
    
    TestLogger.success("Signed typedef parsed correctly")
    TestLogger.complete()


def test_parse_unsigned_typedef() -> None:
    """Test parsing an unsigned typedef."""
    TestLogger.header("CtdParser: Unsigned Typedef")

    ctx = _parse_typedef("typedef unsigned int Unt4")
    
    # Verify type spec
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.signModifier() is not None
    assert type_spec.signModifier().getText() == "unsigned"
    assert type_spec.typeReference() is not None
    assert type_spec.typeReference().qualifiedName().getText() == "int"
    
    # Verify target name
    assert ctx.IDENTIFIER().getText() == "Unt4"
    
    TestLogger.success("Unsigned typedef parsed correctly")
    TestLogger.complete()


def test_parse_pointer_typedef() -> None:
    """Test parsing a pointer typedef."""
    TestLogger.header("CtdParser: Pointer Typedef")

    ctx = _parse_typedef("typedef Void* Any")
    
    # Verify type spec
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.typeReference() is not None
    assert type_spec.typeReference().qualifiedName().getText() == "Void"
    
    # Verify pointer extension
    extensions = type_spec.typeReference().typeExtension()
    assert len(extensions) == 1
    assert extensions[0].pointerModifier() is not None
    
    # Verify target name
    assert ctx.IDENTIFIER().getText() == "Any"
    
    TestLogger.success("Pointer typedef parsed correctly")
    TestLogger.complete()


def test_parse_typedef_with_decorator() -> None:
    """Test parsing typedef with decorator."""
    TestLogger.header("CtdParser: Typedef with Decorator")

    ctx = _parse_typedef("@Deprecated typedef int OldInt")
    
    # Verify decorator
    decorators = ctx.decorator()
    assert len(decorators) == 1
    assert decorators[0].IDENTIFIER().getText() == "Deprecated"
    
    # Verify type spec
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.typeReference().qualifiedName().getText() == "int"
    
    # Verify target name
    assert ctx.IDENTIFIER().getText() == "OldInt"
    
    TestLogger.success("Typedef with decorator parsed correctly")
    TestLogger.complete()


def test_parse_complex_typedef() -> None:
    """Test parsing typedef with complex type extensions."""
    TestLogger.header("CtdParser: Complex Typedef")

    ctx = _parse_typedef("typedef int[3]**[4]* ComplexType")
    
    # Verify type spec with extensions
    type_spec = ctx.typeSpec()
    assert type_spec is not None
    assert type_spec.typeReference().qualifiedName().getText() == "int"
    
    # Verify extensions
    extensions = type_spec.typeReference().typeExtension()
    assert len(extensions) == 5  # [3], *, *, [4], *
    
    # Verify target name
    assert ctx.IDENTIFIER().getText() == "ComplexType"
    
    TestLogger.success("Complex typedef parsed correctly")
    TestLogger.complete()
