"""Test that DefinitionCollection is immutable."""
import pathlib as Pathlib
import typing
import pytest
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger

def test_collection_immutability() -> None:
    """Test that the returned collection is immutable."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection
    
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()
    
    TestLogger.header("Collection Immutability Tests")
    
    # Verify that typedefs and enums return Mapping (immutable)
    assert isinstance(collection.typedefs, typing.Mapping), \
        "typedefs should be a Mapping (immutable)"
    assert isinstance(collection.enums, typing.Mapping), \
        "enums should be a Mapping (immutable)"
    
    # Test that we cannot modify the collections
    try:
        collection.typedefs['test'] = None  # type: ignore
        assert False, "Should not be able to modify typedefs"
    except TypeError as e:
        TestLogger.success(f"Cannot modify typedefs: {e}")
    
    try:
        collection.enums['test'] = None  # type: ignore
        assert False, "Should not be able to modify enums"
    except TypeError as e:
        TestLogger.success(f"Cannot modify enums: {e}")
    
    # Test that we cannot delete items
    try:
        del collection.typedefs['std::lib::Int4']  # type: ignore
        assert False, "Should not be able to delete from typedefs"
    except TypeError as e:
        TestLogger.success(f"Cannot delete from typedefs: {e}")
    
    # Test that we cannot clear
    try:
        collection.typedefs.clear()  # type: ignore
        assert False, "Should not be able to clear typedefs"
    except AttributeError as e:
        TestLogger.success(f"Cannot clear typedefs: {e}")
    
    TestLogger.section_break()
    TestLogger.success("Collection is properly immutable")
    TestLogger.info(f"Typedefs type: {type(collection.typedefs).__name__}", indent=2)
    TestLogger.info(f"Enums type: {type(collection.enums).__name__}", indent=2)
    
    TestLogger.complete("Immutability test passed")
