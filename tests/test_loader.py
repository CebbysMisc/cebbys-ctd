"""Test the CTD module loader."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd

def test_load_std_types() -> None:
    """Test loading the std-types.gtd module."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    
    collection = loader.load()
    
    assert len(collection.typedefs) > 0 or len(collection.enums) > 0, \
        "Should find at least one typedef or enum"
    
    print(f"✓ Loaded {len(collection.typedefs)} typedefs")
    print(f"✓ Loaded {len(collection.enums)} enums")
    
    # Print typedef details
    if collection.typedefs:
        print("\nTypedefs:")
        for qualified_name, typedef in collection.typedefs.items():
            print(f"  - {qualified_name} = {typedef.type_spec}")
    
    # Print enum details
    if collection.enums:
        print("\nEnums:")
        for qualified_name, enum in collection.enums.items():
            base = f" : {enum.base_type}" if enum.base_type else ""
            print(f"  - {qualified_name}{base}")
            for member in enum.members:
                print(f"      {member.name} = {member.value}")
    
    # Test resolution: Null enum should reference Int4 typedef
    null_enum = collection.enums.get('std::lib::Null')
    assert null_enum is not None, "Should find Null enum"
    assert null_enum.base_type is not None, "Null enum should have base type"
    
    # Check that base type references Int4
    base_type = null_enum.base_type.base_type
    assert isinstance(base_type, Ctd.Definitions.TypeReference), \
        "Base type should be a TypeReference"
    assert base_type.target.name == "Int4", \
        f"Base type should reference Int4, got {base_type.target.name}"
    
    print(f"\n✓ Resolution verified: Null enum base type references {base_type.target.qualified_name}")

if __name__ == '__main__':
    test_load_std_types()
    print("\nAll tests passed!")
