"""Tests for CtdMetaParser.parse_typespec method.

Validates typespec parsing:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → typespec string (via Parser.CtdMetaParser)
3. Typespec string validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
from conftest import TestLogger


def _parse_typespec(ctd_string: str) -> str:
    """Helper function to parse CTD typespec string into typespec string.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to typespec string
    
    Args:
        ctd_string: CTD typespec
        
    Returns:
        Typespec string
    """
    ctd_parser: Antlr4.CtdParser
    typespec_ctx: Antlr4.CtdGrammar.TypeSpecContext
    typespec_str: str
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    typespec_ctx = ctd_parser.typeSpec(ctd_string)
    
    assert typespec_ctx is not None
    assert isinstance(typespec_ctx, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to typespec string
    typespec_str = str(Parser.CtdMetaParser.parse_typespec(typespec_ctx))
    
    assert typespec_str is not None
    assert isinstance(typespec_str, str)
    TestLogger.success("Typespec string created")
    
    return typespec_str


def test_parse_simple_type() -> None:
    """Test parsing a simple type."""
    typespec_str: str

    TestLogger.header("MetaParser: Simple Type")

    # Parse and map CTD string to typespec string
    typespec_str = _parse_typespec("Int4")

    # Validate typespec string
    assert typespec_str == "Int4", f"Expected 'Int4', got '{typespec_str}'"
    TestLogger.success("Typespec validated")

    TestLogger.complete()


def test_parse_pointer_type() -> None:
    """Test parsing a pointer type."""
    typespec_str: str

    TestLogger.header("MetaParser: Pointer Type")

    # Parse and map CTD string to typespec string
    typespec_str = _parse_typespec("Void*")

    # Validate typespec string (note: parser may add space)
    assert typespec_str in ["Void*", "Void *"], f"Expected 'Void*' or 'Void *', got '{typespec_str}'"
    TestLogger.success("Typespec validated")

    TestLogger.complete()


def test_parse_double_pointer_type() -> None:
    """Test parsing a double pointer type."""
    typespec_str: str

    TestLogger.header("MetaParser: Double Pointer Type")

    # Parse and map CTD string to typespec string
    typespec_str = _parse_typespec("Int4**")

    # Validate typespec string
    assert typespec_str in ["Int4**", "Int4 * *", "Int4 **"], f"Expected double pointer variant, got '{typespec_str}'"
    TestLogger.success("Typespec validated")

    TestLogger.complete()


def test_parse_array_type() -> None:
    """Test parsing an array type."""
    typespec_str: str

    TestLogger.header("MetaParser: Array Type")

    # Parse and map CTD string to typespec string
    typespec_str = _parse_typespec("Unt1[8]")

    # Validate typespec string (parser adds space before array brackets)
    assert str(typespec_str) == "Unt1[8]", f"Expected 'Unt1[8]', got '{typespec_str}'"
    TestLogger.success("Typespec validated")

    TestLogger.complete()


def test_parse_qualified_type() -> None:
    """Test parsing a qualified type."""
    typespec_str: str

    TestLogger.header("MetaParser: Qualified Type")

    # Parse and map CTD string to typespec string
    typespec_str = _parse_typespec("std::lib::Int4")

    # Validate typespec string
    assert typespec_str == "std::lib::Int4", f"Expected 'std::lib::Int4', got '{typespec_str}'"
    TestLogger.success("Typespec validated")

    TestLogger.complete()
