"""Tests for MetaParser.parseFunctionDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_function() -> None:
    """Test parsing a simple function."""
    TestLogger.header("MetaParser: Simple Function")

    parser = Meta.MetaParser()
    result = parser.parseFunctionDeclaration("Int4 getValue()")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
    TestLogger.success("Simple function parsed")
    TestLogger.complete()


def test_parse_function_with_parameters() -> None:
    """Test parsing a function with parameters."""
    TestLogger.header("MetaParser: Function with Parameters")

    parser = Meta.MetaParser()
    result = parser.parseFunctionDeclaration("Int4 add(Int4 a, Int4 b)")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
    TestLogger.success("Function with parameters parsed")
    TestLogger.complete()


def test_parse_function_with_decorator() -> None:
    """Test parsing a function with decorator."""
    TestLogger.header("MetaParser: Function with Decorator")

    parser = Meta.MetaParser()
    result = parser.parseFunctionDeclaration('''
        @WinApi
        Int4 CreateWindow(Unt4 style, Unt4 flags)
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
    TestLogger.success("Function with decorator parsed")
    TestLogger.complete()


def test_parse_function_with_pointer_return() -> None:
    """Test parsing a function with pointer return type."""
    TestLogger.header("MetaParser: Function with Pointer Return")

    parser = Meta.MetaParser()
    result = parser.parseFunctionDeclaration("Void* allocate(Unt4 size)")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.FunctionDeclarationContext)
    TestLogger.success("Function with pointer return parsed")
    TestLogger.complete()
