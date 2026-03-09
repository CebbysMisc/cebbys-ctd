from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from typing import Any
empty: Any = None

class BuiltinMeta:
    def __init__(self, name: str) -> None:
        self.name = name

class Builtin(Declaration):
    """Represents a builtin member."""

    def __init__(self, name:str) -> None:
        super().__init__(empty, BuiltinMeta(name))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Builtin({self.name!r})"
    
    @property
    def typeref(self):
        return self.name
    


class Array(Declaration):
    def __init__(self, base: Reference, size: int) -> None:
        super().__init__(empty, empty)
        self.base = base
        self.size = size

    def __str__(self) -> str:
        return f"{self.base}[{self.size}]"

    def __repr__(self) -> str:
        return f"Array({self.base!r}, {self.size})"
    
    @property
    def typeref(self):
        return f"{self.base.key}[{self.size}]"

class Pointer(Declaration):
    def __init__(self, base: Reference) -> None:
        super().__init__(empty, empty)
        self.base = base

    def __str__(self) -> str:
        return f"{self.base}*"

    def __repr__(self) -> str:
        return f"Pointer({self.base!r})"
    
    @property
    def typeref(self):
        return f"{self.base.key}*"