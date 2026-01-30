"""Tests for CtdContextParser.parseTypeSpec method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_type() -> None:
    """Test parsing a simple type."""
    TestLogger.header("MetaParser: Simple Type")

    parser = Antlr4.CtdParser()
    result = parser.typeSpec("Int4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("Simple type parsed")
    TestLogger.complete()


def test_parse_pointer_type() -> None:
    """Test parsing a pointer type."""
    TestLogger.header("MetaParser: Pointer Type")

    parser = Antlr4.CtdParser()
    result = parser.typeSpec("Void*")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("Pointer type parsed")
    TestLogger.complete()


def test_parse_double_pointer_type() -> None:
    """Test parsing a double pointer type."""
    TestLogger.header("MetaParser: Double Pointer Type")

    parser = Antlr4.CtdParser()
    result = parser.typeSpec("Int4**")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("Double pointer type parsed")
    TestLogger.complete()


def test_parse_array_type() -> None:
    """Test parsing an array type."""
    TestLogger.header("MetaParser: Array Type")

    parser = Antlr4.CtdParser()
    result = parser.typeSpec("Unt1[8]")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("Array type parsed")
    TestLogger.complete()


def test_parse_qualified_type() -> None:
    """Test parsing a qualified type."""
    TestLogger.header("MetaParser: Qualified Type")

    parser = Antlr4.CtdParser()
    result = parser.typeSpec("std::lib::Int4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.TypeSpecContext)
    TestLogger.success("Qualified type parsed")
    TestLogger.complete()
