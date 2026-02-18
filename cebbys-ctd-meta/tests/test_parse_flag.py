"""Tests for CtdMetaParser.parse_flag method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_flag(ctd_string: str, namespace: str = "test") -> Meta.FlagMeta:
    """Helper function to parse CTD flag string into FlagMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD flag declaration
        namespace: Namespace for the flag (default: "test")
        
    Returns:
        FlagMeta object
    """
    ctd_parser: Antlr4.CtdParser
    flag_ctx: Antlr4.CtdGrammar.FlagDeclarationContext
    flag_meta: Meta.FlagMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    flag_ctx = ctd_parser.flagDeclaration(ctd_string)
    
    assert flag_ctx is not None
    assert isinstance(flag_ctx, Antlr4.CtdGrammar.FlagDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    flag_meta = Parser.CtdMetaParser.parse_flag(namespace, flag_ctx)
    
    assert flag_meta is not None
    assert isinstance(flag_meta, Meta.FlagMeta)
    TestLogger.success("FlagMeta object created")
    
    return flag_meta


def test_parse_simple_flag() -> None:
    """Test parsing a simple flag."""
    flag_meta: Meta.FlagMeta

    TestLogger.header("MetaParser: Simple Flag")

    # Parse and map CTD string to Meta object
    flag_meta = _parse_flag('''
        flag Options : Unt4 {
            OPTION_A
            OPTION_B
            OPTION_C
        }
    ''')

    # Validate Meta object attributes
    assert flag_meta.name == "Options", f"Expected name 'Options', got '{flag_meta.name}'"
    assert str(flag_meta.base_type) == "Unt4", f"Expected base_type 'Unt4', got '{flag_meta.base_type}'"
    assert flag_meta.namespace == "test", f"Expected namespace 'test', got '{flag_meta.namespace}'"
    assert len(flag_meta.decorators) == 0, f"Expected no decorators, got {len(flag_meta.decorators)}"
    
    # Validate members
    assert len(flag_meta.members) == 3, f"Expected 3 members, got {len(flag_meta.members)}"
    assert flag_meta.members[0].name == "OPTION_A", f"Expected member 'OPTION_A', got '{flag_meta.members[0].name}'"
    assert flag_meta.members[1].name == "OPTION_B", f"Expected member 'OPTION_B', got '{flag_meta.members[1].name}'"
    assert flag_meta.members[2].name == "OPTION_C", f"Expected member 'OPTION_C', got '{flag_meta.members[2].name}'"
    
    # Values should be None (auto bit-shift)
    assert flag_meta.members[0].value is None, f"Expected OPTION_A value None, got {flag_meta.members[0].value}"
    assert flag_meta.members[1].value is None, f"Expected OPTION_B value None, got {flag_meta.members[1].value}"
    assert flag_meta.members[2].value is None, f"Expected OPTION_C value None, got {flag_meta.members[2].value}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_flag_with_offsets() -> None:
    """Test parsing a flag with manual offsets."""
    flag_meta: Meta.FlagMeta

    TestLogger.header("MetaParser: Flag with Offsets")

    # Parse and map CTD string to Meta object
    flag_meta = _parse_flag('''
        flag Permissions : Unt4 {
            READ
            WRITE
            EXECUTE = 0x10
            ADMIN
        }
    ''')

    # Validate Meta object attributes
    assert flag_meta.name == "Permissions", f"Expected name 'Permissions', got '{flag_meta.name}'"
    assert str(flag_meta.base_type) == "Unt4", f"Expected base_type 'Unt4', got '{flag_meta.base_type}'"
    assert flag_meta.namespace == "test", f"Expected namespace 'test', got '{flag_meta.namespace}'"
    
    # Validate members with explicit offset
    assert len(flag_meta.members) == 4, f"Expected 4 members, got {len(flag_meta.members)}"
    assert flag_meta.members[0].name == "READ", f"Expected member 'READ', got '{flag_meta.members[0].name}'"
    assert flag_meta.members[0].value is None, f"Expected READ value None, got {flag_meta.members[0].value}"
    
    assert flag_meta.members[1].name == "WRITE", f"Expected member 'WRITE', got '{flag_meta.members[1].name}'"
    assert flag_meta.members[1].value is None, f"Expected WRITE value None, got {flag_meta.members[1].value}"
    
    assert flag_meta.members[2].name == "EXECUTE", f"Expected member 'EXECUTE', got '{flag_meta.members[2].name}'"
    assert flag_meta.members[2].value == 0x10, f"Expected EXECUTE value 0x10, got {flag_meta.members[2].value}"
    
    assert flag_meta.members[3].name == "ADMIN", f"Expected member 'ADMIN', got '{flag_meta.members[3].name}'"
    assert flag_meta.members[3].value is None, f"Expected ADMIN value None, got {flag_meta.members[3].value}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()
