"""Tests for CtdContextParser.parseCompilationUnit method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_empty_compilation_unit() -> None:
    """Test parsing an empty compilation unit."""
    TestLogger.header("MetaParser: Empty Compilation Unit")

    parser = Meta.CtdContextParser()
    result = parser.parseCompilationUnit("")

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
    TestLogger.success("Empty compilation unit parsed successfully")
    TestLogger.complete()


def test_parse_compilation_unit_with_namespace() -> None:
    """Test parsing a compilation unit with a namespace."""
    TestLogger.header("MetaParser: Compilation Unit with Namespace")

    parser = Meta.CtdContextParser()
    result = parser.parseCompilationUnit('''
        namespace test::example {
            typedef int MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
    TestLogger.success("Compilation unit with namespace parsed")
    TestLogger.complete()


def test_parse_compilation_unit_with_import() -> None:
    """Test parsing a compilation unit with imports."""
    TestLogger.header("MetaParser: Compilation Unit with Import")

    parser = Meta.CtdContextParser()
    result = parser.parseCompilationUnit('''
        import "std-types"

        namespace test {
            typedef Int4 MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.CompilationUnitContext)
    TestLogger.success("Compilation unit with import parsed")
    TestLogger.complete()
