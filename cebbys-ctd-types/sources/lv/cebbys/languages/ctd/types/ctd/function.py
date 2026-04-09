from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Declaration,
        Namespace
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
    parameters: list[Parameter]

    def __init__(
        self,
        namespace: "Namespace",
        meta: "FunctionMeta",
        decorators: list[Decorator] | None = None,
        parent: "Declaration|None" = None
    ) -> None:
        super().__init__(namespace, meta, decorators)
        self.parameters = []
        self.base = None
        self._parent = parent

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

    @property
    def name(self) -> str:
        if self.parent:
            return f"{self.parent.name}_{self.meta.name}"
        else:
            return self.meta.name

    @property
    def namespace(self):
        if self.parent:
            return self.parent.namespace
        else:
            return super().namespace

    @property
    def parent(self):
        return self._parent
