"""Tests for CtdContextParser.parseInterfaceDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_interface() -> None:
    """Test parsing a simple interface."""
    TestLogger.header("MetaParser: Simple Interface")

    parser = Meta.CtdInterpreter()
    result = parser.interfaceDeclaration('''
        interface IExample {
            Void doSomething()
            Int4 getValue()
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
    TestLogger.success("Simple interface parsed")
    TestLogger.complete()


def test_parse_interface_with_extension() -> None:
    """Test parsing an interface with base type."""
    TestLogger.header("MetaParser: Interface with Extension")

    parser = Meta.CtdInterpreter()
    result = parser.interfaceDeclaration('''
        interface IExtended : IBase {
            Void extendedMethod()
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
    TestLogger.success("Interface with extension parsed")
    TestLogger.complete()


def test_parse_interface_with_parameters() -> None:
    """Test parsing an interface with method parameters."""
    TestLogger.header("MetaParser: Interface with Parameters")

    parser = Meta.CtdInterpreter()
    result = parser.interfaceDeclaration('''
        interface ICalculator {
            Int4 add(Int4 a, Int4 b)
            Int4 multiply(Int4 x, Int4 y)
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.InterfaceDeclarationContext)
    TestLogger.success("Interface with parameters parsed")
    TestLogger.complete()
