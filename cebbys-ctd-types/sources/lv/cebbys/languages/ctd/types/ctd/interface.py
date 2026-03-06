from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta


class Interface(Declaration):
    """Represents an interface declaration."""
    decorators: list[Decorator]
    _base: Reference | None
    methods: list[Function]
    meta: InterfaceMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self._base = None
        self.methods = []

    @property
    def base(self) -> Declaration | None:
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
            base = f" : {self.base}" if self.base else ""
            return f"{self.namespace.path}::{self.name}{base} {{ {len(self.methods)} methods }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Interface({self.namespace.path}::{self.name})"
