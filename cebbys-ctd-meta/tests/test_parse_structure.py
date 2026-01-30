"""Tests for MetaParser.parseStructureDeclaration method."""
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def test_parse_simple_structure() -> None:
    """Test parsing a simple structure."""
    TestLogger.header("MetaParser: Simple Structure")

    parser = Meta.MetaParser()
    result = parser.parseStructureDeclaration('''
        structure Point {
            Int4 x
            Int4 y
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
    TestLogger.success("Simple structure parsed")
    TestLogger.complete()


def test_parse_structure_with_extension() -> None:
    """Test parsing a structure with base type."""
    TestLogger.header("MetaParser: Structure with Extension")

    parser = Meta.MetaParser()
    result = parser.parseStructureDeclaration('''
        structure Point3D : Point {
            Int4 z
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
    TestLogger.success("Structure with extension parsed")
    TestLogger.complete()


def test_parse_structure_with_pointer_member() -> None:
    """Test parsing a structure with pointer member."""
    TestLogger.header("MetaParser: Structure with Pointer")

    parser = Meta.MetaParser()
    result = parser.parseStructureDeclaration('''
        structure Node {
            Int4 value
            Node* next
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
    TestLogger.success("Structure with pointer parsed")
    TestLogger.complete()


def test_parse_structure_with_array_member() -> None:
    """Test parsing a structure with array member."""
    TestLogger.header("MetaParser: Structure with Array")

    parser = Meta.MetaParser()
    result = parser.parseStructureDeclaration('''
        structure Buffer {
            Unt4 size
            Unt1[256] data
        }
    ''')

    assert result is not None
    assert isinstance(result, Antlr4.CtdParser.StructureDeclarationContext)
    TestLogger.success("Structure with array parsed")
    TestLogger.complete()
