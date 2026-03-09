from lv.cebbys.languages.ctd.types.ctd.declaration import (
    Declaration
)
from lv.cebbys.languages.ctd.types.ctd.decorator import (
    Decorator
)
from lv.cebbys.languages.ctd.types.ctd.__api__ import (
    Reference
)
from lv.cebbys.languages.ctd.types.meta import (
    AliasMeta
)
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
    )

class Alias(Declaration[AliasMeta]):
    """Represents an alias declaration."""
    decorators: list[Decorator]
    base: Reference

    def __init__(
        self,
        namespace: "Namespace",
        meta: "AliasMeta"
    ) -> None:
        super().__init__(namespace, meta)
        self.decorators = []

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} -> {self.base}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Alias({self.namespace.path}::{self.name})"