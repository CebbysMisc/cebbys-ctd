from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    FlagMemberMeta,
    FlagMeta
)


class FlagMember:
    """Represents a flag member."""
    name: str
    offset: int
    meta: FlagMemberMeta

    def __str__(self) -> str:
        return f"{self.name} = {self.offset}"

    def __repr__(self) -> str:
        return f"FlagMember({self.name!r}, {self.offset!r})"


class Flag(Declaration[FlagMeta]):
    """Represents a flag declaration."""
    decorators: list[Decorator]
    members: list[FlagMember]
    _base: Reference | None

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self._base = None

    @property
    def base(self) -> Declaration | None:
        return self._base.value if self._base is not None else None

    @base.setter
    def base(self, value) -> None:
        if isinstance(value, Reference):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} : {self.base} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Flag({self.namespace.path}::{self.name})"
