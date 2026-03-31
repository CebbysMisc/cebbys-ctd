from typing import (
    TYPE_CHECKING,
    Generic,
    TypeVar,
    Any
)
from lv.cebbys.languages.ctd.types.meta import DeclarationMeta

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
    from lv.cebbys.languages.ctd.types.ctd.namespace import Namespace

M = TypeVar("M", bound=DeclarationMeta, default=Any)


class Declaration(Generic[M]):

    def __init__(
        self,
        namespace: "Namespace",
        meta: "M",
        decorators: "tuple[Decorator, ...] | list[Decorator] | None" = None,
    ) -> None:
        super().__init__()
        if namespace:
            self._namespace = namespace
        if meta:
            self._meta = meta
        self._decorators: "tuple[Decorator, ...]" = tuple(decorators) if decorators else ()

    @property
    def typeref(self):
        return f"{self.namespace.path}::{self.name}"

    @property
    def namespace(self):
        return self._namespace

    @property
    def meta(self):
        return self._meta

    @property
    def name(self):
        return self.meta.name

    @property
    def decorators(self) -> "tuple[Decorator, ...]":
        return self._decorators

    @property
    def source(self) -> str:
        ctx = self.meta.ctx
        stream = ctx.start.getInputStream()
        return stream.getText(ctx.start.start, ctx.stop.stop)

    def hash(self) -> int:
        return hash(self.typeref)
