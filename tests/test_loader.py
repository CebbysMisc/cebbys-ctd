"""Test the CTD module loader."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_load_std_types() -> None:
    """Test loading all .gtd files from resources/ctd directory."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    
    collection = loader.load()
    
    assert len(collection.typedefs) > 0 or len(collection.enums) > 0 or len(collection.flags) > 0, \
        "Should find at least one typedef, enum, or flag"
    
    TestLogger.header("Loaded All GTD Files")
    TestLogger.success(f"Loaded {len(collection.typedefs)} typedefs")
    TestLogger.success(f"Loaded {len(collection.enums)} enums")
    TestLogger.success(f"Loaded {len(collection.flags)} flags")
    
    # Print typedef details
    if collection.typedefs:
        TestLogger.section_break()
        TestLogger.info("Typedefs:")
        for qualified_name, typedef in collection.typedefs.items():
            TestLogger.info(f"{qualified_name} = {typedef.type_spec}", indent=2)
    
    # Print enum details
    if collection.enums:
        TestLogger.section_break()
        TestLogger.info("Enums:")
        for qualified_name, enum in collection.enums.items():
            base = f" : {enum.base_type}" if enum.base_type else ""
            TestLogger.info(f"{qualified_name}{base}", indent=2)
            for member in enum.members:
                TestLogger.info(f"{member.name} = {member.value}", indent=6)
    
    # Print flag details
    if collection.flags:
        TestLogger.section_break()
        TestLogger.info("Flags:")
        for qualified_name, flag in collection.flags.items():
            base = f" : {flag.base_type}" if flag.base_type else ""
            TestLogger.info(f"{qualified_name}{base}", indent=2)
            for member in flag.members:
                TestLogger.info(f"{member.name} = {hex(member.value)}", indent=6)
    
    # Test resolution: Null enum should reference Int4 typedef
    null_enum = collection.enums.get('std::lib::Null')
    assert null_enum is not None, "Should find Null enum"
    assert null_enum.base_type is not None, "Null enum should have base type"
    
    # Check that base type references Int4
    base_type = null_enum.base_type.base_type
    assert isinstance(base_type, Ctd.Define.TypeReference), \
        "Base type should be a TypeReference"
    assert base_type.target.name == "Int4", \
        f"Base type should reference Int4, got {base_type.target.name}"
    
    TestLogger.section_break()
    TestLogger.success(f"Resolution verified: Null enum base type references {base_type.target.qualified_name}")
    
    TestLogger.complete("All loader tests passed")
