from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta


class Interface(Declaration):
    """Represents an interface declaration."""
    decorators: list[Decorator]
    base: Reference | None
    methods: list[Function]
    meta: InterfaceMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
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
