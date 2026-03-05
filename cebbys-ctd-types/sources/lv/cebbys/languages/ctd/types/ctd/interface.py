from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.function import Function
from lv.cebbys.languages.ctd.types.meta import InterfaceMeta


class Interface(Declaration):
    """Represents an interface declaration."""
    decorators: list[Decorator]
    base: Declaration | None
    methods: list[Function]
    meta: InterfaceMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.base = None
        self.methods = []
