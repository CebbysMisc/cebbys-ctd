from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)


class Parameter:
    """Represents a function parameter."""
    meta: ParameterMeta
    _type: Reference
    name: str
    decorators: list[Decorator]

    def __init__(self) -> None:
        self.decorators = []
        self._type = None

    @property
    def type(self) -> Declaration:
        return self._type.value if self._type is not None else None

    @type.setter
    def type(self, value) -> None:
        if isinstance(value, Reference):
            self._type = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._type = DirectReference(value)

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def __repr__(self) -> str:
        return f"Parameter({self.name!r}, {self.type!r})"


class Function(Declaration[FunctionMeta]):
    """Represents a function declaration."""
    _return_type: Reference | None
    decorators: list[Decorator]
    parameters: list[Parameter]

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.parameters = []
        self._return_type = None

    @property
    def return_type(self) -> Declaration | None:
        return self._return_type.value if self._return_type is not None else None

    @return_type.setter
    def return_type(self, value) -> None:
        if isinstance(value, Reference):
            self._return_type = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._return_type = DirectReference(value)

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
