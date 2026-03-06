from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import IReference

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
    _base: IReference

    def __init__(self, base, size: int) -> None:
        super().__init__()
        self.size = size
        self.base = base  # use setter

    @property
    def base(self) -> Declaration:
        return self._base.value if self._base is not None else None

    @base.setter
    def base(self, value) -> None:
        if isinstance(value, IReference):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        return f"{self.base}[{self.size}]"

    def __repr__(self) -> str:
        return f"Array({self.base!r}, {self.size})"

class Pointer(Declaration):
    _base: IReference

    def __init__(self, base) -> None:
        super().__init__()
        self.base = base  # use setter

    @property
    def base(self) -> Declaration:
        return self._base.value if self._base is not None else None

    @base.setter
    def base(self, value) -> None:
        if isinstance(value, IReference):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        return f"{self.base}*"

    def __repr__(self) -> str:
        return f"Pointer({self.base!r})"