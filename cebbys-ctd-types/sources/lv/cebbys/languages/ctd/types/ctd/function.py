from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)


class Parameter:
    """Represents a function parameter."""
    meta: ParameterMeta
    type: Reference
    name: str

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"Parameter({self.name!r}, {self.type!r})"


class Function(Declaration[FunctionMeta]):
    """Represents a function declaration."""
    return_type: Reference | None
    decorators: list[Decorator]
    parameters: list[Parameter]

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.parameters = []
        self.base = None

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
