"""Stage 1: Test interface meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_interface_parsing() -> None:
    """Test that interface declarations are parsed into InterfaceMeta."""
    TestLogger.header("Stage 1: Interface Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/unknown.ctd'))

    # unknown.ctd should have 1 interface
    assert len(visitor.collection.interfaces) == 1
    TestLogger.success(f"Parsed {len(visitor.collection.interfaces)} interfaces")

    # Check IUnknown interface
    iunknown = visitor.collection.interfaces[0]
    assert iunknown.name == "IUnknown"
    assert len(iunknown.methods) == 3
    TestLogger.success(f"Interface: {iunknown.name} with {len(iunknown.methods)} methods")

    # Check method names
    expected_methods = ['QueryInterface', 'AddRef', 'Release']
    for i, method in enumerate(iunknown.methods):
        assert method.name == expected_methods[i]
        TestLogger.info(f"Method: {method.name}", indent=2)

    TestLogger.complete("Interface meta loading test passed")


def test_interface_method_parameters() -> None:
    """Test interface method parameters are parsed correctly."""
    TestLogger.header("Stage 1: Interface Method Parameters")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/unknown.ctd'))

    iunknown = visitor.collection.interfaces[0]

    # QueryInterface has 2 parameters
    query_interface = iunknown.methods[0]
    assert len(query_interface.parameters) == 2
    TestLogger.success(f"QueryInterface has {len(query_interface.parameters)} parameters")

    # Check parameter details
    assert query_interface.parameters[0].name == "interfaceId"
    assert query_interface.parameters[0].type_spec == "REFIID"
    assert query_interface.parameters[1].name == "vtable"
    assert query_interface.parameters[1].type_spec == "Any *"

    for param in query_interface.parameters:
        TestLogger.info(f"{param.type_spec} {param.name}", indent=2)

    # AddRef and Release have no parameters
    assert len(iunknown.methods[1].parameters) == 0
    assert len(iunknown.methods[2].parameters) == 0
    TestLogger.success("AddRef and Release have no parameters")

    TestLogger.complete("Interface method parameters test passed")


def test_interface_method_decorators() -> None:
    """Test interface method decorators are parsed correctly."""
    TestLogger.header("Stage 1: Interface Method Decorators")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/unknown.ctd'))

    iunknown = visitor.collection.interfaces[0]
    query_interface = iunknown.methods[0]

    # Interface methods in unknown.ctd don't have decorators
    assert len(query_interface.decorators) == 0
    TestLogger.success("QueryInterface has no decorators (as defined in CTD)")

    TestLogger.complete("Interface method decorators test passed")


def test_interface_method_return_type() -> None:
    """Test interface method return types are parsed correctly."""
    TestLogger.header("Stage 1: Interface Method Return Types")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/unknown.ctd'))

    iunknown = visitor.collection.interfaces[0]

    # QueryInterface returns HRESULT (from wincrypt.ctd)
    assert iunknown.methods[0].return_type == "HRESULT"
    TestLogger.success(f"QueryInterface returns: {iunknown.methods[0].return_type}")

    # AddRef and Release return Unt4
    assert iunknown.methods[1].return_type == "Unt4"
    assert iunknown.methods[2].return_type == "Unt4"
    TestLogger.success(f"AddRef returns: {iunknown.methods[1].return_type}")
    TestLogger.success(f"Release returns: {iunknown.methods[2].return_type}")

    TestLogger.complete("Interface method return types test passed")
