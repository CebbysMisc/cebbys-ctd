from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import (
    StructureMemberMeta,
    StructureMeta
)

class StructureMember:
    """Represents a structure member."""
    name: str
    type: Reference
    meta: StructureMemberMeta

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"StructureMember({self.name!r}, {self.type!r})"


class Structure(Declaration):
    """Represents a structure declaration."""
    decorators: list[Decorator]
    base: Reference | None
    members: list[StructureMember]
    meta: StructureMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Structure({self.namespace.path}::{self.name})"
