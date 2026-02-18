"""Typespec Resolution with Caching

This module provides cached hierarchical search for resolving type specifications
to actual type declarations. Properly handles pointer and array wrappers, returning
Ctd.Pointer and Ctd.Array instances.

Strategy:
- Cache all lookups by (module, path, name)
- First lookup: O(n * m) where n=search paths, m=declarations per namespace
- Subsequent lookups: O(1) - cache hit
- Stores lists of results (including empty lists for failed searches)

Best for:
- Production code with repeated type resolution
- Large projects with many types
- Scalable performance as codebase grows
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
        self._type_cache: dict[str, list[Ctd.Declaration]] = {}
    
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
                    LOGGER.debug(f"Cache hit for '{type_name}' at '{path}'")
                    base_declarations.extend(cached)
                    continue
                
                # Not cached, search
                results = self._find_all_in_namespace(module, path, type_name)
                self._type_cache[cache_key] = results if results else []
                
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
    # Helper Methods
    # ============================================================================
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
