"""Test type resolution in detail."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd

def test_type_resolution() -> None:
    """Test that type references are properly resolved to single instances."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
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
    
    print("✓ Void typedef found")
    print("✓ Any typedef found")
    print("✓ Any references Void as pointer")
    print(f"✓ VERIFIED: Any.type_spec.base_type.target is the same object as Void typedef")
    print(f"  - Void typedef id: {id(void_typedef)}")
    print(f"  - Any target id:   {id(base.target)}")
    
    # Test enum resolution
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
    
    print("✓ Int4 typedef found")
    print("✓ Null enum found")
    print(f"✓ VERIFIED: Null.base_type.base_type.target is the same object as Int4 typedef")
    print(f"  - Int4 typedef id: {id(int4_typedef)}")
    print(f"  - Null target id:  {id(null_base.target)}")

if __name__ == '__main__':
    test_type_resolution()
    print("\n✅ All resolution tests passed!")
