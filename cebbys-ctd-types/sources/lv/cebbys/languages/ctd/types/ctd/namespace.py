from typing import TYPE_CHECKING

from lv.cebbys.languages.ctd.types.meta import NamespaceMeta

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration


class Namespace:
    declarations: list["Declaration"]
    meta: NamespaceMeta
    path: str

    def __str__(self) -> str:
        return f"{self.path} {{ {len(self.declarations)} declarations }}"

    def __repr__(self) -> str:
        return f"Namespace({self.path!r})"