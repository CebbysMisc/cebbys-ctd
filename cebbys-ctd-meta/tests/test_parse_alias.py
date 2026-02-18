"""Tests for CtdMetaParser.parse_alias method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_alias(ctd_string: str, namespace: str = "test") -> Meta.AliasMeta:
    """Helper function to parse CTD alias string into AliasMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD alias declaration
        namespace: Namespace for the alias (default: "test")
        
    Returns:
        AliasMeta object
    """
    ctd_parser: Antlr4.CtdParser
    alias_ctx: Antlr4.CtdGrammar.AliasDeclarationContext
    alias_meta: Meta.AliasMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    alias_ctx = ctd_parser.aliasDeclaration(ctd_string)
    
    assert alias_ctx is not None
    assert isinstance(alias_ctx, Antlr4.CtdGrammar.AliasDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    alias_meta = Parser.CtdMetaParser.parse_alias(namespace, alias_ctx)
    
    assert alias_meta is not None
    assert isinstance(alias_meta, Meta.AliasMeta)
    TestLogger.success("AliasMeta object created")
    
    return alias_meta


def test_parse_simple_alias() -> None:
    """Test parsing a simple alias."""
    alias_meta: Meta.AliasMeta

    TestLogger.header("MetaParser: Simple Alias")

    # Parse and map CTD string to Meta object
    alias_meta = _parse_alias("alias Guid InterfaceId")

    # Validate Meta object attributes
    assert alias_meta.name == "InterfaceId", f"Expected name 'InterfaceId', got '{alias_meta.name}'"
    assert str(alias_meta.type_spec) == "Guid", f"Expected type_spec 'Guid', got '{alias_meta.type_spec}'"
    assert alias_meta.namespace == "test", f"Expected namespace 'test', got '{alias_meta.namespace}'"
    assert len(alias_meta.decorators) == 0, f"Expected no decorators, got {len(alias_meta.decorators)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()


def test_parse_pointer_alias() -> None:
    """Test parsing an alias to a pointer type."""
    alias_meta: Meta.AliasMeta

    TestLogger.header("MetaParser: Pointer Alias")

    # Parse and map CTD string to Meta object
    alias_meta = _parse_alias("alias IID* REFIID")

    # Validate Meta object attributes
    assert alias_meta.name == "REFIID", f"Expected name 'REFIID', got '{alias_meta.name}'"
    assert str(alias_meta.type_spec) == "IID*", f"Expected type_spec 'IID*', got '{alias_meta.type_spec}'"
    assert alias_meta.namespace == "test", f"Expected namespace 'test', got '{alias_meta.namespace}'"
    assert len(alias_meta.decorators) == 0, f"Expected no decorators, got {len(alias_meta.decorators)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()


def test_parse_alias_with_decorator() -> None:
    """Test parsing an alias with decorators."""
    alias_meta: Meta.AliasMeta

    TestLogger.header("MetaParser: Alias with Decorator")

    # Parse and map CTD string to Meta object
    alias_meta = _parse_alias("@deprecated alias OldGuid NewGuid")

    # Validate Meta object attributes including decorators
    assert alias_meta.name == "NewGuid", f"Expected name 'NewGuid', got '{alias_meta.name}'"
    assert str(alias_meta.type_spec) == "OldGuid", f"Expected type_spec 'OldGuid', got '{alias_meta.type_spec}'"
    assert alias_meta.namespace == "test", f"Expected namespace 'test', got '{alias_meta.namespace}'"

    assert len(alias_meta.decorators) == 1, f"Expected 1 decorator, got {len(alias_meta.decorators)}"
    assert alias_meta.decorators[0].name == "deprecated", f"Expected decorator 'deprecated', got '{alias_meta.decorators[0].name}'"
    TestLogger.success("All attributes validated")

    TestLogger.complete()
