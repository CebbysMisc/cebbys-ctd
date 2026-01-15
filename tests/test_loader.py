"""Test the GTD module loader."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd as Ctd

def test_load_cebbys_types() -> None:
    """Test loading the cebbys-types.gtd module."""
    loader: Ctd.Loader.ModuleLoader
    paths: list[Pathlib.Path]
    modules: list[Ctd.Loader.ModuleInfo]
    
    loader = Ctd.Loader.ModuleLoader()
    paths = [Pathlib.Path('resources/ctd')]
    
    modules = loader.load_modules(paths)
    
    assert len(modules) > 0, "Should find at least one module"
    
    # Find cebbys-types module
    cebbys_types = None
    for module in modules:
        if 'cebbys-types' in module.module_path:
            cebbys_types = module
            break
    
    assert cebbys_types is not None, "Should find cebbys-types module"
    assert cebbys_types.parse_tree is not None, "Parse tree should not be None"
    
    print(f"✓ Loaded module: {cebbys_types.module_path}")
    print(f"✓ File: {cebbys_types.file_path}")
    print(f"✓ Parse tree type: {type(cebbys_types.parse_tree).__name__}")

if __name__ == '__main__':
    test_load_cebbys_types()
    print("\nAll tests passed!")
