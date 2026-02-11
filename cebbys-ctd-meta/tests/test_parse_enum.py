"""Tests for CtdMetaParser.parse_enum method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_enum(ctd_string: str, namespace: str = "test") -> Meta.EnumMeta:
    """Helper function to parse CTD enum string into EnumMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD enum declaration
        namespace: Namespace for the enum (default: "test")
        
    Returns:
        EnumMeta object
    """
    ctd_parser: Antlr4.CtdParser
    enum_ctx: Antlr4.CtdGrammar.EnumDeclarationContext
    enum_meta: Meta.EnumMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    enum_ctx = ctd_parser.enumDeclaration(ctd_string)
    
    assert enum_ctx is not None
    assert isinstance(enum_ctx, Antlr4.CtdGrammar.EnumDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    enum_meta = Parser.CtdMetaParser.parse_enum(namespace, enum_ctx)
    
    assert enum_meta is not None
    assert isinstance(enum_meta, Meta.EnumMeta)
    TestLogger.success("EnumMeta object created")
    
    return enum_meta


def test_parse_simple_enum() -> None:
    """Test parsing a simple enum."""
    enum_meta: Meta.EnumMeta

    TestLogger.header("MetaParser: Simple Enum")

    # Parse and map CTD string to Meta object
    enum_meta = _parse_enum('''
        enum Color : Int4 {
            RED
            GREEN
            BLUE
        }
    ''')

    # Validate Meta object attributes
    assert enum_meta.name == "Color", f"Expected name 'Color', got '{enum_meta.name}'"
    assert enum_meta.base_type == "Int4", f"Expected base_type 'Int4', got '{enum_meta.base_type}'"
    assert enum_meta.namespace == "test", f"Expected namespace 'test', got '{enum_meta.namespace}'"
    assert len(enum_meta.decorators) == 0, f"Expected no decorators, got {len(enum_meta.decorators)}"
    
    # Validate members
    assert len(enum_meta.members) == 3, f"Expected 3 members, got {len(enum_meta.members)}"
    assert enum_meta.members[0].name == "RED", f"Expected member 'RED', got '{enum_meta.members[0].name}'"
    assert enum_meta.members[1].name == "GREEN", f"Expected member 'GREEN', got '{enum_meta.members[1].name}'"
    assert enum_meta.members[2].name == "BLUE", f"Expected member 'BLUE', got '{enum_meta.members[2].name}'"
    
    # Values should be None (auto-increment)
    assert enum_meta.members[0].value is None, f"Expected RED value None, got {enum_meta.members[0].value}"
    assert enum_meta.members[1].value is None, f"Expected GREEN value None, got {enum_meta.members[1].value}"
    assert enum_meta.members[2].value is None, f"Expected BLUE value None, got {enum_meta.members[2].value}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_enum_with_values() -> None:
    """Test parsing an enum with explicit values."""
    enum_meta: Meta.EnumMeta

    TestLogger.header("MetaParser: Enum with Values")

    # Parse and map CTD string to Meta object
    enum_meta = _parse_enum('''
        enum Status : Unt4 {
            OK = 0
            ERROR = 1
            PENDING = 0x10
        }
    ''')

    # Validate Meta object attributes
    assert enum_meta.name == "Status", f"Expected name 'Status', got '{enum_meta.name}'"
    assert enum_meta.base_type == "Unt4", f"Expected base_type 'Unt4', got '{enum_meta.base_type}'"
    assert enum_meta.namespace == "test", f"Expected namespace 'test', got '{enum_meta.namespace}'"
    
    # Validate members with explicit values
    assert len(enum_meta.members) == 3, f"Expected 3 members, got {len(enum_meta.members)}"
    assert enum_meta.members[0].name == "OK", f"Expected member 'OK', got '{enum_meta.members[0].name}'"
    assert enum_meta.members[0].value == 0, f"Expected OK value 0, got {enum_meta.members[0].value}"
    
    assert enum_meta.members[1].name == "ERROR", f"Expected member 'ERROR', got '{enum_meta.members[1].name}'"
    assert enum_meta.members[1].value == 1, f"Expected ERROR value 1, got {enum_meta.members[1].value}"
    
    assert enum_meta.members[2].name == "PENDING", f"Expected member 'PENDING', got '{enum_meta.members[2].name}'"
    assert enum_meta.members[2].value == 0x10, f"Expected PENDING value 0x10, got {enum_meta.members[2].value}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()
