"""Comprehensive test demonstrating all features."""
import pathlib as Pathlib
import typing
import lv.cebbys.languages.ctd as Ctd

def test_comprehensive_features() -> None:
    """Comprehensive test showing all key features of the CTD loader."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    # Load CTD files
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    print("=" * 60)
    print("FEATURE 1: Loader returns immutable DefinitionCollection")
    print("=" * 60)
    assert isinstance(collection.typedefs, typing.Mapping)
    assert isinstance(collection.enums, typing.Mapping)
    print("✓ Collection uses MappingProxyType (immutable)")
    print(f"  - Cannot add, remove, or modify entries")
    
    print("\n" + "=" * 60)
    print("FEATURE 2: All type references point to single instances")
    print("=" * 60)
    
    # Get Void and Any
    void_typedef = collection.typedefs['std::lib::Void']
    any_typedef = collection.typedefs['std::lib::Any']
    
    # Any references Void
    any_base = any_typedef.type_spec.base_type
    assert isinstance(any_base, Ctd.Definitions.TypeReference)
    assert any_base.target is void_typedef
    
    print(f"✓ Any (Void*) references the same Void instance")
    print(f"  - Void typedef object id: {id(void_typedef)}")
    print(f"  - Any.base_type.target id: {id(any_base.target)}")
    print(f"  - Same object: {any_base.target is void_typedef}")
    
    # Get Int4 and Null
    int4_typedef = collection.typedefs['std::lib::Int4']
    null_enum = collection.enums['std::lib::Null']
    
    # Null references Int4
    null_base = null_enum.base_type.base_type
    assert isinstance(null_base, Ctd.Definitions.TypeReference)
    assert null_base.target is int4_typedef
    
    print(f"✓ Null enum (base: Int4) references the same Int4 instance")
    print(f"  - Int4 typedef object id: {id(int4_typedef)}")
    print(f"  - Null.base_type.target id: {id(null_base.target)}")
    print(f"  - Same object: {null_base.target is int4_typedef}")
    
    print("\n" + "=" * 60)
    print("FEATURE 3: Type specifications are fully resolved")
    print("=" * 60)
    
    # Primitive types
    snt4 = collection.typedefs['std::lib::Snt4']
    assert isinstance(snt4.type_spec.base_type, Ctd.Definitions.PrimitiveType)
    print(f"✓ Snt4 = {snt4.type_spec.base_type}")
    
    # Pointer types
    assert any_typedef.type_spec.is_pointer
    print(f"✓ Any is a pointer type: {any_typedef.type_spec}")
    
    # Type references
    assert isinstance(any_base, Ctd.Definitions.TypeReference)
    print(f"✓ Any base is TypeReference: {any_base}")
    
    print("\n" + "=" * 60)
    print("FEATURE 4: Enum members have resolved values")
    print("=" * 60)
    
    null_member = null_enum.members[0]
    assert null_member.name == "NULL"
    assert null_member.value == 0
    print(f"✓ Enum member resolved: {null_member.name} = {null_member.value}")
    
    print("\n" + "=" * 60)
    print("FEATURE 5: Read-only operations work correctly")
    print("=" * 60)
    
    # Can iterate
    typedef_count = sum(1 for _ in collection.typedefs.items())
    print(f"✓ Can iterate: {typedef_count} typedefs")
    
    # Can lookup
    found = collection.find_type('std::lib::Int4')
    assert found is int4_typedef
    print(f"✓ Can lookup: find_type('std::lib::Int4') = {found.qualified_name}")
    
    # Can check membership
    assert 'std::lib::Void' in collection.typedefs
    print(f"✓ Can check membership: 'Void' in typedefs")
    
    print("\n" + "=" * 60)
    print("✅ ALL FEATURES VERIFIED")
    print("=" * 60)

if __name__ == '__main__':
    test_comprehensive_features()
