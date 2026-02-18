from typing import TYPE_CHECKING

from lv.cebbys.languages.ctd.types.meta import NamespaceMeta

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration


class Namespace:
    declarations: list["Declaration"]
    meta: NamespaceMeta
    path: str