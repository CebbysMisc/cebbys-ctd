from collections.abc import Callable
from enum import (
    Enum,
    auto,
)
from typing import Any, Callable

class AutoPropertyMode(Enum):
    GETSET = auto()
    GET = auto()
    SET = auto()

class AutoProperty(property):
    def __init__(
        self,
        fget: Callable[[Any], Any] | None = None,
        fset: Callable[[Any, Any], None] | None = None,
        fdel: Callable[[Any], None] | None = None,
        doc: str | None = None
    ) -> None:
        super().__init__(self._getter(fget), fset, fdel, doc)

    def _getter(self, fget: Callable[[Any], Any]|None = None) -> Callable[[Any], Any]|None:
        if fget is None:
            return None
        else:
            def wrap(*args: Any):
                return fget(*args)
            return wrap