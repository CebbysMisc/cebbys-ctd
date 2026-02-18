"""Tests for linker typespec resolution."""

import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.resolver.constructor as Constructor
import lv.cebbys.languages.ctd.resolver.linker.resolver as Resolver
from conftest import TestLogger


def parse_modules(module_dict: dict[str, str]) -> dict[str, Ctd.Module]:
    """Parse CTD module source strings into Ctd.Module objects.
    
    Args:
        module_dict: Dictionary mapping module names to CTD source code
        
    Returns:
        Dictionary mapping module names to constructed Ctd.Module objects
        
    Example:
        modules = parse_modules({
            "test-module": '''
                namespace test {
                    typedef int Int4
                }
            '''
        })
    """
    modules: dict[str, Ctd.Module] = {}
    parser: Antlr4.CtdParser
    parse_tree: Antlr4.CtdGrammar.ModuleDeclarationContext
    module_meta: Meta.ModuleMeta
    module: Ctd.Module
    
    for module_name, module_content in module_dict.items():
        # Parse CTD content with ANTLR4
        parser = Antlr4.CtdParser()
        parse_tree = parser.moduleDeclaration(module_content)
        
        # Convert to meta
        module_meta = Parser.CtdMetaParser.parse_module(parse_tree)
        
        # Construct Ctd.Module
        module = Constructor.ModuleConstructor.construct(module_name, module_meta)
        modules[module_name] = module
    
    return modules


def test_resolver_simple_typedef() -> None:
    """Test resolving a simple typedef to a builtin type."""
    modules: dict[str, Ctd.Module]
    module: Ctd.Module
    namespace: Ctd.Namespace
    resolver: Resolver.TypespecResolverApi
    typespec: Meta.TypespecMeta
    results: list[Ctd.Declaration]
    
    TestLogger.header("Resolver: Simple Typedef Resolution")
    
    # Create test module
    modules = parse_modules({
        "test": '''
namespace app {
    typedef int Int4
}
        '''
    })
    
    module = modules["test"]
    namespace = module.namespaces[0]
    
    # Create resolver
    resolver = Resolver.TypespecResolverApi()
    
    # Create typespec for "int"
    typespec = Meta.TypedTypespecMeta("int")
    
    # Resolve
    results = resolver.resolve(module, namespace, typespec)
    
    # Verify
    assert len(results) == 1, f"Expected 1 result, got {len(results)}"
    assert isinstance(results[0], Ctd.Builtin), f"Expected Builtin, got {type(results[0])}"
    assert results[0].name == "int", f"Expected 'int', got '{results[0].name}'"
    
    TestLogger.success(f"Resolved 'int' to {results[0]}")
    TestLogger.complete("Simple typedef resolution test passed")


def test_resolver_pointer_type() -> None:
    """Test resolving a pointer type."""
    modules: dict[str, Ctd.Module]
    module: Ctd.Module
    namespace: Ctd.Namespace
    resolver: Resolver.TypespecResolverApi
    typespec: Meta.TypespecMeta
    results: list[Ctd.Declaration]
    base_typespec: Meta.TypespecMeta
    
    TestLogger.header("Resolver: Pointer Type Resolution")
    
    # Create test module
    modules = parse_modules({
        "test": '''
namespace app {
    typedef int* IntPtr
}
        '''
    })
    
    module = modules["test"]
    namespace = module.namespaces[0]
    
    # Create resolver
    resolver = Resolver.TypespecResolverApi()
    
    # Create typespec for "int*"
    base_typespec = Meta.TypedTypespecMeta("int")
    typespec = Meta.PointerTypespecMeta(base_typespec)
    
    # Resolve
    results = resolver.resolve(module, namespace, typespec)
    
    # Verify
    assert len(results) == 1, f"Expected 1 result, got {len(results)}"
    assert isinstance(results[0], Ctd.Pointer), f"Expected Pointer, got {type(results[0])}"
    assert isinstance(results[0].base, Ctd.Builtin), f"Expected base to be Builtin, got {type(results[0].base)}"
    assert results[0].base.name == "int", f"Expected base name 'int', got '{results[0].base.name}'"
    
    TestLogger.success(f"Resolved 'int*' to {results[0]}")
    TestLogger.complete("Pointer type resolution test passed")


def test_resolver_array_type() -> None:
    """Test resolving an array type."""
    modules: dict[str, Ctd.Module]
    module: Ctd.Module
    namespace: Ctd.Namespace
    resolver: Resolver.TypespecResolverApi
    typespec: Meta.TypespecMeta
    results: list[Ctd.Declaration]
    base_typespec: Meta.TypespecMeta
    
    TestLogger.header("Resolver: Array Type Resolution")
    
    # Create test module
    modules = parse_modules({
        "test": '''
namespace app {
    typedef int[10] IntArray
}
        '''
    })
    
    module = modules["test"]
    namespace = module.namespaces[0]
    
    # Create resolver
    resolver = Resolver.TypespecResolverApi()
    
    # Create typespec for "int[10]"
    base_typespec = Meta.TypedTypespecMeta("int")
    typespec = Meta.ArrayTypespecMeta(base_typespec, 10)
    
    # Resolve
    results = resolver.resolve(module, namespace, typespec)
    
    # Verify
    assert len(results) == 1, f"Expected 1 result, got {len(results)}"
    assert isinstance(results[0], Ctd.Array), f"Expected Array, got {type(results[0])}"
    assert results[0].size == 10, f"Expected size 10, got {results[0].size}"
    assert isinstance(results[0].base, Ctd.Builtin), f"Expected base to be Builtin, got {type(results[0].base)}"
    assert results[0].base.name == "int", f"Expected base name 'int', got '{results[0].base.name}'"
    
    TestLogger.success(f"Resolved 'int[10]' to {results[0]}")
    TestLogger.complete("Array type resolution test passed")


def test_resolver_complex_nested() -> None:
    """Test resolving complex nested type: int**[4]"""
    modules: dict[str, Ctd.Module]
    module: Ctd.Module
    namespace: Ctd.Namespace
    resolver: Resolver.TypespecResolverApi
    typespec: Meta.TypespecMeta
    results: list[Ctd.Declaration]
    base: Meta.TypespecMeta
    
    TestLogger.header("Resolver: Complex Nested Type Resolution")
    
    # Create test module
    modules = parse_modules({
        "test": '''
namespace app {
    typedef int**[4] ComplexType
}
        '''
    })
    
    module = modules["test"]
    namespace = module.namespaces[0]
    
    # Create resolver
    resolver = Resolver.TypespecResolverApi()
    
    # Create typespec for "int**[4]" - array of 4 pointer-to-pointer-to-int
    base = Meta.TypedTypespecMeta("int")
    base = Meta.PointerTypespecMeta(base)       # int*
    base = Meta.PointerTypespecMeta(base)       # int**
    typespec = Meta.ArrayTypespecMeta(base, 4)  # int**[4]
    
    # Resolve
    results = resolver.resolve(module, namespace, typespec)
    
    # Verify structure: Array(Pointer(Pointer(Builtin("int"))), 4)
    assert len(results) == 1, f"Expected 1 result, got {len(results)}"
    
    # Should be Array
    assert isinstance(results[0], Ctd.Array), f"Expected Array, got {type(results[0])}"
    assert results[0].size == 4, f"Expected size 4, got {results[0].size}"
    
    # Base should be Pointer
    assert isinstance(results[0].base, Ctd.Pointer), f"Expected first base to be Pointer, got {type(results[0].base)}"
    
    # Second level should be Pointer
    assert isinstance(results[0].base.base, Ctd.Pointer), f"Expected second base to be Pointer, got {type(results[0].base.base)}"
    
    # Final base should be Builtin("int")
    assert isinstance(results[0].base.base.base, Ctd.Builtin), f"Expected final base to be Builtin, got {type(results[0].base.base.base)}"
    assert results[0].base.base.base.name == "int", f"Expected final base name 'int', got '{results[0].base.base.base.name}'"
    
    TestLogger.success(f"Resolved 'int**[4]' to {results[0]}")
    TestLogger.complete("Complex nested type resolution test passed")


def test_resolver_caching() -> None:
    """Test that resolver caches results correctly."""
    modules: dict[str, Ctd.Module]
    module: Ctd.Module
    namespace: Ctd.Namespace
    resolver: Resolver.TypespecResolverApi
    typespec: Meta.TypespecMeta
    results1: list[Ctd.Declaration]
    results2: list[Ctd.Declaration]
    
    TestLogger.header("Resolver: Caching Behavior")
    
    # Create test module
    modules = parse_modules({
        "test": '''
namespace app {
    typedef int Int4
    typedef int Int4Copy
}
        '''
    })
    
    module = modules["test"]
    namespace = module.namespaces[0]
    
    # Create resolver
    resolver = Resolver.TypespecResolverApi()
    
    # Create typespec for "int"
    typespec = Meta.TypedTypespecMeta("int")
    
    # Resolve twice
    results1 = resolver.resolve(module, namespace, typespec)
    results2 = resolver.resolve(module, namespace, typespec)
    
    # Verify both return same builtin instance (cached)
    assert len(results1) == 1
    assert len(results2) == 1
    assert results1[0] is results2[0], "Expected cached result to be same instance"
    
    TestLogger.success("Cache returned same instance")
    
    # Clear cache and resolve again
    resolver.clear_cache()
    results3 = resolver.resolve(module, namespace, typespec)
    
    # Should still work after cache clear
    assert len(results3) == 1
    assert isinstance(results3[0], Ctd.Builtin)
    
    TestLogger.success("Cache cleared and resolution still works")
    TestLogger.complete("Caching behavior test passed")
