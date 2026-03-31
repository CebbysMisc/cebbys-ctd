from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import (
    StructureMemberMeta,
    StructureMeta
)
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
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


class Structure(Declaration[StructureMeta]):
    """Represents a structure declaration."""
    base: Reference | None
    members: list[StructureMember]

    def __init__(
        self,
        namespace: "Namespace",
        meta: "StructureMeta",
        decorators: list[Decorator] | None = None,
    ) -> None:
        super().__init__(namespace, meta, decorators)
        self.members = []
        self.base = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Structure({self.namespace.path}::{self.name})"
