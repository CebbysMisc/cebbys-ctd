from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import (
    EnumMemberMeta,
    EnumMeta
)
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
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
    members: list[EnumMember]
    base: Reference | None

    def __init__(
        self,
        namespace: "Namespace",
        meta: "EnumMeta",
        decorators: list[Decorator] | None = None,
    ) -> None:
        super().__init__(namespace, meta, decorators)
        self.members = []
        self.base = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} : {self.base} {{ {len(self.members)} members }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Enum({self.namespace.path}::{self.name})"
