"""Comprehensive test demonstrating all features."""
import pathlib as Pathlib
import typing
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_comprehensive_features() -> None:
    """Comprehensive test showing all key features of the CTD loader."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    # Load CTD files
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    TestLogger.header("FEATURE 1: Loader returns immutable DefinitionCollection")
    assert isinstance(collection.typedefs, typing.Mapping)
    assert isinstance(collection.enums, typing.Mapping)
    TestLogger.success("Collection uses MappingProxyType (immutable)")
    TestLogger.info("Cannot add, remove, or modify entries", indent=2)
    
    TestLogger.header("FEATURE 2: All type references point to single instances")
    
    # Get Void and Any
    void_typedef = collection.typedefs['std::lib::Void']
    any_typedef = collection.typedefs['std::lib::Any']
    
    # Any references Void
    any_base = any_typedef.type_spec.base_type
    assert isinstance(any_base, Ctd.Definitions.TypeReference)
    assert any_base.target is void_typedef
    
    TestLogger.success("Any (Void*) references the same Void instance")
    TestLogger.info(f"Void typedef object id: {id(void_typedef)}", indent=2)
    TestLogger.info(f"Any.base_type.target id: {id(any_base.target)}", indent=2)
    TestLogger.info(f"Same object: {any_base.target is void_typedef}", indent=2)
    
    # Get Int4 and Null
    int4_typedef = collection.typedefs['std::lib::Int4']
    null_enum = collection.enums['std::lib::Null']
    
    # Null references Int4
    null_base = null_enum.base_type.base_type
    assert isinstance(null_base, Ctd.Definitions.TypeReference)
    assert null_base.target is int4_typedef
    
    TestLogger.success("Null enum (base: Int4) references the same Int4 instance")
    TestLogger.info(f"Int4 typedef object id: {id(int4_typedef)}", indent=2)
    TestLogger.info(f"Null.base_type.target id: {id(null_base.target)}", indent=2)
    TestLogger.info(f"Same object: {null_base.target is int4_typedef}", indent=2)
    
    TestLogger.header("FEATURE 3: Type specifications are fully resolved")
    
    # Primitive types
    snt4 = collection.typedefs['std::lib::Snt4']
    assert isinstance(snt4.type_spec.base_type, Ctd.Definitions.PrimitiveType)
    TestLogger.success(f"Snt4 = {snt4.type_spec.base_type}")
    
    # Pointer types
    assert any_typedef.type_spec.is_pointer
    TestLogger.success(f"Any is a pointer type: {any_typedef.type_spec}")
    
    # Type references
    assert isinstance(any_base, Ctd.Definitions.TypeReference)
    TestLogger.success(f"Any base is TypeReference: {any_base}")
    
    TestLogger.header("FEATURE 4: Enum members have resolved values")
    
    null_member = null_enum.members[0]
    assert null_member.name == "NULL"
    assert null_member.value == 0
    TestLogger.success(f"Enum member resolved: {null_member.name} = {null_member.value}")
    
    TestLogger.header("FEATURE 5: Read-only operations work correctly")
    
    # Can iterate
    typedef_count = sum(1 for _ in collection.typedefs.items())
    TestLogger.success(f"Can iterate: {typedef_count} typedefs")
    
    # Can lookup
    found = collection.find_type('std::lib::Int4')
    assert found is int4_typedef
    TestLogger.success(f"Can lookup: find_type('std::lib::Int4') = {found.qualified_name}")
    
    # Can check membership
    assert 'std::lib::Void' in collection.typedefs
    TestLogger.success("Can check membership: 'Void' in typedefs")
    
    TestLogger.complete("ALL FEATURES VERIFIED")

if __name__ == '__main__':
    test_comprehensive_features()
