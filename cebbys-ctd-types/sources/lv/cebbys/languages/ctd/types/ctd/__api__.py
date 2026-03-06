from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from typing import Any, TypeVar, Protocol, runtime_checkable, Union

T = TypeVar("T", default=Any)

__all__ = ["Reference", "Referable"]


@runtime_checkable
class Reference(Protocol[T]):
    """Mutable reference cell pointing to a Declaration.

    Implementations may hold a registry key (resolved lazily) or a direct
    value. The .value property always returns the current target.
    """
    value: T
    key: str

Referable = Union[Reference, Declaration]