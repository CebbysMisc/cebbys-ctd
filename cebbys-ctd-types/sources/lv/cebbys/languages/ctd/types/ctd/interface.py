from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta


class Interface(Declaration):
    """Represents an interface declaration."""
    decorators: list[Decorator]
    base: Declaration | None
    meta: InterfaceMeta
