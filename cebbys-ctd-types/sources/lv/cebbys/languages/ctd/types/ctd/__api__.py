from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration


class Reference:
    key: "str"

    @property
    def value(self) -> "Declaration": ...