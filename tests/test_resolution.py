"""Test type resolution in detail."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_type_resolution() -> None:
    """Test that type references are properly resolved to single instances."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    TestLogger.header("Type Resolution: Void and Any")
    
    # Get the Void typedef
    void_typedef = collection.typedefs.get('std::lib::Void')
    assert void_typedef is not None, "Should find Void typedef"
    
    # Get the Any typedef which references Void*
    any_typedef = collection.typedefs.get('std::lib::Any')
    assert any_typedef is not None, "Should find Any typedef"
    
    # Any should be a pointer type
    assert any_typedef.type_spec.is_pointer, "Any should be a pointer type"
    
    # The base type should be a TypeReference
    base = any_typedef.type_spec.base_type
    assert isinstance(base, Ctd.Definitions.TypeReference), \
        "Any base type should be TypeReference"
    
    # The target should be the SAME instance as void_typedef
    assert base.target is void_typedef, \
        "Any should reference the same Void typedef instance"
    
    TestLogger.success("Void typedef found")
    TestLogger.success("Any typedef found")
    TestLogger.success("Any references Void as pointer")
    TestLogger.success("VERIFIED: Any.type_spec.base_type.target is the same object as Void typedef")
    TestLogger.info(f"Void typedef id: {id(void_typedef)}", indent=2)
    TestLogger.info(f"Any target id:   {id(base.target)}", indent=2)
    
    # Test enum resolution
    TestLogger.header("Type Resolution: Int4 and Null")
    
    null_enum = collection.enums.get('std::lib::Null')
    assert null_enum is not None, "Should find Null enum"
    
    int4_typedef = collection.typedefs.get('std::lib::Int4')
    assert int4_typedef is not None, "Should find Int4 typedef"
    
    # Null enum base type should reference the SAME Int4 instance
    null_base = null_enum.base_type.base_type
    assert isinstance(null_base, Ctd.Definitions.TypeReference), \
        "Null base type should be TypeReference"
    assert null_base.target is int4_typedef, \
        "Null should reference the same Int4 typedef instance"
    
    TestLogger.success("Int4 typedef found")
    TestLogger.success("Null enum found")
    TestLogger.success("VERIFIED: Null.base_type.base_type.target is the same object as Int4 typedef")
    TestLogger.info(f"Int4 typedef id: {id(int4_typedef)}", indent=2)
    TestLogger.info(f"Null target id:  {id(null_base.target)}", indent=2)
    
    TestLogger.complete("All resolution tests passed")
