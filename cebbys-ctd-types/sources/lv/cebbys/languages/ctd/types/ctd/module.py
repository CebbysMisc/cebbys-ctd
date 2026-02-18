from lv.cebbys.languages.ctd.types.ctd.namespace import Namespace
from lv.cebbys.languages.ctd.types.meta import ModuleMeta

class Module:
    namespaces: list[Namespace]
    includes: 'list[Module]'
    meta: ModuleMeta
    name: str

    def __str__(self) -> str:
        out = f"// module \"{self.name}\"\n\n"
        out += "\n".join([f"include \"{i.name}\"" for i in self.includes])
        return out