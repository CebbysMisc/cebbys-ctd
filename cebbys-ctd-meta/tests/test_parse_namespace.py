"""Tests for MetaParser.parseNamespaceDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_namespace() -> None:
    """Test parsing a simple namespace."""
    TestLogger.header("MetaParser: Simple Namespace")

    parser = Meta.MetaParser()
    result = parser.parseNamespaceDeclaration('''
        namespace example {
            typedef int MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.NamespaceDeclarationContext)
    TestLogger.success("Simple namespace parsed")
    TestLogger.complete()


def test_parse_nested_namespace() -> None:
    """Test parsing a nested namespace."""
    TestLogger.header("MetaParser: Nested Namespace")

    parser = Meta.MetaParser()
    result = parser.parseNamespaceDeclaration('''
        namespace foo::bar::baz {
            typedef int MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.NamespaceDeclarationContext)
    TestLogger.success("Nested namespace parsed")
    TestLogger.complete()
