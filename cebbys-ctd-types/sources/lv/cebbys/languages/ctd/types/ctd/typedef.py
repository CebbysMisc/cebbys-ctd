from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.__api__ import IReference
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import TypedefMeta


class Typedef(Declaration):
    """Represents a typedef declaration."""
    decorators: list[Decorator]
    signed: bool | None
    _base: IReference
    meta: TypedefMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.signed = None
        self._base = None

    @property
    def base(self) -> Declaration:
        return self._base.value if self._base is not None else None

    @base.setter
    def base(self, value) -> None:
        from lv.cebbys.languages.ctd.types.ctd.__api__ import IReference as _IRef
        if isinstance(value, _IRef):
            self._base = value
        else:
            from lv.cebbys.languages.ctd.resolver.manager import DirectReference
            self._base = DirectReference(value)

    def __str__(self) -> str:
        try:
            return f"{self.namespace.path}::{self.name} ({self.base})"
        except:
            return f"{self.namespace.path}::{self.name}"

    def __repr__(self) -> str:
        return f"Typedef({self.namespace.path}::{self.name})"