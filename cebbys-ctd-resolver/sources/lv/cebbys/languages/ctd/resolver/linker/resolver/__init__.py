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
    
    def resolve(self, module: Ctd.Module, namespace: Ctd.Namespace, typespec: Meta.TypespecMeta) -> list[Ctd.Declaration]:
        """Resolve CTD type from typespec, returning all matching declarations.

        Since a type name may exist in multiple namespaces that are in the search
        path, this method returns ALL matching types found across all search paths.

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
                String name     // Type spec String could be std::collection::String or std::String
                                // Both would be returned if both exist
                String color    
                int count       // This is a builtin type - returns single match
            }

            typedef List Fruits  // If List exists in multiple namespaces, all are returned
        }
        ```
        With the example above, if String exists in both std::collection and std,
        both declarations would be returned in the list.

        Args:
            module: Module containing the namespace
            namespace: Namespace the typespec was used in
            typespec: The type specification object to resolve
            
        Returns:
            List of resolved type declarations (may be wrapped in Pointer/Array)
            Empty list if no matches found
            
        Raises:
            TypeError: If typespec type is unexpected
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
    ) -> list[Ctd.Declaration]:
        """Algorithm 1: Iterative unwrapping with sequential path search.
        
        Steps:
        1. Collect extension wrappers (pointers/arrays) while unwrapping
        2. Resolve base type from ALL matching paths
        3. Rebuild wrappers for each match
        """
        # Step 1: Collect wrappers
        wrappers: list[Meta.TypespecMeta] = []
        current = typespec
        
        while isinstance(current, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            wrappers.append(current)
            current = current.base
        
        # Step 2: Resolve base type from all paths
        if not isinstance(current, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta at base, got {type(current)}")
        
        type_name = current.qualified_name
        search_paths = [namespace.path, *namespace.meta.uses]
        
        # Check builtins first (single match)
        if type_name in self._builtin_cache:
            LOGGER.debug(f"Resolved '{type_name}' as builtin")
            base_declarations = [self._builtin_cache[type_name]]
        else:
            # Collect all matches from all paths
            base_declarations: list[Ctd.Declaration] = []
            for path in search_paths:
                results = self._find_all_in_namespace(module, path, type_name)
                for result in results:
                    LOGGER.debug(f"Resolved '{type_name}' from path '{path}'")
                    base_declarations.append(result)
        
        # Step 3: Rebuild wrappers for each base declaration
        final_results: list[Ctd.Declaration] = []
        for base_decl in base_declarations:
            result = base_decl
            for wrapper in reversed(wrappers):
                if isinstance(wrapper, Meta.PointerTypespecMeta):
                    result = Ctd.Pointer(result)
                elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                    result = Ctd.Array(result, wrapper.size)
            final_results.append(result)
        
        return final_results
    
    # ============================================================================
    # ALGORITHM 2: Recursive Descent with Wrapper Construction
    # ============================================================================
    
    def _resolve_recursive_descent(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> list[Ctd.Declaration]:
        """Algorithm 2: Recursive descent with wrapper construction.
        
        Steps:
        1. Check if typespec is TypedTypespecMeta (base case) -> resolve all matches
        2. If pointer -> recurse on base, return Ctd.Pointer for each result
        3. If array -> recurse on base, return Ctd.Array for each result
        """
        # Base case: typed typespec
        if isinstance(typespec, Meta.TypedTypespecMeta):
            type_name = typespec.qualified_name
            search_paths = [namespace.path, *namespace.meta.uses]
            
            # Check builtins (single match)
            if type_name in self._builtin_cache:
                return [self._builtin_cache[type_name]]
            
            # Collect all matches from all paths
            results: list[Ctd.Declaration] = []
            for path in search_paths:
                matches = self._find_all_in_namespace(module, path, type_name)
                results.extend(matches)
            
            return results
        
        # Recursive case: pointer
        elif isinstance(typespec, Meta.PointerTypespecMeta):
            base_results = self._resolve_recursive_descent(module, namespace, typespec.base)
            return [Ctd.Pointer(base) for base in base_results]
        
        # Recursive case: array
        elif isinstance(typespec, Meta.ArrayTypespecMeta):
            base_results = self._resolve_recursive_descent(module, namespace, typespec.base)
            return [Ctd.Array(base, typespec.size) for base in base_results]
        
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
    ) -> list[Ctd.Declaration]:
        """Algorithm 3: Cached hierarchical search.
        
        Steps:
        1. Collect wrappers while unwrapping to base
        2. Resolve base type with caching - collect ALL matches
        3. Rebuild wrappers for each match
        
        Note: Caches results per (module, path, name) to avoid repeated searches.
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
        
        # Check builtins (always fast, single match)
        if type_name in self._builtin_cache:
            base_declarations = [self._builtin_cache[type_name]]
        else:
            # Search with caching - collect all matches
            search_paths = [namespace.path, *namespace.meta.uses]
            base_declarations: list[Ctd.Declaration] = []
            
            for path in search_paths:
                cache_key = f"{module.name}::{path}::{type_name}"
                
                # Check cache
                if cache_key in self._type_cache:
                    cached = self._type_cache[cache_key]
                    if cached is not None:
                        LOGGER.debug(f"Cache hit for '{type_name}' at '{path}'")
                        # Cached value is a list
                        if isinstance(cached, list):
                            base_declarations.extend(cached)
                        else:
                            base_declarations.append(cached)
                    # Cached None/empty means we already know nothing in this path
                    continue
                
                # Not cached, search
                results = self._find_all_in_namespace(module, path, type_name)
                self._type_cache[cache_key] = results if results else None
                
                if results:
                    LOGGER.debug(f"Cached {len(results)} result(s) for '{type_name}' at '{path}'")
                    base_declarations.extend(results)
        
        # Rebuild wrappers for each base declaration
        final_results: list[Ctd.Declaration] = []
        for base_decl in base_declarations:
            result = base_decl
            for wrapper in reversed(wrappers):
                if isinstance(wrapper, Meta.PointerTypespecMeta):
                    result = Ctd.Pointer(result)
                elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                    result = Ctd.Array(result, wrapper.size)
            final_results.append(result)
        
        return final_results
    
    # ============================================================================
    # ALGORITHM 4: Breadth-First Multi-Module Search
    # ============================================================================
    
    def _resolve_breadth_first(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> list[Ctd.Declaration]:
        """Algorithm 4: Breadth-first multi-module search.
        
        Steps:
        1. Collect wrappers while unwrapping
        2. Resolve base with breadth-first module search - collect ALL matches
        3. Rebuild wrappers for each match
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
            base_declarations = [self._builtin_cache[type_name]]
        else:
            # Build module list
            modules = [module, *module.includes]
            search_paths = [namespace.path, *namespace.meta.uses]
            
            # Breadth-first: each path, all modules - collect ALL matches
            base_declarations: list[Ctd.Declaration] = []
            for path in search_paths:
                for search_module in modules:
                    results = self._find_all_in_namespace(search_module, path, type_name)
                    for result in results:
                        LOGGER.debug(
                            f"Found '{type_name}' in module '{search_module.name}' "
                            f"at path '{path}'"
                        )
                        base_declarations.append(result)
        
        # Rebuild wrappers for each base declaration
        final_results: list[Ctd.Declaration] = []
        for base_decl in base_declarations:
            result = base_decl
            for wrapper in reversed(wrappers):
                if isinstance(wrapper, Meta.PointerTypespecMeta):
                    result = Ctd.Pointer(result)
                elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                    result = Ctd.Array(result, wrapper.size)
            final_results.append(result)
        
        return final_results
    
    # ============================================================================
    # Helper Methods
    # ============================================================================
    
    def _find_in_namespace(
        self,
        module: Ctd.Module,
        namespace_path: str,
        type_name: str
    ) -> Ctd.Declaration | None:
        """Search for type in specific namespace of module (returns first match).
        
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
    
    def _find_all_in_namespace(
        self,
        module: Ctd.Module,
        namespace_path: str,
        type_name: str
    ) -> list[Ctd.Declaration]:
        """Search for ALL types matching name in specific namespace of module.
        
        Args:
            module: Module to search
            namespace_path: Namespace path (e.g., "std::collection")
            type_name: Simple type name to find
            
        Returns:
            List of all matching declarations (empty if none found)
        """
        results: list[Ctd.Declaration] = []
        
        for ns in module.namespaces:
            if ns.path != namespace_path:
                continue
            
            for decl in ns.declarations:
                if decl.name == type_name:
                    results.append(decl)
        
        return results
    
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
    - Returns ALL matching types from all search paths
    
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
    ) -> list[Ctd.Declaration]:
        """Resolve typespec to declarations using cached hierarchical search.
        
        Returns ALL matching types found across all search paths. For example,
        if 'String' exists in both 'std::collection' and 'std', both will be
        returned in the list.
        
        Properly handles pointer and array extensions, returning Ctd.Pointer
        and Ctd.Array instances as needed.
        
        See TypespecResolverApi.resolve() for full documentation.
        """
        return self._resolve_cached_hierarchical(module, namespace, typespec)