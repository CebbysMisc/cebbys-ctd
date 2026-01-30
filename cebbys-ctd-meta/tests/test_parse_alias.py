"""Tests for MetaParser.parseAliasDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_alias() -> None:
    """Test parsing a simple alias."""
    TestLogger.header("MetaParser: Simple Alias")

    parser = Meta.MetaParser()
    result = parser.parseAliasDeclaration("alias Guid InterfaceId")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.AliasDeclarationContext)
    TestLogger.success("Simple alias parsed")
    TestLogger.complete()


def test_parse_pointer_alias() -> None:
    """Test parsing an alias to a pointer type."""
    TestLogger.header("MetaParser: Pointer Alias")

    parser = Meta.MetaParser()
    result = parser.parseAliasDeclaration("alias IID* REFIID")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.AliasDeclarationContext)
    TestLogger.success("Pointer alias parsed")
    TestLogger.complete()
