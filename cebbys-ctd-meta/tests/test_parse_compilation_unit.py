"""Tests for CtdInterpreter.moduleDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.types.meta as TypesMeta
from conftest import TestLogger


def test_parse_empty_compilation_unit() -> None:
    """Test parsing an empty compilation unit."""
    TestLogger.header("CtdInterpreter: Empty Module Declaration")

    parser = Meta.CtdInterpreter()
    result = parser.moduleDeclaration("")

    assert result is not None
    assert isinstance(result, TypesMeta.ModuleMeta)
    TestLogger.success("Empty module declaration parsed successfully")
    TestLogger.complete()


def test_parse_compilation_unit_with_namespace() -> None:
    """Test parsing a compilation unit with a namespace."""
    TestLogger.header("CtdInterpreter: Module with Namespace")

    parser = Meta.CtdInterpreter()
    result = parser.moduleDeclaration('''
        namespace test::example {
            typedef int MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, TypesMeta.ModuleMeta)
    TestLogger.success("Module with namespace parsed")
    TestLogger.complete()


def test_parse_compilation_unit_with_import() -> None:
    """Test parsing a compilation unit with imports."""
    TestLogger.header("CtdInterpreter: Module with Import")

    parser = Meta.CtdInterpreter()
    result = parser.moduleDeclaration('''
        import "std-types"

        namespace test {
            typedef Int4 MyInt
        }
    ''')

    assert result is not None
    assert isinstance(result, TypesMeta.ModuleMeta)
    TestLogger.success("Module with import parsed")
    TestLogger.complete()
