"""Typespec Resolution

Resolves type specifications to Reference objects by looking up the
CtdDeclarationManager registry directly. Named types are looked up as
``"{namespace}::{typename}"`` for each namespace in the search path.

Since all declarations are pre-registered in the manager during construction,
resolution is a pure key-lookup — O(k) where k = number of search paths.
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
                    is a DeclarationReference so alias erasure propagates through it.
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
        """Initialize resolver with manager."""
        self._manager = manager

    def resolve(self, module: Ctd.Module, namespace: Ctd.Namespace, typespec: Meta.TypespecMeta) -> list[Reference]:
        """Resolve CTD type from typespec, returning all matching References.

        Search order: namespace.path first, then each `use` declaration.
        Each candidate is looked up directly in the manager by key
        ``"{namespace}::{typename}"``.

        Args:
            module: Module containing the namespace (unused after manager migration,
                    kept for API compatibility)
            namespace: Namespace the typespec was used in
            typespec: The type specification object to resolve

        Returns:
            List of resolved Reference objects (may wrap Pointer/Array).
            Empty list if no matches found.

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

        # Check builtins first
        if type_name in self._builtin_cache:
            base_refs: list[Reference] = [DirectReference(self._builtin_cache[type_name])]
        else:
            # Search each namespace in priority order: own namespace first, then uses
            search_paths = [namespace.path, *namespace.meta.uses]
            base_refs = []

            for path in search_paths:
                if self._manager.contains(path, type_name):
                    ref = self._manager.reference(path, type_name)
                    base_refs.append(ref)
                    LOGGER.debug(f"Resolved '{type_name}' via '{path}'")

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

