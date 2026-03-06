import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.typedef import TypedefLinker
from lv.cebbys.languages.ctd.resolver.linker.alias import AliasLinker
from lv.cebbys.languages.ctd.resolver.linker.enum import EnumLinker
from lv.cebbys.languages.ctd.resolver.linker.flag import FlagLinker
from lv.cebbys.languages.ctd.resolver.linker.structure import StructureLinker
from lv.cebbys.languages.ctd.resolver.linker.function import FunctionLinker
from lv.cebbys.languages.ctd.resolver.linker.interface import InterfaceLinker
from typing import (
    Protocol,
    Any
)
from uuid import (
    uuid4
)
__all__ = ["ModuleLinker"]



class DeclarationLinker(Protocol):
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Any
    ) -> None: ...

LINK = f"link-{uuid4()}"

def register_linkers():
    linker_registry: dict[type[Ctd.Declaration], type[DeclarationLinker]] = {
        Ctd.Interface: InterfaceLinker,
        Ctd.Structure: StructureLinker,
        Ctd.Function: FunctionLinker,
        Ctd.Typedef: TypedefLinker,
        Ctd.Alias: AliasLinker,
        Ctd.Enum: EnumLinker,
        Ctd.Flag: FlagLinker
    }
    for ctd, linker in linker_registry.items():
        setattr(ctd, LINK, linker.link)

register_linkers()

class ModuleLinker:
    @staticmethod
    def link_all(modules: dict[str, Ctd.Module]) -> None:
        resolver = TypespecResolverApi()
        for _, module in modules.items():
            module.includes = [modules[i.path] for i in module.meta.includes]
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    getattr(type(declaration), LINK)(resolver, module, namespace, declaration)
