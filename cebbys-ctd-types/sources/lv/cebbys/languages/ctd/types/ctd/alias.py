from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import AliasMeta


class Alias(Declaration[AliasMeta]):
    """Represents an alias declaration."""
    base_reference:Reference
    decorators: list[Decorator]
    meta: AliasMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []

    @property
    def base(self) -> Declaration:
        return self.base_reference.value

    @base.setter
    def base(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.base_reference = value
        else:
            self.base_reference.key = value.typeref

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} -> {self.base}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Alias({self.namespace.path}::{self.name})"