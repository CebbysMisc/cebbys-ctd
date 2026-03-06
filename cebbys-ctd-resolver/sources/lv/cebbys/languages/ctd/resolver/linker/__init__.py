import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.typedef import TypedefLinker
from lv.cebbys.languages.ctd.resolver.linker.alias import AliasLinker
from lv.cebbys.languages.ctd.resolver.linker.enum import EnumLinker
from lv.cebbys.languages.ctd.resolver.linker.flag import FlagLinker
from lv.cebbys.languages.ctd.resolver.linker.structure import StructureLinker
from lv.cebbys.languages.ctd.resolver.linker.function import FunctionLinker
from lv.cebbys.languages.ctd.resolver.linker.interface import InterfaceLinker

__all__ = ["ModuleLinker"]


class ModuleLinker:
    @staticmethod
    def link(modules: dict[str, Ctd.Module]) -> None:
        resolver = TypespecResolverApi()

        for _, module in modules.items():
            module.includes = [modules[i.path] for i in module.meta.includes]
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    if isinstance(declaration, Ctd.Typedef):
                        TypedefLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Alias):
                        AliasLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Enum):
                        EnumLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Flag):
                        FlagLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Structure):
                        StructureLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Function):
                        FunctionLinker.link(resolver, module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Interface):
                        InterfaceLinker.link(resolver, module, namespace, declaration)

