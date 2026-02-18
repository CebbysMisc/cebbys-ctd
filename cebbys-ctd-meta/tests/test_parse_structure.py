"""Tests for CtdMetaParser.parse_structure method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_structure(ctd_string: str, namespace: str = "test") -> Meta.StructureMeta:
    """Helper function to parse CTD structure string into StructureMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD structure declaration
        namespace: Namespace for the structure (default: "test")
        
    Returns:
        StructureMeta object
    """
    ctd_parser: Antlr4.CtdParser
    structure_ctx: Antlr4.CtdGrammar.StructureDeclarationContext
    structure_meta: Meta.StructureMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    structure_ctx = ctd_parser.structureDeclaration(ctd_string)
    
    assert structure_ctx is not None
    assert isinstance(structure_ctx, Antlr4.CtdGrammar.StructureDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    structure_meta = Parser.CtdMetaParser.parse_structure(namespace, structure_ctx)
    
    assert structure_meta is not None
    assert isinstance(structure_meta, Meta.StructureMeta)
    TestLogger.success("StructureMeta object created")
    
    return structure_meta


def test_parse_simple_structure() -> None:
    """Test parsing a simple structure."""
    structure_meta: Meta.StructureMeta

    TestLogger.header("MetaParser: Simple Structure")

    # Parse and map CTD string to Meta object
    structure_meta = _parse_structure('''
        structure Point {
            Int4 x
            Int4 y
        }
    ''')

    # Validate Meta object attributes
    assert structure_meta.name == "Point", f"Expected name 'Point', got '{structure_meta.name}'"
    assert structure_meta.base_type is None, f"Expected no base_type, got '{structure_meta.base_type}'"
    assert structure_meta.namespace == "test", f"Expected namespace 'test', got '{structure_meta.namespace}'"
    assert len(structure_meta.decorators) == 0, f"Expected no decorators, got {len(structure_meta.decorators)}"
    
    # Validate members
    assert len(structure_meta.members) == 2, f"Expected 2 members, got {len(structure_meta.members)}"
    assert structure_meta.members[0].name == "x", f"Expected member 'x', got '{structure_meta.members[0].name}'"
    assert str(structure_meta.members[0].type_spec) == "Int4", f"Expected type_spec 'Int4', got '{structure_meta.members[0].type_spec}'"
    assert structure_meta.members[1].name == "y", f"Expected member 'y', got '{structure_meta.members[1].name}'"
    assert str(structure_meta.members[1].type_spec) == "Int4", f"Expected type_spec 'Int4', got '{structure_meta.members[1].type_spec}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_structure_with_extension() -> None:
    """Test parsing a structure with base type."""
    structure_meta: Meta.StructureMeta

    TestLogger.header("MetaParser: Structure with Extension")

    # Parse and map CTD string to Meta object
    structure_meta = _parse_structure('''
        structure Point3D : Point {
            Int4 z
        }
    ''')

    # Validate Meta object attributes
    assert structure_meta.name == "Point3D", f"Expected name 'Point3D', got '{structure_meta.name}'"
    assert str(structure_meta.base_type) == "Point", f"Expected base_type 'Point', got '{structure_meta.base_type}'"
    assert structure_meta.namespace == "test", f"Expected namespace 'test', got '{structure_meta.namespace}'"
    
    # Validate members
    assert len(structure_meta.members) == 1, f"Expected 1 member, got {len(structure_meta.members)}"
    assert structure_meta.members[0].name == "z", f"Expected member 'z', got '{structure_meta.members[0].name}'"
    assert str(structure_meta.members[0].type_spec) == "Int4", f"Expected type_spec 'Int4', got '{structure_meta.members[0].type_spec}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_structure_with_pointer_member() -> None:
    """Test parsing a structure with pointer member."""
    structure_meta: Meta.StructureMeta

    TestLogger.header("MetaParser: Structure with Pointer")

    # Parse and map CTD string to Meta object
    structure_meta = _parse_structure('''
        structure Node {
            Int4 value
            Node* next
        }
    ''')

    # Validate Meta object attributes
    assert structure_meta.name == "Node", f"Expected name 'Node', got '{structure_meta.name}'"
    assert structure_meta.namespace == "test", f"Expected namespace 'test', got '{structure_meta.namespace}'"
    
    # Validate members including pointer
    assert len(structure_meta.members) == 2, f"Expected 2 members, got {len(structure_meta.members)}"
    assert structure_meta.members[0].name == "value", f"Expected member 'value', got '{structure_meta.members[0].name}'"
    assert str(structure_meta.members[0].type_spec) == "Int4", f"Expected type_spec 'Int4', got '{structure_meta.members[0].type_spec}'"
    
    assert structure_meta.members[1].name == "next", f"Expected member 'next', got '{structure_meta.members[1].name}'"
    assert str(structure_meta.members[1].type_spec) == "Node*", f"Expected type_spec 'Node*', got '{structure_meta.members[1].type_spec}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_structure_with_array_member() -> None:
    """Test parsing a structure with array member."""
    structure_meta: Meta.StructureMeta

    TestLogger.header("MetaParser: Structure with Array")

    # Parse and map CTD string to Meta object
    structure_meta = _parse_structure('''
        structure Buffer {
            Unt4 size
            Unt1[256] data
        }
    ''')

    # Validate Meta object attributes
    assert structure_meta.name == "Buffer", f"Expected name 'Buffer', got '{structure_meta.name}'"
    assert structure_meta.namespace == "test", f"Expected namespace 'test', got '{structure_meta.namespace}'"
    
    # Validate members including array
    assert len(structure_meta.members) == 2, f"Expected 2 members, got {len(structure_meta.members)}"
    assert structure_meta.members[0].name == "size", f"Expected member 'size', got '{structure_meta.members[0].name}'"
    assert str(structure_meta.members[0].type_spec) == "Unt4", f"Expected type_spec 'Unt4', got '{structure_meta.members[0].type_spec}'"
    
    assert structure_meta.members[1].name == "data", f"Expected member 'data', got '{structure_meta.members[1].name}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()
