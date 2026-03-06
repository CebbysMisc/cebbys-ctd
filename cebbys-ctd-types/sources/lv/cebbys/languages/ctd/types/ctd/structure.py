from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import IReference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    StructureMemberMeta,
    StructureMeta
)

class StructureMember:
    """Represents a structure member."""
    name: str
    _type: IReference
    meta: StructureMemberMeta

    @property
    def type(self) -> Declaration:
        return self._type.value if self._type is not None else None

    @type.setter
    def type(self, value) -> None:
        if isinstance(value, IReference):
            self._type = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._type = DirectReference(value)

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"StructureMember({self.name!r}, {self.type!r})"


class Structure(Declaration):
    """Represents a structure declaration."""
    decorators: list[Decorator]
    _base: IReference | None
    members: list[StructureMember]
    meta: StructureMeta

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
        if isinstance(value, IReference):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Structure({self.namespace.path}::{self.name})"
