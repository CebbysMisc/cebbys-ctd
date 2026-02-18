from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)


class Parameter:
    """Represents a function parameter."""
    meta: ParameterMeta
    type: Declaration
    name: str


class Function(Declaration[FunctionMeta]):
    """Represents a function declaration."""
    return_type: Declaration | None
    decorators: list[Decorator]
    parameters: list[Parameter]

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.parameters = []
        self.base = None
