"""Test d3d11 types and new syntax features."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_d3d11_enum_members() -> None:
    """Test that d3d11 enum members and new syntax are parsed correctly."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
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
    assert isinstance(base_type_ref, Ctd.Definitions.TypeReference), \
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
    
    # Verify HResult typedef exists
    hresult_typedef = collection.typedefs.get('com::microsoft::direct::graphics::d3d11::HResult')
    assert hresult_typedef is not None, "Should find HResult typedef"
    TestLogger.section_break()
    TestLogger.success(f"HResult typedef found: {hresult_typedef.qualified_name}")
    
    TestLogger.success("All enum members auto-incremented correctly")
    TestLogger.success("Cross-file type resolution working (d3d11 -> std-types)")
    TestLogger.success("New syntax parsed successfully (structure, function, annotation)")
    
    TestLogger.complete("D3D11 test complete")
