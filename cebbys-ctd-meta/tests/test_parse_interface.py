"""Tests for CtdMetaParser.parse_interface method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_interface(ctd_string: str, namespace: str = "test") -> Meta.InterfaceMeta:
    """Helper function to parse CTD interface string into InterfaceMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD interface declaration
        namespace: Namespace for the interface (default: "test")
        
    Returns:
        InterfaceMeta object
    """
    ctd_parser: Antlr4.CtdParser
    interface_ctx: Antlr4.CtdGrammar.InterfaceDeclarationContext
    interface_meta: Meta.InterfaceMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    interface_ctx = ctd_parser.interfaceDeclaration(ctd_string)
    
    assert interface_ctx is not None
    assert isinstance(interface_ctx, Antlr4.CtdGrammar.InterfaceDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    interface_meta = Parser.CtdMetaParser.parse_interface(namespace, interface_ctx)
    
    assert interface_meta is not None
    assert isinstance(interface_meta, Meta.InterfaceMeta)
    TestLogger.success("InterfaceMeta object created")
    
    return interface_meta


def test_parse_simple_interface() -> None:
    """Test parsing a simple interface."""
    interface_meta: Meta.InterfaceMeta

    TestLogger.header("MetaParser: Simple Interface")

    # Parse and map CTD string to Meta object
    interface_meta = _parse_interface('''
        interface IExample {
            Void doSomething()
            Int4 getValue()
        }
    ''')

    # Validate Meta object attributes
    assert interface_meta.name == "IExample", f"Expected name 'IExample', got '{interface_meta.name}'"
    assert interface_meta.base_type is None, f"Expected no base_type, got '{interface_meta.base_type}'"
    assert interface_meta.namespace == "test", f"Expected namespace 'test', got '{interface_meta.namespace}'"
    assert len(interface_meta.decorators) == 0, f"Expected no decorators, got {len(interface_meta.decorators)}"
    
    # Validate methods
    assert len(interface_meta.methods) == 2, f"Expected 2 methods, got {len(interface_meta.methods)}"
    assert interface_meta.methods[0].name == "doSomething", f"Expected method 'doSomething', got '{interface_meta.methods[0].name}'"
    assert str(interface_meta.methods[0].return_type) == "Void", f"Expected return type 'Void', got '{interface_meta.methods[0].return_type}'"
    
    assert interface_meta.methods[1].name == "getValue", f"Expected method 'getValue', got '{interface_meta.methods[1].name}'"
    assert str(interface_meta.methods[1].return_type) == "Int4", f"Expected return type 'Int4', got '{interface_meta.methods[1].return_type}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_interface_with_extension() -> None:
    """Test parsing an interface with base type."""
    interface_meta: Meta.InterfaceMeta

    TestLogger.header("MetaParser: Interface with Extension")

    # Parse and map CTD string to Meta object
    interface_meta = _parse_interface('''
        interface IExtended : IBase {
            Void extendedMethod()
        }
    ''')

    # Validate Meta object attributes
    assert interface_meta.name == "IExtended", f"Expected name 'IExtended', got '{interface_meta.name}'"
    assert str(interface_meta.base_type) == "IBase", f"Expected base_type 'IBase', got '{interface_meta.base_type}'"
    assert interface_meta.namespace == "test", f"Expected namespace 'test', got '{interface_meta.namespace}'"
    
    # Validate methods
    assert len(interface_meta.methods) == 1, f"Expected 1 method, got {len(interface_meta.methods)}"
    assert interface_meta.methods[0].name == "extendedMethod", f"Expected method 'extendedMethod', got '{interface_meta.methods[0].name}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_interface_with_parameters() -> None:
    """Test parsing an interface with method parameters."""
    interface_meta: Meta.InterfaceMeta

    TestLogger.header("MetaParser: Interface with Parameters")

    # Parse and map CTD string to Meta object
    interface_meta = _parse_interface('''
        interface ICalculator {
            Int4 add(Int4 a, Int4 b)
            Int4 multiply(Int4 x, Int4 y)
        }
    ''')

    # Validate Meta object attributes
    assert interface_meta.name == "ICalculator", f"Expected name 'ICalculator', got '{interface_meta.name}'"
    assert interface_meta.namespace == "test", f"Expected namespace 'test', got '{interface_meta.namespace}'"
    
    # Validate methods with parameters
    assert len(interface_meta.methods) == 2, f"Expected 2 methods, got {len(interface_meta.methods)}"
    
    # Validate first method
    assert interface_meta.methods[0].name == "add", f"Expected method 'add', got '{interface_meta.methods[0].name}'"
    assert len(interface_meta.methods[0].parameters) == 2, f"Expected 2 parameters, got {len(interface_meta.methods[0].parameters)}"
    assert interface_meta.methods[0].parameters[0].name == "a", f"Expected param 'a', got '{interface_meta.methods[0].parameters[0].name}'"
    assert str(interface_meta.methods[0].parameters[0].type_spec) == "Int4", f"Expected type 'Int4', got '{interface_meta.methods[0].parameters[0].type_spec}'"
    
    # Validate second method
    assert interface_meta.methods[1].name == "multiply", f"Expected method 'multiply', got '{interface_meta.methods[1].name}'"
    assert len(interface_meta.methods[1].parameters) == 2, f"Expected 2 parameters, got {len(interface_meta.methods[1].parameters)}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()
