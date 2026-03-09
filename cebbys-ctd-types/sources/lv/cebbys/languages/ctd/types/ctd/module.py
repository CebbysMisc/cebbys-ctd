from typing import (
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.namespace import (
        Namespace
    )
    from lv.cebbys.languages.ctd.types.meta import (
        ModuleMeta
    )
    # from lv.cebbys.languages.ctd.types.ctd.__api__ import (
    #     Ref as Reference
    # )

class Module:
    def __init__(self, meta: "ModuleMeta") -> None:
        self._meta = meta
        self.namespaces: "list[Namespace]" = []
        self.includes: "list[Module]" = []

    @property
    def meta(self):
        return self._meta
    
    @property
    def name(self):
        return self.meta.name

    def __str__(self) -> "str":
        out = f"// module \"{self.name}\"\n\n"
        out += "\n".join([f"include \"{i.name}\"" for i in self.includes])
        return out
    
    def __repr__(self) -> "str":
        return f"Module[{self.name}]"