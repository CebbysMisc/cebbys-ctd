import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.typedef import TypedefLinker
from lv.cebbys.languages.ctd.resolver.linker.alias import AliasLinker
from lv.cebbys.languages.ctd.resolver.linker.enum import EnumLinker
from lv.cebbys.languages.ctd.resolver.linker.flag import FlagLinker
from lv.cebbys.languages.ctd.resolver.linker.structure import StructureLinker
from lv.cebbys.languages.ctd.resolver.linker.function import FunctionLinker
from lv.cebbys.languages.ctd.resolver.linker.interface import InterfaceLinker
from lv.cebbys.languages.ctd.resolver.linker.clazz import ClassLinker
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
        Ctd.Flag: FlagLinker,
        Ctd.Class: ClassLinker,
    }
    for ctd, linker in linker_registry.items():
        setattr(ctd, LINK, linker.link)


register_linkers()


class ModuleLinker:
    @staticmethod
    def link_all(modules: dict[str, Ctd.Module]) -> None:
        try:
            for _, module in modules.items():
                module.includes = link_includes(module, modules)
                for namespace in module.namespaces:
                    for declaration in namespace.declarations:
                        getattr(type(declaration), LINK)(namespace, declaration)
        except BaseException as e:
            raise RuntimeError("Error during module linking stage") from e


def link_includes(module: Ctd.Module, modules: dict[str, Ctd.Module]):
    try:
        return [modules[i.path] for i in module.meta.includes]
    except BaseException as e:
        raise RuntimeError(f"Error linking includes for module '{module.name}'") from e
