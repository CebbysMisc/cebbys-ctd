from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import AliasMeta

class Alias(Declaration[AliasMeta]):
    """Represents an alias declaration."""
    decorators: list[Decorator]
    _base: Reference
    meta: AliasMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self._base = None

    @property
    def base(self) -> Declaration:
        return self._base.value if self._base is not None else None

    @base.setter
    def base(self, value) -> None:
        if isinstance(value, Reference):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} -> {self.base}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Alias({self.namespace.path}::{self.name})"