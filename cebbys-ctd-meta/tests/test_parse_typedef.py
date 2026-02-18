"""Tests for CtdMetaParser.parse_typedef method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_typedef(ctd_string: str, namespace: str = "test") -> Meta.TypedefMeta:
    """Helper function to parse CTD typedef string into TypedefMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD typedef declaration
        namespace: Namespace for the typedef (default: "test")
        
    Returns:
        TypedefMeta object
    """
    ctd_parser: Antlr4.CtdParser
    typedef_ctx: Antlr4.CtdGrammar.TypedefDeclarationContext
    typedef_meta: Meta.TypedefMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    typedef_ctx = ctd_parser.typedefDeclaration(ctd_string)
    
    assert typedef_ctx is not None
    assert isinstance(typedef_ctx, Antlr4.CtdGrammar.TypedefDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    typedef_meta = Parser.CtdMetaParser.parse_typedef(namespace, typedef_ctx)
    
    assert typedef_meta is not None
    assert isinstance(typedef_meta, Meta.TypedefMeta)
    TestLogger.success("TypedefMeta object created")
    
    return typedef_meta


def test_parse_simple_typedef() -> None:
    """Test parsing a simple typedef."""
    typedef_meta: Meta.TypedefMeta

    TestLogger.header("MetaParser: Simple Typedef")

    # Parse and map CTD string to Meta object
    typedef_meta = _parse_typedef("typedef int MyInt")

    # Validate Meta object attributes
    assert typedef_meta.name == "MyInt", f"Expected name 'MyInt', got '{typedef_meta.name}'"
    assert str(typedef_meta.type_spec) == "int", f"Expected type_spec 'int', got '{typedef_meta.type_spec}'"
    assert typedef_meta.namespace == "test", f"Expected namespace 'test', got '{typedef_meta.namespace}'"
    assert len(typedef_meta.decorators) == 0, f"Expected no decorators, got {len(typedef_meta.decorators)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()


def test_parse_signed_typedef() -> None:
    """Test parsing a signed typedef."""
    typedef_meta: Meta.TypedefMeta

    TestLogger.header("MetaParser: Signed Typedef")

    # Parse and map CTD string to Meta object
    typedef_meta = _parse_typedef("typedef signed int Snt4")

    # Validate Meta object attributes
    assert typedef_meta.name == "Snt4", f"Expected name 'Snt4', got '{typedef_meta.name}'"
    assert str(typedef_meta.type_spec) == "signed int", f"Expected type_spec 'signed int', got '{typedef_meta.type_spec}'"
    assert typedef_meta.namespace == "test", f"Expected namespace 'test', got '{typedef_meta.namespace}'"
    assert len(typedef_meta.decorators) == 0, f"Expected no decorators, got {len(typedef_meta.decorators)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()


def test_parse_unsigned_typedef() -> None:
    """Test parsing an unsigned typedef."""
    typedef_meta: Meta.TypedefMeta

    TestLogger.header("MetaParser: Unsigned Typedef")

    # Parse and map CTD string to Meta object
    typedef_meta = _parse_typedef("typedef unsigned int Unt4")

    # Validate Meta object attributes
    assert typedef_meta.name == "Unt4", f"Expected name 'Unt4', got '{typedef_meta.name}'"
    assert str(typedef_meta.type_spec) == "unsigned int", f"Expected type_spec 'unsigned int', got '{typedef_meta.type_spec}'"
    assert typedef_meta.namespace == "test", f"Expected namespace 'test', got '{typedef_meta.namespace}'"
    assert len(typedef_meta.decorators) == 0, f"Expected no decorators, got {len(typedef_meta.decorators)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()


def test_parse_typedef_with_decorator() -> None:
    """Test parsing a typedef with decorators."""
    typedef_meta: Meta.TypedefMeta

    TestLogger.header("MetaParser: Typedef with Decorator")

    # Parse and map CTD string to Meta object
    typedef_meta = _parse_typedef("@platform(\"win32\") typedef long Long")

    # Validate Meta object attributes including decorators
    assert typedef_meta.name == "Long", f"Expected name 'Long', got '{typedef_meta.name}'"
    assert str(typedef_meta.type_spec) == "long", f"Expected type_spec 'long', got '{typedef_meta.type_spec}'"
    assert typedef_meta.namespace == "test", f"Expected namespace 'test', got '{typedef_meta.namespace}'"
    
    assert len(typedef_meta.decorators) == 1, f"Expected 1 decorator, got {len(typedef_meta.decorators)}"
    assert typedef_meta.decorators[0].name == "platform", f"Expected decorator 'platform', got '{typedef_meta.decorators[0].name}'"
    assert len(typedef_meta.decorators[0].arguments) == 1, f"Expected 1 argument, got {len(typedef_meta.decorators[0].arguments)}"
    TestLogger.success("All attributes validated")

    TestLogger.complete()
