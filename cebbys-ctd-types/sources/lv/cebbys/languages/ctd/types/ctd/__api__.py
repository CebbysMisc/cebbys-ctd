from typing import Any, TypeVar, Protocol, runtime_checkable

T = TypeVar("T", default=Any)

__all__ = ["Reference"]


@runtime_checkable
class Reference(Protocol[T]):
    """Mutable reference cell pointing to a Declaration.

    Implementations may hold a registry key (resolved lazily) or a direct
    value. The .value property always returns the current target.
    """

    @property
    def value(self) -> T: ...

    @value.setter
    def value(self, declaration: T) -> None: ...
