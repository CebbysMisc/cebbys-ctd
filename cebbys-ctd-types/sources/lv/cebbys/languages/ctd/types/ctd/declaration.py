from typing import (
    TYPE_CHECKING,
    Generic,
    TypeVar,
    Any
)
from lv.cebbys.languages.ctd.types.meta import DeclarationMeta

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import Namespace

M = TypeVar("M", bound=DeclarationMeta, default=Any)


class Declaration(Generic[M]):

    def __init__(
        self,
        namespace: "Namespace",
        meta: "M"
    ) -> None:
        super().__init__()
        if namespace:
            self._namespace = namespace
        if meta:
            self._meta = meta

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

    def hash(self) -> int:
        return hash(self.typeref)
