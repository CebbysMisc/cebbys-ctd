from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration

class Builtin(Declaration):
    """Represents a builtin member."""

    def __init__(self, name:str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Builtin({self.name!r})"

class Array(Declaration):
    def __init__(self, base: Declaration, size: int) -> None:
        super().__init__()
        self.base = base
        self.size = size

    def __str__(self) -> str:
        return f"{self.base}[{self.size}]"

    def __repr__(self) -> str:
        return f"Array({self.base!r}, {self.size})"

class Pointer(Declaration):
    def __init__(self, base: Declaration) -> None:
        super().__init__()
        self.base = base

    def __str__(self) -> str:
        return f"{self.base}*"

    def __repr__(self) -> str:
        return f"Pointer({self.base!r})"