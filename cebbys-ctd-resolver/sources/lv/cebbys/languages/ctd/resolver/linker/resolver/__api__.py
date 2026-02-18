"""Typespec Resolution Algorithms

This module provides multiple strategies for resolving type specifications to 
actual type declarations. All algorithms are implemented in TypespecResolverApi
as protected methods, allowing easy comparison and selection.

=============================================================================
ALGORITHM COMPARISON
=============================================================================

Algorithm 1: Iterative Unwrapping with Sequential Path Search
--------------------------------------------------------------
Strategy: Unwrap extensions iteratively, search paths one by one
Time: O(n * m) where n=search paths, m=declarations per namespace
Space: O(1) - no caching
Best for: Simple projects, debugging, learning the codebase
Worst for: Large projects with many types and repeated lookups

Algorithm 2: Recursive Descent with Early Return
-------------------------------------------------
Strategy: Recursively unwrap typespecs, resolve at base case
Time: O(n * m) per call, no caching between calls
Space: O(d) where d=nesting depth (stack frames)
Best for: Deep type nesting (e.g., int***[4][5]), functional style
Worst for: Flat types, large projects (no caching)

Algorithm 3: Cached Hierarchical Search ⭐ RECOMMENDED
--------------------------------------------------------
Strategy: Cache all lookups by (module, path, name), search optimally
Time: O(n * m) first lookup, O(1) subsequent lookups
Space: O(k) where k=unique (module, path, name) combinations
Best for: Large projects, repeated type usage, production code
Worst for: One-off scripts, memory-constrained environments

Algorithm 4: Breadth-First Multi-Module Search
-----------------------------------------------
Strategy: Search all modules at each path level before next path
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


class TypespecResolverApi:
    """Base class for typespec resolution strategies.
    
    Resolves type specifications to actual type declarations by searching
    through module namespaces based on use declarations and imports.
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
            Resolved type declaration
            
        Raises:
            TypeError: If typespec type is unexpected
            LookupError: If type cannot be found
        """
        raise NotImplementedError("Subclasses must implement resolve()")
    
    # ============================================================================
    # ALGORITHM 1: Iterative Unwrapping with Sequential Path Search
    # ============================================================================
    # Strategy: Unwrap extensions iteratively, search paths sequentially
    # Pros: Simple logic, easy to debug, matches mental model
    # Cons: May search same namespace multiple times, not optimized
    
    def _resolve_iterative_unwrap(
        self, 
        module: Ctd.Module, 
        namespace: Ctd.Namespace, 
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 1: Iterative unwrapping with sequential path search.
        
        Steps:
        1. Unwrap array/pointer extensions to get base type
        2. Extract type name and signed modifier
        3. Build search paths (namespace::path + use declarations)
        4. Search builtins first
        5. Search each path sequentially until found
        """
        # Step 1: Unwrap extensions
        base_typespec = typespec
        while isinstance(base_typespec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            base_typespec = base_typespec.base
        
        # Step 2: Validate and extract
        if not isinstance(base_typespec, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta at base, got {type(base_typespec)}")
        
        type_name = base_typespec.qualified_name
        
        # Step 3: Build search paths
        search_paths = [namespace.path, *namespace.meta.uses]
        
        # Step 4: Check builtins
        if type_name in self._builtin_cache:
            LOGGER.debug(f"Resolved '{type_name}' as builtin")
            return self._builtin_cache[type_name]
        
        # Step 5: Sequential path search
        for path in search_paths:
            result = self._find_in_namespace(module, path, type_name)
            if result:
                LOGGER.debug(f"Resolved '{type_name}' from path '{path}'")
                return result
        
        raise LookupError(
            f"Type '{type_name}' not found in module '{module.name}' "
            f"with search paths {search_paths}"
        )
    
    # ============================================================================
    # ALGORITHM 2: Recursive Descent with Early Return
    # ============================================================================
    # Strategy: Recursive unwrapping, fail-fast on each level
    # Pros: Elegant recursive structure, natural type nesting handling
    # Cons: Stack overhead, harder to add caching between levels
    
    def _resolve_recursive_descent(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 2: Recursive descent with early return.
        
        Steps:
        1. Check if typespec is TypedTypespecMeta (base case)
        2. If yes, resolve directly
        3. If no (array/pointer), recurse on base, return wrapper
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
        
        # Recursive case: array
        elif isinstance(typespec, Meta.ArrayTypespecMeta):
            # Recurse to resolve base, then we'd wrap in array type
            # (For now just recurse since we're only resolving base declarations)
            return self._resolve_recursive_descent(module, namespace, typespec.base)
        
        # Recursive case: pointer
        elif isinstance(typespec, Meta.PointerTypespecMeta):
            return self._resolve_recursive_descent(module, namespace, typespec.base)
        
        else:
            raise TypeError(f"Unknown TypespecMeta type: {type(typespec)}")
    
    # ============================================================================
    # ALGORITHM 3: Cached Hierarchical Search
    # ============================================================================
    # Strategy: Cache lookups by (module, path, name), search hierarchy optimally
    # Pros: Best performance for repeated lookups, minimal duplicate searches
    # Cons: More complex, cache invalidation concerns
    
    def _resolve_cached_hierarchical(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 3: Cached hierarchical search.
        
        Steps:
        1. Unwrap to base type
        2. Extract type name
        3. For each search path, check cache first
        4. If not cached, search and cache result (even None)
        5. Return first match
        """
        # Unwrap to base
        base_typespec = typespec
        while isinstance(base_typespec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            base_typespec = base_typespec.base
        
        if not isinstance(base_typespec, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta, got {type(base_typespec)}")
        
        type_name = base_typespec.qualified_name
        
        # Check builtins (always fast)
        if type_name in self._builtin_cache:
            return self._builtin_cache[type_name]
        
        # Search with caching
        search_paths = [namespace.path, *namespace.meta.uses]
        for path in search_paths:
            cache_key = f"{module.name}::{path}::{type_name}"
            
            # Check cache
            if cache_key in self._type_cache:
                cached = self._type_cache[cache_key]
                if cached is not None:
                    LOGGER.debug(f"Cache hit for '{type_name}' at '{path}'")
                    return cached
                # Cached None means we already know it's not in this path
                continue
            
            # Not cached, search
            result = self._find_in_namespace(module, path, type_name)
            self._type_cache[cache_key] = result
            
            if result:
                LOGGER.debug(f"Cached '{type_name}' at '{path}'")
                return result
        
        raise LookupError(
            f"Type '{type_name}' not found in module '{module.name}' "
            f"with search paths {search_paths}"
        )
    
    # ============================================================================
    # ALGORITHM 4: Breadth-First Multi-Module Search
    # ============================================================================
    # Strategy: Search all modules at each path level before moving to next path
    # Pros: Finds types in included modules efficiently, good for complex imports
    # Cons: More complex logic, may search unnecessary modules
    
    def _resolve_breadth_first(
        self,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Algorithm 4: Breadth-first multi-module search.
        
        Steps:
        1. Unwrap to base type
        2. Extract type name
        3. Build module list (current + includes)
        4. For each search path:
           - Search in all modules before moving to next path
        5. This prioritizes finding types in current namespace across all modules
        """
        # Unwrap
        base_typespec = typespec
        while isinstance(base_typespec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            base_typespec = base_typespec.base
        
        if not isinstance(base_typespec, Meta.TypedTypespecMeta):
            raise TypeError(f"Expected TypedTypespecMeta, got {type(base_typespec)}")
        
        type_name = base_typespec.qualified_name
        
        # Check builtins
        if type_name in self._builtin_cache:
            return self._builtin_cache[type_name]
        
        # Build module list
        modules = [module, *module.includes]
        search_paths = [namespace.path, *namespace.meta.uses]
        
        # Breadth-first: each path, all modules
        for path in search_paths:
            for search_module in modules:
                result = self._find_in_namespace(search_module, path, type_name)
                if result:
                    LOGGER.debug(
                        f"Found '{type_name}' in module '{search_module.name}' "
                        f"at path '{path}'"
                    )
                    return result
        
        raise LookupError(
            f"Type '{type_name}' not found across {len(modules)} modules "
            f"with search paths {search_paths}"
        )
    
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