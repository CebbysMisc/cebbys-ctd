"""Tests for CtdContextParser.parseAliasDeclaration method."""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta as Meta
from conftest import TestLogger


def test_parse_simple_alias() -> None:
    """Test parsing a simple alias."""
    TestLogger.header("MetaParser: Simple Alias")

    parser = Antlr4.CtdParser()
    result = parser.aliasDeclaration("alias Guid InterfaceId")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.AliasDeclarationContext)
    TestLogger.success("Simple alias parsed")
    TestLogger.complete()


def test_parse_pointer_alias() -> None:
    """Test parsing an alias to a pointer type."""
    TestLogger.header("MetaParser: Pointer Alias")

    parser = Antlr4.CtdParser()
    result = parser.aliasDeclaration("alias IID* REFIID")

    assert result is not None
    assert isinstance(result, Antlr4.CtdGrammar.AliasDeclarationContext)
    TestLogger.success("Pointer alias parsed")
    TestLogger.complete()
