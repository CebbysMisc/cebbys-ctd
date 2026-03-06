from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference, Referable
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)


class Parameter:
    """Represents a function parameter."""
    meta: ParameterMeta
    type_reference: Reference
    name: str
    decorators: list[Decorator]

    def __init__(self) -> None:
        self.decorators = []

    @property
    def type(self) -> Declaration:
        return self.type_reference.value

    @type.setter
    def type(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.type_reference = value
        else:
            self.type_reference.key = value.typeref

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"Parameter({self.name!r}, {self.type!r})"


class Function(Declaration[FunctionMeta]):
    """Represents a function declaration."""
    return_type_reference: Reference | None
    decorators: list[Decorator]
    parameters: list[Parameter]

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.parameters = []
        self.return_type_reference = None

    @property
    def return_type(self) -> Declaration | None:
        return self.return_type_reference.value if self.return_type_reference is not None else None

    @return_type.setter
    def return_type(self, value: Referable) -> None:
        if isinstance(value, Reference):
            self.return_type_reference = value
        else:
            self.return_type_reference.key = value.typeref

    def __str__(self) -> str:
        try:
            params = ", ".join(str(p) for p in self.parameters)
            ns = getattr(self, "namespace", None)
            prefix = f"{ns.path}::" if ns else ""
            return f"{self.return_type} {prefix}{self.name}({params})"
        except:
            return f"Function({self.name})"

    def __repr__(self) -> str:
        return f"Function({self.namespace.path}::{self.name})"
