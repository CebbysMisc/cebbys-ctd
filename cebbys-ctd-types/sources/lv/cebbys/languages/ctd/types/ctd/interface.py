from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta


class Interface(Declaration):
    """Represents an interface declaration."""
    decorators: list[Decorator]
    base_reference: Reference | None
    methods: list[Function]
    meta: InterfaceMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.base_reference = None
        self.methods = []

    @property
    def base(self) -> Declaration | None:
        return self.base_reference.value if self.base_reference is not None else None

    @base.setter
    def base(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.base_reference = value
        else:
            self.base_reference.key = value.typeref

    def __str__(self) -> str:
        try:
            base = f" : {self.base}" if self.base else ""
            return f"{self.namespace.path}::{self.name}{base} {{ {len(self.methods)} methods }}"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Interface({self.namespace.path}::{self.name})"
