from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration



class Ref[T]:
    key: "str"

    @property
    def value(self) -> "T": ...

class Reference(Ref["Declaration"]):
    ...