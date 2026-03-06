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
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.resolver.manager import (
    CtdDeclarationManager,
    DeclarationReference,
    DirectReference,
)
from typing import Final

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


__all__ = ['TypespecResolverApi']


class TypespecResolverApi:
    """Resolves type specifications to Reference[Declaration].

    Named types → DeclarationReference (backed by manager, auto-updates on alias erasure).
    Builtins → DirectReference(Builtin).
    Pointer/Array → DirectReference(Pointer/Array) where the wrapper's inner base
                    is the inner DeclarationReference so alias erasure propagates.
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
    
    def __init__(self, manager: CtdDeclarationManager):
        """Initialize resolver with manager and empty cache."""
        self._manager = manager
        self._type_cache: dict[str, list[Reference]] = {}
    
    def resolve(self, module: Ctd.Module, namespace: Ctd.Namespace, typespec: Meta.TypespecMeta) -> list[Reference]:
        """Resolve CTD type from typespec, returning all matching References.

        Args:
            module: Module containing the namespace
            namespace: Namespace the typespec was used in
            typespec: The type specification object to resolve
            
        Returns:
            List of resolved Reference objects (may wrap Pointer/Array)
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
            base_refs: list[Reference] = [DirectReference(self._builtin_cache[type_name])]
        else:
            # Search with caching - collect all matches
            search_paths = [namespace.path, *namespace.meta.uses]
            base_refs = []
            
            for path in search_paths:
                cache_key = f"{module.name}::{path}::{type_name}"
                
                # Check cache
                if cache_key in self._type_cache:
                    cached = self._type_cache[cache_key]
                    LOGGER.debug(f"Cache hit for '{type_name}' at '{path}'")
                    base_refs.extend(cached)
                    continue
                
                # Not cached, search
                results = self._find_references_in_namespace(module, path, type_name)
                self._type_cache[cache_key] = results
                
                if results:
                    LOGGER.debug(f"Cached {len(results)} result(s) for '{type_name}' at '{path}'")
                    base_refs.extend(results)
        
        # Rebuild wrappers for each base reference
        final_refs: list[Reference] = []
        for base_ref in base_refs:
            result_ref: Reference = base_ref
            for wrapper in reversed(wrappers):
                if isinstance(wrapper, Meta.PointerTypespecMeta):
                    result_ref = DirectReference(Ctd.Pointer(result_ref))
                elif isinstance(wrapper, Meta.ArrayTypespecMeta):
                    result_ref = DirectReference(Ctd.Array(result_ref, wrapper.size))
            final_refs.append(result_ref)
        
        return final_refs
    
    # ============================================================================
    # Helper Methods
    # ============================================================================
    def _find_references_in_namespace(
        self,
        module: Ctd.Module,
        namespace_path: str,
        type_name: str
    ) -> list[Reference]:
        """Search for ALL type references matching name in specific namespace of module.

        Returns DeclarationReference objects backed by the manager.
        """
        results: list[Reference] = []

        for m in [module, *module.includes]:
            for ns in m.namespaces:
                if ns.path != namespace_path:
                    continue

                for decl in ns.declarations:
                    if decl.name == type_name:
                        key = f"{namespace_path}::{type_name}"
                        ref = self._manager.reference(key)
                        results.append(ref)

        return results
    
    def clear_cache(self) -> None:
        """Clear the type resolution cache."""
        self._type_cache.clear()
        LOGGER.debug("Type resolution cache cleared")
