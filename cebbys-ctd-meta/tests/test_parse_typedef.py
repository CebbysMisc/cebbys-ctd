"""Tests for MetaParser.parseTypedefDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_typedef() -> None:
    """Test parsing a simple typedef."""
    TestLogger.header("MetaParser: Simple Typedef")

    parser = Meta.MetaParser()
    result = parser.parseTypedefDeclaration("typedef int MyInt")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
    TestLogger.success("Simple typedef parsed")
    TestLogger.complete()


def test_parse_signed_typedef() -> None:
    """Test parsing a signed typedef."""
    TestLogger.header("MetaParser: Signed Typedef")

    parser = Meta.MetaParser()
    result = parser.parseTypedefDeclaration("typedef signed int Snt4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
    TestLogger.success("Signed typedef parsed")
    TestLogger.complete()


def test_parse_unsigned_typedef() -> None:
    """Test parsing an unsigned typedef."""
    TestLogger.header("MetaParser: Unsigned Typedef")

    parser = Meta.MetaParser()
    result = parser.parseTypedefDeclaration("typedef unsigned int Unt4")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.TypedefDeclarationContext)
    TestLogger.success("Unsigned typedef parsed")
    TestLogger.complete()
