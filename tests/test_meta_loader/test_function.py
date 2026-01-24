"""Stage 1: Test function meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_function_parsing() -> None:
    """Test that function declarations are parsed into FunctionMeta."""
    TestLogger.header("Stage 1: Function Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    # functions.ctd should have 1 function
    assert len(visitor.collection.functions) == 1
    TestLogger.success(f"Parsed {len(visitor.collection.functions)} functions")

    # Check CreateDeviceAndSwapChain function
    func = visitor.collection.functions[0]
    assert func.name == "CreateDeviceAndSwapChain"
    assert func.return_type == "ResultCode"
    assert len(func.parameters) == 8
    TestLogger.success(f"Function: {func.name}")
    TestLogger.info(f"Return type: {func.return_type}", indent=2)
    TestLogger.info(f"Parameters: {len(func.parameters)}", indent=2)

    TestLogger.complete("Function meta loading test passed")


def test_function_parameters() -> None:
    """Test function parameters are parsed correctly."""
    TestLogger.header("Stage 1: Function Parameters")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    func = visitor.collection.functions[0]

    # Check parameter names and types
    expected_params = [
        ('adapter', 'Adapter *'),
        ('driverType', 'DriverType'),
        ('software', 'ModuleHandle'),
        ('flags', 'CreateDeviceFlag'),
        ('featureLevels', 'FeatureLevel *'),
        ('featureLevelsCount', 'Unt4'),
        ('sdkVersion', 'Unt4'),
        ('outputDesc', 'Rational **'),
    ]

    for i, (name, type_spec) in enumerate(expected_params):
        param = func.parameters[i]
        assert param.name == name, f"Parameter {i} should be '{name}', got '{param.name}'"
        assert param.type_spec == type_spec, \
            f"Parameter {name} type should be '{type_spec}', got '{param.type_spec}'"
        TestLogger.info(f"{param.type_spec} {param.name}", indent=2)

    TestLogger.complete("Function parameters test passed")


def test_function_decorator() -> None:
    """Test function decorators are parsed correctly."""
    TestLogger.header("Stage 1: Function Decorators")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    func = visitor.collection.functions[0]

    # Should have @WinApi decorator
    assert len(func.decorators) == 1
    assert func.decorators[0].name == "WinApi"
    TestLogger.success(f"Function decorator: @{func.decorators[0].name}")

    TestLogger.complete("Function decorator test passed")


def test_parameter_decorator() -> None:
    """Test parameter decorators are parsed correctly."""
    TestLogger.header("Stage 1: Parameter Decorators")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    func = visitor.collection.functions[0]

    # First parameter (adapter) should have @Nullable decorator
    adapter_param = func.parameters[0]
    assert len(adapter_param.decorators) == 1
    assert adapter_param.decorators[0].name == "Nullable"
    TestLogger.success(f"Parameter decorator: @{adapter_param.decorators[0].name} {adapter_param.name}")

    # Other parameters should have no decorators
    for param in func.parameters[1:]:
        assert len(param.decorators) == 0

    TestLogger.complete("Parameter decorator test passed")


def test_function_namespace() -> None:
    """Test function namespace is captured correctly."""
    TestLogger.header("Stage 1: Function Namespace")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    func = visitor.collection.functions[0]
    assert func.namespace == "test::functions"
    TestLogger.success(f"Function namespace: {func.namespace}")

    TestLogger.complete("Function namespace test passed")
