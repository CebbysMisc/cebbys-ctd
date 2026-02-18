"""Tests for CtdMetaParser.parse_function method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_function(ctd_string: str, namespace: str = "test") -> Meta.FunctionMeta:
    """Helper function to parse CTD function string into FunctionMeta.
    
    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object
    
    Args:
        ctd_string: CTD function declaration
        namespace: Namespace for the function (default: "test")
        
    Returns:
        FunctionMeta object
    """
    ctd_parser: Antlr4.CtdParser
    function_ctx: Antlr4.CtdGrammar.FunctionDeclarationContext
    function_meta: Meta.FunctionMeta
    
    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    function_ctx = ctd_parser.functionDeclaration(ctd_string)
    
    assert function_ctx is not None
    assert isinstance(function_ctx, Antlr4.CtdGrammar.FunctionDeclarationContext)
    TestLogger.success("ANTLR4 context created")
    
    # Step 2: Map ANTLR4 context to Meta object
    function_meta = Parser.CtdMetaParser.parse_function(namespace, function_ctx)
    
    assert function_meta is not None
    assert isinstance(function_meta, Meta.FunctionMeta)
    TestLogger.success("FunctionMeta object created")
    
    return function_meta


def test_parse_simple_function() -> None:
    """Test parsing a simple function."""
    function_meta: Meta.FunctionMeta

    TestLogger.header("MetaParser: Simple Function")

    # Parse and map CTD string to Meta object
    function_meta = _parse_function("Int4 getValue()")

    # Validate Meta object attributes
    assert function_meta.name == "getValue", f"Expected name 'getValue', got '{function_meta.name}'"
    assert str(function_meta.return_type) == "Int4", f"Expected return_type 'Int4', got '{function_meta.return_type}'"
    assert function_meta.namespace == "test", f"Expected namespace 'test', got '{function_meta.namespace}'"
    assert len(function_meta.decorators) == 0, f"Expected no decorators, got {len(function_meta.decorators)}"
    assert len(function_meta.parameters) == 0, f"Expected no parameters, got {len(function_meta.parameters)}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_function_with_parameters() -> None:
    """Test parsing a function with parameters."""
    function_meta: Meta.FunctionMeta

    TestLogger.header("MetaParser: Function with Parameters")

    # Parse and map CTD string to Meta object
    function_meta = _parse_function("Int4 add(Int4 a, Int4 b)")

    # Validate Meta object attributes
    assert function_meta.name == "add", f"Expected name 'add', got '{function_meta.name}'"
    assert str(function_meta.return_type) == "Int4", f"Expected return_type 'Int4', got '{function_meta.return_type}'"
    assert function_meta.namespace == "test", f"Expected namespace 'test', got '{function_meta.namespace}'"
    
    # Validate parameters
    assert len(function_meta.parameters) == 2, f"Expected 2 parameters, got {len(function_meta.parameters)}"
    assert function_meta.parameters[0].name == "a", f"Expected param 'a', got '{function_meta.parameters[0].name}'"
    assert str(function_meta.parameters[0].type_spec) == "Int4", f"Expected type 'Int4', got '{function_meta.parameters[0].type_spec}'"
    assert function_meta.parameters[1].name == "b", f"Expected param 'b', got '{function_meta.parameters[1].name}'"
    assert str(function_meta.parameters[1].type_spec) == "Int4", f"Expected type 'Int4', got '{function_meta.parameters[1].type_spec}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_function_with_decorator() -> None:
    """Test parsing a function with decorator."""
    function_meta: Meta.FunctionMeta

    TestLogger.header("MetaParser: Function with Decorator")

    # Parse and map CTD string to Meta object
    function_meta = _parse_function('''
        @WinApi
        Int4 CreateWindow(Unt4 style, Unt4 flags)
    ''')

    # Validate Meta object attributes including decorator
    assert function_meta.name == "CreateWindow", f"Expected name 'CreateWindow', got '{function_meta.name}'"
    assert str(function_meta.return_type) == "Int4", f"Expected return_type 'Int4', got '{function_meta.return_type}'"
    assert function_meta.namespace == "test", f"Expected namespace 'test', got '{function_meta.namespace}'"
    
    # Validate decorator
    assert len(function_meta.decorators) == 1, f"Expected 1 decorator, got {len(function_meta.decorators)}"
    assert function_meta.decorators[0].name == "WinApi", f"Expected decorator 'WinApi', got '{function_meta.decorators[0].name}'"
    
    # Validate parameters
    assert len(function_meta.parameters) == 2, f"Expected 2 parameters, got {len(function_meta.parameters)}"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_function_with_pointer_return() -> None:
    """Test parsing a function with pointer return type."""
    function_meta: Meta.FunctionMeta

    TestLogger.header("MetaParser: Function with Pointer Return")

    # Parse and map CTD string to Meta object
    function_meta = _parse_function("Void* allocate(Unt4 size)")

    # Validate Meta object attributes
    assert function_meta.name == "allocate", f"Expected name 'allocate', got '{function_meta.name}'"
    assert str(function_meta.return_type) == "Void*", f"Expected return_type 'Void*', got '{function_meta.return_type}'"
    assert function_meta.namespace == "test", f"Expected namespace 'test', got '{function_meta.namespace}'"
    
    # Validate parameters
    assert len(function_meta.parameters) == 1, f"Expected 1 parameter, got {len(function_meta.parameters)}"
    assert function_meta.parameters[0].name == "size", f"Expected param 'size', got '{function_meta.parameters[0].name}'"
    assert str(function_meta.parameters[0].type_spec) == "Unt4", f"Expected type 'Unt4', got '{function_meta.parameters[0].type_spec}'"
    
    TestLogger.success("All attributes validated")
    TestLogger.complete()
