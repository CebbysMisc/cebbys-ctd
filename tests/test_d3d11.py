"""Test d3d11 types and new syntax features."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_d3d11_enum_members() -> None:
    """Test that d3d11 enum members and new syntax are parsed correctly."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    TestLogger.header("D3D11 Type Definitions")
    TestLogger.info(f"Total typedefs: {len(collection.typedefs)}")
    TestLogger.info(f"Total enums: {len(collection.enums)}")
    
    # Verify d3d11 DriverType enum loaded
    driver_type = collection.enums.get('com::microsoft::direct::graphics::d3d11::DriverType')
    assert driver_type is not None, "Should find DriverType enum"
    
    TestLogger.success(f"DriverType enum found with {len(driver_type.members)} members")
    
    # Verify base type resolves to std::lib::Int4
    assert driver_type.base_type is not None, "DriverType should have base type"
    base_type_ref = driver_type.base_type.base_type
    assert isinstance(base_type_ref, Ctd.Define.TypeReference), \
        "Base type should be TypeReference"
    
    int4_typedef = collection.typedefs.get('std::lib::Int4')
    assert int4_typedef is not None, "Should find std::lib::Int4"
    assert base_type_ref.target is int4_typedef, \
        "DriverType base should reference std::lib::Int4"
    
    TestLogger.success(f"Base type resolved: {base_type_ref.target.qualified_name}")
    
    # Verify enum members have auto-incremented values
    expected_values = [0, 1, 2, 3, 4, 5]
    expected_names = ['UNKNOWN', 'HARDWARE', 'REFERENCE', 'NULL', 'SOFTWARE', 'WARP']
    
    assert len(driver_type.members) == 6, f"Should have 6 members, got {len(driver_type.members)}"
    
    TestLogger.section_break()
    TestLogger.info("Enum members:")
    for i, member in enumerate(driver_type.members):
        TestLogger.info(f"{member.name} = {member.value}", indent=2)
        assert member.name == expected_names[i], \
            f"Member {i} should be {expected_names[i]}, got {member.name}"
        assert member.value == expected_values[i], \
            f"Member {i} should have value {expected_values[i]}, got {member.value}"
    
    # Verify CreateDeviceFlag flag exists and has correct bit-shifted values
    create_device_flag = collection.flags.get('com::microsoft::direct::graphics::d3d11::CreateDeviceFlag')
    assert create_device_flag is not None, "Should find CreateDeviceFlag flag"
    TestLogger.section_break()
    TestLogger.success(f"CreateDeviceFlag flag found: {create_device_flag.qualified_name}")
    
    # Verify flag members have bit-shifted values
    expected_flag_values = [0x1, 0x2, 0x4, 0x8, 0x20, 0x40, 0x80, 0x100, 0x200]
    expected_flag_names = ['SINGLETHREADED', 'DEBUG', 'SWITCH_TO_REF', 'PREVENT_INTERNAL_THREADING_OPTIMIZATIONS',
                          'BGRA_SUPPORT', 'DEBUGGABLE', 'PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY',
                          'DISABLE_GPU_TIMEOUT', 'VIDEO_SUPPORT']
    
    assert len(create_device_flag.members) == 9, f"Should have 9 members, got {len(create_device_flag.members)}"
    
    TestLogger.info("Flag members:")
    for i, member in enumerate(create_device_flag.members):
        TestLogger.info(f"{member.name} = 0x{member.value:X}", indent=2)
        assert member.name == expected_flag_names[i], \
            f"Member {i} should be {expected_flag_names[i]}, got {member.name}"
        assert member.value == expected_flag_values[i], \
            f"Member {i} should have value 0x{expected_flag_values[i]:X}, got 0x{member.value:X}"
    
    TestLogger.section_break()
    TestLogger.success("All enum members auto-incremented correctly")
    TestLogger.success("All flag members bit-shifted correctly")
    TestLogger.success("Manual offset in BGRA_SUPPORT respected")
    TestLogger.success("Cross-file type resolution working (d3d11 -> std-types)")
    TestLogger.success("New syntax parsed successfully (structure, function, annotation, flags)")
    
    # Verify function is resolved correctly
    TestLogger.section_break()
    TestLogger.info("Functions:")
    TestLogger.info(f"Total functions: {len(collection.functions)}")

    d3d11_func = collection.functions.get('com::microsoft::direct::graphics::d3d11::D3D11CreateDeviceAndSwapChain')
    assert d3d11_func is not None, "Should find D3D11CreateDeviceAndSwapChain function"

    TestLogger.success(f"Function: {d3d11_func.qualified_name}")
    TestLogger.info(f"Decorators: {d3d11_func.decorators}", indent=2)
    TestLogger.info(f"Return type: {d3d11_func.return_type}", indent=2)
    TestLogger.info(f"Parameters: {len(d3d11_func.parameters)}", indent=2)

    # Verify function decorator
    assert len(d3d11_func.decorators) == 1, \
        f"Function should have 1 decorator, got {len(d3d11_func.decorators)}"
    assert d3d11_func.decorators[0].name == "WinApi", \
        f"Function decorator should be 'WinApi', got '{d3d11_func.decorators[0].name}'"

    # Verify return type resolves to ResultCode typedef
    result_code = collection.typedefs.get('com::microsoft::direct::graphics::d3d11::ResultCode')
    assert result_code is not None, "Should find ResultCode typedef"
    assert isinstance(d3d11_func.return_type.base_type, Ctd.Define.TypeReference), \
        "Return type should be TypeReference"
    assert d3d11_func.return_type.base_type.target is result_code, \
        "Return type should reference ResultCode"

    TestLogger.success("Return type resolved to ResultCode")

    # Verify parameters
    assert len(d3d11_func.parameters) == 8, \
        f"Should have 8 parameters, got {len(d3d11_func.parameters)}"

    # Check first parameter (adapter with @Nullable decorator and pointer type)
    adapter_param = d3d11_func.parameters[0]
    assert adapter_param.name == "adapter", f"First param should be 'adapter', got '{adapter_param.name}'"
    assert len(adapter_param.decorators) == 1, \
        f"First param should have 1 decorator, got {len(adapter_param.decorators)}"
    assert adapter_param.decorators[0].name == "Nullable", \
        f"First param decorator should be 'Nullable', got '{adapter_param.decorators[0].name}'"
    assert adapter_param.type_spec.is_pointer, "adapter should be pointer type"

    TestLogger.success("Parameter @Nullable Adapter* adapter resolved correctly")

    # Check parameter with flag type
    flags_param = d3d11_func.parameters[3]
    assert flags_param.name == "flags", f"Fourth param should be 'flags', got '{flags_param.name}'"
    assert isinstance(flags_param.type_spec.base_type, Ctd.Define.TypeReference), \
        "flags type should be TypeReference"
    assert flags_param.type_spec.base_type.target is create_device_flag, \
        "flags should reference CreateDeviceFlag"

    TestLogger.success("Parameter CreateDeviceFlag flags resolved correctly")

    for param in d3d11_func.parameters:
        decorators_str = " ".join(str(d) for d in param.decorators)
        if decorators_str:
            decorators_str += " "
        ptr_str = "*" if param.type_spec.is_pointer else ""
        TestLogger.info(f"{decorators_str}{param.type_spec.base_type}{ptr_str} {param.name}", indent=4)

    TestLogger.section_break()
    TestLogger.success("Function definition resolved with all types")
    TestLogger.success("Flag type references resolved correctly (used in function parameters)")

    TestLogger.complete("D3D11 test complete")
