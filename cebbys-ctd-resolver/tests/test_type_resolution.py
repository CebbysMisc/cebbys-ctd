"""Stage 3: Test type reference resolution.

Tests that type references are correctly resolved to singleton instances.
"""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.types.define as Define
from test_utils import TestLogger
from conftest import get_resource_path

# Test CTD files to load (order matters for dependencies)
TEST_CTD_FILES = [
    get_resource_path('resources/test/ctd/std-types.ctd'),
    get_resource_path('resources/test/ctd/enums.ctd'),
    get_resource_path('resources/test/ctd/flags.ctd'),
    get_resource_path('resources/test/ctd/structures.ctd'),
    get_resource_path('resources/test/ctd/interfaces.ctd'),
    get_resource_path('resources/test/ctd/aliases.ctd'),
    get_resource_path('resources/test/ctd/functions.ctd'),
]


def test_typedef_reference_resolution() -> None:
    """Test that typedef type references are resolved to singletons."""
    TestLogger.header("Stage 3: Typedef Reference Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get Void and Any typedefs
    void_typedef = collection.typedefs.get('std::lib::Void')
    any_typedef = collection.typedefs.get('std::lib::Any')

    assert void_typedef is not None
    assert any_typedef is not None

    # Any references Void*
    assert any_typedef.type_spec.is_pointer
    base = any_typedef.type_spec.base_type
    assert isinstance(base, Define.TypeReference)

    # The target should be the SAME instance as void_typedef
    assert base.target is void_typedef
    TestLogger.success("Any.type_spec.base_type.target is Void typedef")
    TestLogger.info(f"Void id: {id(void_typedef)}", indent=2)
    TestLogger.info(f"Target id: {id(base.target)}", indent=2)

    TestLogger.complete("Typedef reference resolution test passed")


def test_enum_base_type_resolution() -> None:
    """Test that enum base types are resolved correctly."""
    TestLogger.header("Stage 3: Enum Base Type Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get Null enum and Int4 typedef
    null_enum = collection.enums.get('std::lib::Null')
    int4_typedef = collection.typedefs.get('std::lib::Int4')

    assert null_enum is not None
    assert int4_typedef is not None

    # Null enum base type should reference Int4
    assert null_enum.base_type is not None
    base = null_enum.base_type.base_type
    assert isinstance(base, Define.TypeReference)
    assert base.target is int4_typedef

    TestLogger.success("Null enum base type references Int4")
    TestLogger.info(f"Int4 id: {id(int4_typedef)}", indent=2)
    TestLogger.info(f"Base target id: {id(base.target)}", indent=2)

    TestLogger.complete("Enum base type resolution test passed")


def test_enum_member_value_resolution() -> None:
    """Test that enum member values are auto-incremented correctly."""
    TestLogger.header("Stage 3: Enum Member Value Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get DriverType enum
    driver_type = collection.enums.get('test::enums::DriverType')
    assert driver_type is not None

    # Check auto-incremented values
    expected_values = [0, 1, 2, 3, 4, 5]
    for i, member in enumerate(driver_type.members):
        assert member.value == expected_values[i], \
            f"{member.name} should have value {expected_values[i]}, got {member.value}"
        TestLogger.info(f"{member.name} = {member.value}", indent=2)

    TestLogger.complete("Enum member value resolution test passed")


def test_flag_member_value_resolution() -> None:
    """Test that flag member values are bit-shifted correctly."""
    TestLogger.header("Stage 3: Flag Member Value Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get CreateDeviceFlag
    create_flag = collection.flags.get('test::flags::CreateDeviceFlag')
    assert create_flag is not None

    # Check bit-shifted values (1 << index)
    expected_values = [0x1, 0x2, 0x4, 0x8, 0x20, 0x40, 0x80, 0x100, 0x200]
    for i, member in enumerate(create_flag.members):
        assert member.value == expected_values[i], \
            f"{member.name} should have value 0x{expected_values[i]:X}, got 0x{member.value:X}"
        TestLogger.info(f"{member.name} = 0x{member.value:X}", indent=2)

    TestLogger.complete("Flag member value resolution test passed")


def test_structure_member_type_resolution() -> None:
    """Test that structure member types are resolved correctly."""
    TestLogger.header("Stage 3: Structure Member Type Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get Rational structure
    rational = collection.structures.get('test::structures::Rational')
    assert rational is not None

    # Get Unt4 typedef
    unt4 = collection.typedefs.get('std::lib::Unt4')
    assert unt4 is not None

    # Members should reference Unt4
    for member in rational.members:
        base = member.type_spec.base_type
        assert isinstance(base, Define.TypeReference)
        assert base.target is unt4
        TestLogger.info(f"{member.name}: references {base.target.qualified_name}", indent=2)

    TestLogger.complete("Structure member type resolution test passed")


def test_function_return_type_resolution() -> None:
    """Test that function return types are resolved correctly."""
    TestLogger.header("Stage 3: Function Return Type Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    # Get CreateDeviceAndSwapChain function
    func = collection.functions.get('test::functions::CreateDeviceAndSwapChain')
    assert func is not None

    # Return type should reference ResultCode typedef
    result_code = collection.typedefs.get('test::functions::ResultCode')
    assert result_code is not None

    assert isinstance(func.return_type.base_type, Define.TypeReference)
    assert func.return_type.base_type.target is result_code
    TestLogger.success(f"Return type references {result_code.qualified_name}")

    TestLogger.complete("Function return type resolution test passed")


def test_function_parameter_type_resolution() -> None:
    """Test that function parameter types are resolved correctly."""
    TestLogger.header("Stage 3: Function Parameter Type Resolution")

    loader = Loader.CtdLoader(TEST_CTD_FILES)
    collection = loader.load()

    func = collection.functions.get('test::functions::CreateDeviceAndSwapChain')
    assert func is not None

    # Check flags parameter references CreateDeviceFlag
    flags_param = func.parameters[3]
    assert flags_param.name == 'flags'

    create_flag = collection.flags.get('test::flags::CreateDeviceFlag')
    assert create_flag is not None

    assert isinstance(flags_param.type_spec.base_type, Define.TypeReference)
    assert flags_param.type_spec.base_type.target is create_flag
    TestLogger.success(f"flags parameter references {create_flag.qualified_name}")

    TestLogger.complete("Function parameter type resolution test passed")
