"""Test that DefinitionCollection is immutable."""
import pathlib as Pathlib
import pytest
import lv.cebbys.languages.ctd as Ctd

def test_collection_immutability() -> None:
    """Test that the returned collection is immutable."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Definitions.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    # Verify that typedefs and enums return Mapping (immutable)
    import typing
    assert isinstance(collection.typedefs, typing.Mapping), \
        "typedefs should be a Mapping (immutable)"
    assert isinstance(collection.enums, typing.Mapping), \
        "enums should be a Mapping (immutable)"
    
    # Test that we cannot modify the collections
    try:
        collection.typedefs['test'] = None  # type: ignore
        assert False, "Should not be able to modify typedefs"
    except TypeError as e:
        print(f"✓ Cannot modify typedefs: {e}")
    
    try:
        collection.enums['test'] = None  # type: ignore
        assert False, "Should not be able to modify enums"
    except TypeError as e:
        print(f"✓ Cannot modify enums: {e}")
    
    # Test that we cannot delete items
    try:
        del collection.typedefs['lv::cebbys::types::Int4']  # type: ignore
        assert False, "Should not be able to delete from typedefs"
    except TypeError as e:
        print(f"✓ Cannot delete from typedefs: {e}")
    
    # Test that we cannot clear
    try:
        collection.typedefs.clear()  # type: ignore
        assert False, "Should not be able to clear typedefs"
    except AttributeError as e:
        print(f"✓ Cannot clear typedefs: {e}")
    
    print("\n✓ Collection is properly immutable")
    print(f"✓ Typedefs type: {type(collection.typedefs).__name__}")
    print(f"✓ Enums type: {type(collection.enums).__name__}")

if __name__ == '__main__':
    test_collection_immutability()
    print("\n✅ Immutability test passed!")
