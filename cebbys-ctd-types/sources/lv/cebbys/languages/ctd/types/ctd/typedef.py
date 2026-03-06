from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.types.meta import TypedefMeta


class Typedef(Declaration):
    """Represents a typedef declaration."""
    decorators: list[Decorator]
    signed: bool|None
    base: Reference
    meta: TypedefMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.signed = None

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} ({self.base})"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Typedef({self.namespace.path}::{self.name})"