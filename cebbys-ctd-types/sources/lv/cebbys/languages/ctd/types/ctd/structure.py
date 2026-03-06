from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    StructureMemberMeta,
    StructureMeta
)

class StructureMember:
    """Represents a structure member."""
    name: str
    type_reference: Reference
    meta: StructureMemberMeta

    @property
    def type(self) -> Declaration:
        return self.type_reference.value

    @type.setter
    def type(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.type_reference = value
        else:
            self.type_reference.key = value.typeref

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"StructureMember({self.name!r}, {self.type!r})"


class Structure(Declaration):
    """Represents a structure declaration."""
    decorators: list[Decorator]
    base_reference: Reference | None
    members: list[StructureMember]
    meta: StructureMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base_reference = None

    @property
    def base(self) -> Declaration | None:
        return self.base_reference.value if self.base_reference is not None else None

    @base.setter
    def base(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.base_reference = value
        else:
            self.base_reference.key = value.typeref

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Structure({self.namespace.path}::{self.name})"
