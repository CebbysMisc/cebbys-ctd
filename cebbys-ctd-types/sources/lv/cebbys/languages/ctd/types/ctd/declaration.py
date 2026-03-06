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
    namespace: "Namespace"
    meta: "M"
    name: "str"

    @property
    def typeref(self) -> str:
        return f"{self.namespace.path}::{self.name}"