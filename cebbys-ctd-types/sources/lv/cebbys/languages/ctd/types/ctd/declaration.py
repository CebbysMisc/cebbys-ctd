from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import Namespace


class Declaration:
    namespace: "Namespace"
    name: str