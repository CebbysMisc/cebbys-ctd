from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import ClassMemberMeta, ClassMeta
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
    )


class ClassMember:
    """Represents a class member (property/attribute)."""
    name: str
    type: Reference
    meta: ClassMemberMeta

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"ClassMember({self.name!r}, {self.type!r})"


class Class(Declaration[ClassMeta]):
    """Represents a class declaration combining structure members and interface methods."""
    bases: list[Reference]
    members: list[ClassMember]
    methods: list[Function]

    def __init__(
        self,
        namespace: "Namespace",
        meta: "ClassMeta",
        decorators: list[Decorator] | None = None,
    ) -> None:
        super().__init__(namespace, meta, decorators)
        self.bases = []
        self.members = []
        self.methods = []

    def __str__(self) -> str:
        try:
            base_str = f" : {', '.join(str(b) for b in self.bases)}" if self.bases else ""
            return (
                f"{self.namespace.path}::{self.name}{base_str} "
                f"{{ {len(self.members)} members, {len(self.methods)} methods }}"
            )
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Class({self.namespace.path}::{self.name})"
