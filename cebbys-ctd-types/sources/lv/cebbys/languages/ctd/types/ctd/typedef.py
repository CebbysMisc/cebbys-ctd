from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import TypedefMeta
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
    )

class Typedef(Declaration):
    """Represents a typedef declaration."""
    decorators: list[Decorator]
    signed: bool|None
    base: Reference

    def __init__(
        self,
        namespace: "Namespace",
        meta: "TypedefMeta"
    ) -> None: 
        super().__init__(namespace, meta)
        self.decorators = []
        self.signed = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} ({self.base})"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Typedef({self.namespace.path}::{self.name})"