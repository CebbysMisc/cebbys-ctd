from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import IReference
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
    _base: IReference | None

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
            return f"{self.namespace.path}::{self.name} : {self.base} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Enum({self.namespace.path}::{self.name})"
