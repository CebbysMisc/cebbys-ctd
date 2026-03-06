from typing import TypeVar, Generic, Protocol, runtime_checkable

T = TypeVar("T")

__all__ = ["IReference"]


@runtime_checkable
class IReference(Protocol[T]):
    """Interface for a mutable reference cell pointing to a Declaration.

    Implementations may hold a registry key (resolved lazily) or a direct
    value. The .value property always returns the current target.
    """

    @property
    def value(self) -> T: ...

    @value.setter
    def value(self, declaration: T) -> None: ...
