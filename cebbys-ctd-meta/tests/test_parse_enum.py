"""Tests for CtdContextParser.parseEnumDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_enum() -> None:
    """Test parsing a simple enum."""
    TestLogger.header("MetaParser: Simple Enum")

    parser = Meta.CtdInterpreter()
    result = parser.enumDeclaration('''
        enum Color : Int4 {
            RED
            GREEN
            BLUE
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.EnumDeclarationContext)
    TestLogger.success("Simple enum parsed")
    TestLogger.complete()


def test_parse_enum_with_values() -> None:
    """Test parsing an enum with explicit values."""
    TestLogger.header("MetaParser: Enum with Values")

    parser = Meta.CtdInterpreter()
    result = parser.enumDeclaration('''
        enum Status : Unt4 {
            OK = 0
            ERROR = 1
            PENDING = 0x10
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.EnumDeclarationContext)
    TestLogger.success("Enum with values parsed")
    TestLogger.complete()
