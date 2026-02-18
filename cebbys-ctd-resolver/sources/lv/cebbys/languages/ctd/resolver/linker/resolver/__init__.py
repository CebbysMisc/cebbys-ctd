"""Typespec Resolution Algorithms

This module provides multiple strategies for resolving type specifications to 
actual type declarations. All algorithms properly handle pointer and array
wrappers, returning Ctd.Pointer and Ctd.Array instances.

=============================================================================
ALGORITHM COMPARISON
=============================================================================

Algorithm 1: Iterative Unwrapping with Sequential Path Search
--------------------------------------------------------------
Strategy: Unwrap extensions iteratively, search paths one by one, rebuild wrappers
Time: O(n * m) where n=search paths, m=declarations per namespace
Space: O(1) - no caching
Best for: Simple projects, debugging, learning the codebase
Worst for: Large projects with many types and repeated lookups

Algorithm 2: Recursive Descent with Wrapper Construction
---------------------------------------------------------
Strategy: Recursively unwrap typespecs, resolve at base case, build wrappers on return
Time: O(n * m) per call, no caching between calls
Space: O(d) where d=nesting depth (stack frames)
Best for: Deep type nesting (e.g., int***[4][5]), functional style
Worst for: Flat types, large projects (no caching)

Algorithm 3: Cached Hierarchical Search ⭐ RECOMMENDED
--------------------------------------------------------
Strategy: Cache all lookups by (module, path, name), search optimally, wrap results
Time: O(n * m) first lookup, O(1) subsequent lookups
Space: O(k) where k=unique (module, path, name) combinations
Best for: Large projects, repeated type usage, production code
Worst for: One-off scripts, memory-constrained environments

Algorithm 4: Breadth-First Multi-Module Search
-----------------------------------------------
Strategy: Search all modules at each path level, then wrap results
Time: O(p * m * d) where p=paths, m=modules, d=declarations
Space: O(1) - no caching
Best for: Complex multi-module hierarchies, prioritizing current namespace
Worst for: Simple single-module projects, performance-critical code

=============================================================================
RECOMMENDATION: Use Algorithm 3 (Cached Hierarchical Search)
=============================================================================

Rationale:
- Production-ready: Handles large codebases efficiently
- Balanced: Good time/space tradeoff
- Predictable: Consistent performance across calls
- Debuggable: Cache can be inspected and cleared
- Scalable: Performance improves with codebase size

When to use alternatives:
- Algorithm 1: Teaching/learning, small one-off scripts
- Algorithm 2: Academic interest in recursive algorithms
- Algorithm 4: Complex include hierarchies where module priority matters

=============================================================================
"""

import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from typing import Final

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


__all__ = ['TypespecResolverApi', 'BasicTypespecResolver']


class TypespecResolverApi:
    """Base class for typespec resolution strategies.
    
    Resolves type specifications to actual type declarations by searching
    through module namespaces based on use declarations and imports.
    Properly constructs Pointer and Array wrappers for extension types.
    """
    
    # Builtin type cache (shared across all resolvers)
    _builtin_cache: Final[dict[str, Ctd.Builtin]] = {
        "char": Ctd.Builtin("char"),
        "short": Ctd.Builtin("short"),
        "int": Ctd.Builtin("int"),
        "long": Ctd.Builtin("long"),
        "float": Ctd.Builtin("float"),
        "double": Ctd.Builtin("double"),
        "void": Ctd.Builtin("void"),
    }
    
    def __init__(self):
        """Initialize resolver with empty cache."""
        self._type_cache: dict[str, Ctd.Declaration | None] = {}
    
    def resolve(self, module: Ctd.Module, namespace: Ctd.Namespace, typespec: Meta.TypespecMeta) -> Ctd.Declaration:
        """Resolve CTD type singleton from typespec.

        Example module
        ```
        // Module uses namespaces from two other modules
        import "std/collections"
        import "std/types"
        
        namespace lv::cebbys::app {
            // In this namespace use type suffix for type specs
            use std::collection
            use std

            structure Fruit {
                String name     // Type spec String could be std::collection::String or std::String or String 
                String color    
                int count       // This is a builtin type and it is immediately found due to being keyword
            }

            typedef List Fruits
        }
        ```
        With the example above type String shall be resolved from module "std/types" namespace std
        And the List would be resolved from "std/collections" std::collection namespace

        Args:
            module: Module containing the namespace
            namespace: Namespace the typespec was used in
            typespec: The type specification object to resolve
            
        Returns:
            Resolved type declaration (may be wrapped in Pointer/Array)
            
        Raises:
            TypeError: If typespec type is unexpected
            LookupError: If type cannot be found
        """
        raise NotImplementedError("Subclasses must implement resolve()")
    
    # ============================================================================
    # ALGORITHM 1: Iterative Unwrapping with Sequential Path Search
    # ============================================================================
    
    def _resolve_iterative_unwrap(
        self, 
        module: Ctd.Module, 
        namespace: Ctd.Namespace, 
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 1: Iterative unwrapping with sequential path search.
        
        Steps:
        1. Collect extension wrappers (pointers/arrays) while unwrapping
        2. Resolve base type
        3. Rebuild wrappers in reverse order
        """
        # Step 1: Collect wrappers
        wrappers: list[Meta.TypespecMeta] = []
        current = typespec
        
        while isinstance(current, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            wrappers.append(current)
            current = current.base
        
        # Step 2: Resolve base type
        if not isinstance(current, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta at base, got {type(current)}")
        
        type_name = current.qualified_name
        search_paths = [namespace.path, *namespace.meta.uses]
        
        # Check builtins
        if type_name in self._builtin_cache:
            LOGGER.debug(f"Resolved '{type_name}' as builtin")
            base_decl = self._builtin_cache[type_name]
        else:
            # Sequential path search
            base_decl = None
            for path in search_paths:
                result = self._find_in_namespace(module, path, type_name)
                if result:
                    LOGGER.debug(f"Resolved '{type_name}' from path '{path}'")
                    base_decl = result
                    break
            
            if base_decl is None:
                raise LookupError(
                    f"Type '{type_name}' not found in module '{module.name}' "
                    f"with search paths {search_paths}"
                )
        
        # Step 3: Rebuild wrappers in reverse order
        result = base_decl
        for wrapper in reversed(wrappers):
            if isinstance(wrapper, Meta.PointerTypespecMeta):
                result = Ctd.Pointer(result)
            elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                result = Ctd.Array(result, wrapper.size)
        
        return result
    
    # ============================================================================
    # ALGORITHM 2: Recursive Descent with Wrapper Construction
    # ============================================================================
    
    def _resolve_recursive_descent(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 2: Recursive descent with wrapper construction.
        
        Steps:
        1. Check if typespec is TypedTypespecMeta (base case) -> resolve
        2. If pointer -> recurse on base, return Ctd.Pointer(resolved_base)
        3. If array -> recurse on base, return Ctd.Array(resolved_base, size)
        """
        # Base case: typed typespec
        if isinstance(typespec, Meta.TypedTypespecMeta):
            type_name = typespec.qualified_name
            search_paths = [namespace.path, *namespace.meta.uses]
            
            # Check builtins
            if type_name in self._builtin_cache:
                return self._builtin_cache[type_name]
            
            # Search paths
            for path in search_paths:
                result = self._find_in_namespace(module, path, type_name)
                if result:
                    return result
            
            raise LookupError(f"Type '{type_name}' not found")
        
        # Recursive case: pointer
        elif isinstance(typespec, Meta.PointerTypespecMeta):
            base_resolved = self._resolve_recursive_descent(module, namespace, typespec.base)
            return Ctd.Pointer(base_resolved)
        
        # Recursive case: array
        elif isinstance(typespec, Meta.ArrayTypespecMeta):
            base_resolved = self._resolve_recursive_descent(module, namespace, typespec.base)
            return Ctd.Array(base_resolved, typespec.size)
        
        else:
            raise TypeError(f"Unknown TypespecMeta type: {type(typespec)}")
    
    # ============================================================================
    # ALGORITHM 3: Cached Hierarchical Search
    # ============================================================================
    
    def _resolve_cached_hierarchical(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 3: Cached hierarchical search.
        
        Steps:
        1. Collect wrappers while unwrapping to base
        2. Resolve base type with caching
        3. Rebuild wrappers
        """
        # Collect wrappers
        wrappers: list[Meta.TypespecMeta] = []
        current = typespec
        
        while isinstance(current, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            wrappers.append(current)
            current = current.base
        
        # Resolve base
        if not isinstance(current, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta, got {type(current)}")
        
        type_name = current.qualified_name
        
        # Check builtins (always fast)
        if type_name in self._builtin_cache:
            base_decl = self._builtin_cache[type_name]
        else:
            # Search with caching
            search_paths = [namespace.path, *namespace.meta.uses]
            base_decl = None
            
            for path in search_paths:
                cache_key = f"{module.name}::{path}::{type_name}"
                
                # Check cache
                if cache_key in self._type_cache:
                    cached = self._type_cache[cache_key]
                    if cached is not None:
                        LOGGER.debug(f"Cache hit for '{type_name}' at '{path}'")
                        base_decl = cached
                        break
                    # Cached None means we already know it's not in this path
                    continue
                
                # Not cached, search
                result = self._find_in_namespace(module, path, type_name)
                self._type_cache[cache_key] = result
                
                if result:
                    LOGGER.debug(f"Cached '{type_name}' at '{path}'")
                    base_decl = result
                    break
            
            if base_decl is None:
                raise LookupError(
                    f"Type '{type_name}' not found in module '{module.name}' "
                    f"with search paths {search_paths}"
                )
        
        # Rebuild wrappers
        result = base_decl
        for wrapper in reversed(wrappers):
            if isinstance(wrapper, Meta.PointerTypespecMeta):
                result = Ctd.Pointer(result)
            elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                result = Ctd.Array(result, wrapper.size)
        
        return result
    
    # ============================================================================
    # ALGORITHM 4: Breadth-First Multi-Module Search
    # ============================================================================
    
    def _resolve_breadth_first(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 4: Breadth-first multi-module search.
        
        Steps:
        1. Collect wrappers while unwrapping
        2. Resolve base with breadth-first module search
        3. Rebuild wrappers
        """
        # Collect wrappers
        wrappers: list[Meta.TypespecMeta] = []
        current = typespec
        
        while isinstance(current, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            wrappers.append(current)
            current = current.base
        
        # Resolve base
        if not isinstance(current, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta, got {type(current)}")
        
        type_name = current.qualified_name
        
        # Check builtins
        if type_name in self._builtin_cache:
            base_decl = self._builtin_cache[type_name]
        else:
            # Build module list
            modules = [module, *module.includes]
            search_paths = [namespace.path, *namespace.meta.uses]
            
            # Breadth-first: each path, all modules
            base_decl = None
            for path in search_paths:
                for search_module in modules:
                    result = self._find_in_namespace(search_module, path, type_name)
                    if result:
                        LOGGER.debug(
                            f"Found '{type_name}' in module '{search_module.name}' "
                            f"at path '{path}'"
                        )
                        base_decl = result
                        break
                if base_decl:
                    break
            
            if base_decl is None:
                raise LookupError(
                    f"Type '{type_name}' not found across {len(modules)} modules "
                    f"with search paths {search_paths}"
                )
        
        # Rebuild wrappers
        result = base_decl
        for wrapper in reversed(wrappers):
            if isinstance(wrapper, Meta.PointerTypespecMeta):
                result = Ctd.Pointer(result)
            elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                result = Ctd.Array(result, wrapper.size)
        
        return result
    
    # ============================================================================
    # Helper Methods
    # ============================================================================
    
    def _find_in_namespace(
        self,
        module: Ctd.Module,
        namespace_path: str,
        type_name: str
    ) -> Ctd.Declaration | None:
        """Search for type in specific namespace of module.
        
        Args:
            module: Module to search
            namespace_path: Namespace path (e.g., "std::collection")
            type_name: Simple type name to find
            
        Returns:
            Declaration if found, None otherwise
        """
        for ns in module.namespaces:
            if ns.path != namespace_path:
                continue
            
            for decl in ns.declarations:
                if decl.name == type_name:
                    return decl
        
        return None
    
    def clear_cache(self) -> None:
        """Clear the type resolution cache."""
        self._type_cache.clear()
        LOGGER.debug("Type resolution cache cleared")


class BasicTypespecResolver(TypespecResolverApi):
    """Default typespec resolver using cached hierarchical search.
    
    Uses Algorithm 3 (Cached Hierarchical Search) as it provides:
    - Best performance for repeated lookups (common in large codebases)
    - Minimal duplicate searches across namespaces
    - Simple, predictable behavior
    - Good balance of speed and memory usage
    - Properly constructs Pointer and Array wrappers
    
    Algorithm rationale:
    - Algorithm 1 (Iterative): Too slow for large projects (no caching)
    - Algorithm 2 (Recursive): Elegant but stack overhead, no inter-call caching
    - Algorithm 3 (Cached): ✓ Best overall - fast, efficient, scalable
    - Algorithm 4 (Breadth-first): Overkill for simple cases, harder to debug
    """
    
    def resolve(
        self, 
        module: Ctd.Module, 
        namespace: Ctd.Namespace, 
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Resolve typespec to declaration using cached hierarchical search.
        
        Properly handles pointer and array extensions, returning Ctd.Pointer
        and Ctd.Array instances as needed.
        
        See TypespecResolverApi.resolve() for full documentation.
        """
        return self._resolve_cached_hierarchical(module, namespace, typespec)