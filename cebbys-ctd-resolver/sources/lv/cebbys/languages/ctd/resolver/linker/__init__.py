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
    def link(modules: dict[str, Ctd.Module]) -> None:
        resolver = TypespecResolverApi()

        # Pass 1: wire includes and link all typedefs/aliases first so
        # the resolver can safely erase aliases in pass 2.
        for _, module in modules.items():
            module.includes = [modules[i.path] for i in module.meta.includes]
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    if isinstance(declaration, (Ctd.Typedef, Ctd.Alias)):
                        getattr(type(declaration), LINK)(resolver, module, namespace, declaration)

        # Pass 2: link remaining declaration types (aliases already resolved).
        for _, module in modules.items():
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    if not isinstance(declaration, (Ctd.Typedef, Ctd.Alias)):
                        getattr(type(declaration), LINK)(resolver, module, namespace, declaration)
