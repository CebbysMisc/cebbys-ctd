from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable

class Builtin(Declaration):
    """Represents a builtin member."""

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Builtin({self.name!r})"

class Array(Declaration):
    base_reference: Reference

    def __init__(self, base: Referable, size: int) -> None:
        super().__init__()
        self.size = size
        self.base = base

    @property
    def base(self) -> Declaration:
        return self.base_reference.value

    @base.setter
    def base(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.base_reference = value
        else:
            self.base_reference.key = value.typeref

    def __str__(self) -> str:
        return f"{self.base}[{self.size}]"

    def __repr__(self) -> str:
        return f"Array({self.base!r}, {self.size})"

class Pointer(Declaration):
    base_reference: Reference

    def __init__(self, base: Referable) -> None:
        super().__init__()
        self.base = base

    @property
    def base(self) -> Declaration:
        return self.base_reference.value

    @base.setter
    def base(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.base_reference = value
        else:
            self.base_reference.key = value.typeref

    def __str__(self) -> str:
        return f"{self.base}*"

    def __repr__(self) -> str:
        return f"Pointer({self.base!r})"