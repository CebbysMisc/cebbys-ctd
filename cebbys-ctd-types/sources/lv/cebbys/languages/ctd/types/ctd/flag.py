from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
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
    base: Reference | None

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} : {self.base} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Flag({self.namespace.path}::{self.name})"
