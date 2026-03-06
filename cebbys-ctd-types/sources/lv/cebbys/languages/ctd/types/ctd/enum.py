from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    EnumMemberMeta,
    EnumMeta
)

class EnumMember:
    """Represents an enum member."""
    name: str
    value: int
    meta: EnumMemberMeta

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"

    def __repr__(self) -> str:
        return f"EnumMember({self.name!r}, {self.value!r})"


class Enum(Declaration[EnumMeta]):
    """Represents an enum declaration."""
    decorators: list[Decorator]
    members: list[EnumMember]
    base_reference: Reference | None

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
            return f"{self.namespace.path}::{self.name} : {self.base} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Enum({self.namespace.path}::{self.name})"
