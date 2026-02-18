from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.meta import NamespaceMeta


class Namespace:
    declarations: list[Declaration]
    meta: NamespaceMeta
    path: str