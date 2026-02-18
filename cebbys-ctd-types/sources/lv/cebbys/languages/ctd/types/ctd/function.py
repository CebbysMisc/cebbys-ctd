from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    ParameterMeta,
    FunctionMeta
)


class Parameter:
    """Represents a function parameter."""
    name: str
    type: Declaration
    meta: ParameterMeta


class Function(Declaration):
    """Represents a function declaration."""
    decorators: list[Decorator]
    return_type: Declaration | None
    parameters: list[Parameter]
    meta: FunctionMeta
