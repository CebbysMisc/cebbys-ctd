from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
    )

class Interface(Declaration[InterfaceMeta]):
    """Represents an interface declaration."""
    base: Reference | None
    methods: list[Function]

    def __init__(
        self,
        namespace: "Namespace",
        meta: "InterfaceMeta",
        decorators: list[Decorator] | None = None,
    ) -> None:
        super().__init__(namespace, meta, decorators)
        self.base = None
        self.methods = []

    def __str__(self) -> str:
        try:
            base = f" : {self.base}" if self.base else ""
            return f"{self.namespace.path}::{self.name}{base} {{ {len(self.methods)} methods }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Interface({self.namespace.path}::{self.name})"
