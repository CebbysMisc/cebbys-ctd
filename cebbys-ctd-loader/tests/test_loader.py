"""Test for CtdLoader basic functionality."""
import pathlib as Pathlib
import pytest as Pytest
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.types.define as Define

# Import TestLogger from workspace conftest
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent.parent))
from conftest import TestLogger


def test_loader_transformation_chain() -> None:
    """Test that CtdLoader executes all transformation stages."""
    loader: Loader.CtdLoader
    test_dir: Pathlib.Path
    
    TestLogger.header("CtdLoader: Transformation Chain")
    
    # Get test resources directory
    test_dir = Pathlib.Path(__file__).parent / "resources" / "ctd" / "simple-test"
    assert test_dir.exists(), f"Test directory not found: {test_dir}"
    
    TestLogger.info(f"Loading from: {test_dir}")
    
    # Create loader (executes transformation chain in __init__)
    loader = Loader.CtdLoader([test_dir])
    
    # Verify Stage 1: File discovery
    TestLogger.info(f"Stage 1: Found {len(loader._ctd_files)} .ctd files")
    assert len(loader._ctd_files) > 0, "Should find at least one .ctd file"
    assert all(f.suffix == '.ctd' for f in loader._ctd_files), "All files should be .ctd"
    
    # Verify Stage 2: ANTLR4 parsing
    TestLogger.info(f"Stage 2: Parsed {len(loader._module_contexts)} contexts")
    assert len(loader._module_contexts) > 0, "Should parse at least one context"
    
    # Check context structure
    for file_path, context in loader._module_contexts:
        assert file_path.exists(), f"File should exist: {file_path}"
        assert context is not None, "Context should not be None"
        TestLogger.info(f"  - {file_path.name}: {type(context).__name__}")
    
    # Verify Stage 3: Meta conversion
    TestLogger.info(f"Stage 3: Converted {len(loader._module_metas)} meta objects")
    assert len(loader._module_metas) > 0, "Should convert at least one meta"
    
    # Check meta structure
    for file_path, module_meta in loader._module_metas:
        assert file_path.exists(), f"File should exist: {file_path}"
        assert module_meta is not None, "ModuleMeta should not be None"
        TestLogger.info(f"  - {file_path.name}: {type(module_meta).__name__}")
    
    TestLogger.success("All transformation stages executed successfully")
    TestLogger.complete("Test passed")


def test_loader_with_existing_resources() -> None:
    """Test loader with existing CTD resources."""
    loader: Loader.CtdLoader
    resources_dir: Pathlib.Path
    collection: Define.DefinitionCollection
    
    TestLogger.header("CtdLoader: Existing Resources")
    
    # Use existing std-types.ctd
    resources_dir = Pathlib.Path(__file__).parent.parent / "resources" / "ctd"
    assert resources_dir.exists(), f"Resources directory not found: {resources_dir}"
    
    TestLogger.info(f"Loading from: {resources_dir}")
    
    # Create loader
    loader = Loader.CtdLoader([resources_dir])
    
    TestLogger.info(f"Found {len(loader._ctd_files)} files")
    TestLogger.info(f"Parsed {len(loader._module_contexts)} contexts")
    TestLogger.info(f"Converted {len(loader._module_metas)} metas")
    
    # Test existing load() method still works
    collection = loader.load()
    assert collection is not None, "Should return collection"
    
    TestLogger.success(f"Loaded {len(collection.typedefs)} typedefs")
    TestLogger.complete("Test passed")


def test_loader_empty_directory() -> None:
    """Test loader with empty directory."""
    loader: Loader.CtdLoader
    empty_dir: Pathlib.Path
    
    TestLogger.header("CtdLoader: Empty Directory")
    
    # Create empty directory
    empty_dir = Pathlib.Path(__file__).parent / "resources" / "ctd" / "empty"
    empty_dir.mkdir(parents=True, exist_ok=True)
    
    TestLogger.info(f"Loading from empty: {empty_dir}")
    
    # Create loader
    loader = Loader.CtdLoader([empty_dir])
    
    # Should handle empty gracefully
    assert len(loader._ctd_files) == 0, "Should find no files"
    assert len(loader._module_contexts) == 0, "Should parse no contexts"
    assert len(loader._module_metas) == 0, "Should convert no metas"
    
    TestLogger.success("Handled empty directory gracefully")
    TestLogger.complete("Test passed")
