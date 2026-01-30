"""Tests for CtdContextParser.parseFlagDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_flag() -> None:
    """Test parsing a simple flag."""
    TestLogger.header("MetaParser: Simple Flag")

    parser = Meta.CtdContextParser()
    result = parser.parseFlagDeclaration('''
        flag Options : Unt4 {
            OPTION_A
            OPTION_B
            OPTION_C
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FlagDeclarationContext)
    TestLogger.success("Simple flag parsed")
    TestLogger.complete()


def test_parse_flag_with_offsets() -> None:
    """Test parsing a flag with manual offsets."""
    TestLogger.header("MetaParser: Flag with Offsets")

    parser = Meta.CtdContextParser()
    result = parser.parseFlagDeclaration('''
        flag Permissions : Unt4 {
            READ
            WRITE
            EXECUTE = 0x10
            ADMIN
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FlagDeclarationContext)
    TestLogger.success("Flag with offsets parsed")
    TestLogger.complete()
