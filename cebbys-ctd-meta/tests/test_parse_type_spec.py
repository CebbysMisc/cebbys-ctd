"""Tests for MetaParser.parseTypeSpec method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_type() -> None:
    """Test parsing a simple type."""
    TestLogger.header("MetaParser: Simple Type")

    parser = Meta.MetaParser()
    result = parser.parseTypeSpec("Int4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
    TestLogger.success("Simple type parsed")
    TestLogger.complete()


def test_parse_pointer_type() -> None:
    """Test parsing a pointer type."""
    TestLogger.header("MetaParser: Pointer Type")

    parser = Meta.MetaParser()
    result = parser.parseTypeSpec("Void*")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
    TestLogger.success("Pointer type parsed")
    TestLogger.complete()


def test_parse_double_pointer_type() -> None:
    """Test parsing a double pointer type."""
    TestLogger.header("MetaParser: Double Pointer Type")

    parser = Meta.MetaParser()
    result = parser.parseTypeSpec("Int4**")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
    TestLogger.success("Double pointer type parsed")
    TestLogger.complete()


def test_parse_array_type() -> None:
    """Test parsing an array type."""
    TestLogger.header("MetaParser: Array Type")

    parser = Meta.MetaParser()
    result = parser.parseTypeSpec("Unt1[8]")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
    TestLogger.success("Array type parsed")
    TestLogger.complete()


def test_parse_qualified_type() -> None:
    """Test parsing a qualified type."""
    TestLogger.header("MetaParser: Qualified Type")

    parser = Meta.MetaParser()
    result = parser.parseTypeSpec("std::lib::Int4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypeSpecContext)
    TestLogger.success("Qualified type parsed")
    TestLogger.complete()
