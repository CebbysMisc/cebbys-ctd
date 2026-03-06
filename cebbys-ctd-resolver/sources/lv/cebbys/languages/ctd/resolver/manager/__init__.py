from typing import TypeVar, Generic
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

T = TypeVar("T")

__all__ = ["CtdDeclarationManager", "DeclarationReference", "DirectReference"]


class CtdDeclarationManager:
    """Registry mapping qualified declaration keys to Declaration instances.

    Keys are always formatted as ``"{namespace}::{typename}"`` — use
    :meth:`make_key` to construct them consistently.

    All named declarations are pre-registered during construction.
    AliasLinker updates entries to erase aliases after resolution.
    """

    @staticmethod
    def make_key(namespace: str, typename: str) -> str:
        """Return the canonical registry key for a declaration."""
        return f"{namespace}::{typename}"

    def __init__(self) -> None:
        self._registry: dict[str, object] = {}

    def register(self, namespace: str, typename: str, declaration: object) -> None:
        key = CtdDeclarationManager.make_key(namespace, typename)
        if key in self._registry:
            LOGGER.warning(f"Overwriting existing registration for '{key}'")
        self._registry[key] = declaration
        LOGGER.debug(f"Registered '{key}'")

    def get(self, namespace: str, typename: str) -> object | None:
        return self._registry.get(CtdDeclarationManager.make_key(namespace, typename))

    def get_by_key(self, key: str) -> object | None:
        return self._registry.get(key)

    def update(self, namespace: str, typename: str, declaration: object) -> None:
        key = CtdDeclarationManager.make_key(namespace, typename)
        if key not in self._registry:
            LOGGER.warning(f"Updating unregistered key '{key}'")
        self._registry[key] = declaration
        LOGGER.debug(f"Updated '{key}' -> {declaration!r}")

    def update_by_key(self, key: str, declaration: object) -> None:
        if key not in self._registry:
            LOGGER.warning(f"Updating unregistered key '{key}'")
        self._registry[key] = declaration
        LOGGER.debug(f"Updated '{key}' -> {declaration!r}")

    def reference(self, namespace: str, typename: str) -> "DeclarationReference":
        """Create a Reference pointing to the given namespace::typename key."""
        key = CtdDeclarationManager.make_key(namespace, typename)
        return DeclarationReference(self, key)

    def contains(self, namespace: str, typename: str) -> bool:
        return CtdDeclarationManager.make_key(namespace, typename) in self._registry


class DeclarationReference(Generic[T]):
    """A reference cell backed by a CtdDeclarationManager key.

    When the manager entry is updated (alias erasure), all holders of this
    reference automatically see the new value via the .value property.
    """

    def __init__(self, manager: CtdDeclarationManager, key: str) -> None:
        self._manager = manager
        self._key = key

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, new_key: str) -> None:
        self._key = new_key

    @property
    def value(self) -> T:
        return self._manager.get_by_key(self._key)  # type: ignore[return-value]

    @value.setter
    def value(self, declaration: T) -> None:
        self._manager.update_by_key(self._key, declaration)

    def __str__(self) -> str:
        v = self.value
        return str(v) if v is not None else f"<unresolved:{self._key}>"

    def __repr__(self) -> str:
        return f"DeclarationReference({self._key!r})"


class DirectReference(Generic[T]):
    """A reference cell holding a value directly (not via a registry key).

    Used for anonymous structural types (Pointer, Array) and builtins
    that are not registered in the manager.
    """

    def __init__(self, declaration: T) -> None:
        self._value = declaration
        self._key = ""

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, new_key: str) -> None:
        self._key = new_key

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, declaration: T) -> None:
        self._value = declaration

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"DirectReference({self._value!r})"
