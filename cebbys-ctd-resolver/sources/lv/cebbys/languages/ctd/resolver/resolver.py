import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.constructor import (
    ModuleConstructor
)
from lv.cebbys.languages.ctd.resolver.linker import (
    ModuleLinker
)

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


def _erase_aliases(modules: dict[str, Ctd.Module]) -> None:
    """Replace all Alias references with their resolved base types.

    Walks every declaration field that can hold a Declaration reference
    and follows any Alias chain to its terminal non-Alias type.
    Must be called after all declarations are fully linked.
    """
    def unwrap(decl: Ctd.Declaration) -> Ctd.Declaration:
        visited: set[int] = set()
        while isinstance(decl, Ctd.Alias):
            if id(decl) in visited:
                break
            visited.add(id(decl))
            decl = decl.base
        return decl

    for module in modules.values():
        for namespace in module.namespaces:
            for declaration in namespace.declarations:
                if isinstance(declaration, Ctd.Typedef):
                    declaration.base = unwrap(declaration.base)

                elif isinstance(declaration, (Ctd.Enum, Ctd.Flag)):
                    if declaration.base is not None:
                        declaration.base = unwrap(declaration.base)

                elif isinstance(declaration, Ctd.Structure):
                    if declaration.base is not None:
                        declaration.base = unwrap(declaration.base)
                    for member in declaration.members:
                        member.type = unwrap(member.type)

                elif isinstance(declaration, Ctd.Function):
                    if declaration.return_type is not None:
                        declaration.return_type = unwrap(declaration.return_type)
                    for param in declaration.parameters:
                        param.type = unwrap(param.type)

                elif isinstance(declaration, Ctd.Interface):
                    if declaration.base is not None:
                        declaration.base = unwrap(declaration.base)
                    for method in declaration.methods:
                        if method.return_type is not None:
                            method.return_type = unwrap(method.return_type)
                        for param in method.parameters:
                            param.type = unwrap(param.type)


class CtdMetaResolver:
    @staticmethod
    def resolve(module_tree: dict[str, Meta.ModuleMeta]):
        modules: dict[str, Ctd.Module] = {}

        for name, module_meta in module_tree.items():
            LOGGER.debug(f"Constructing module '{name}'")
            modules[name] = ModuleConstructor.construct(name, module_meta)

        ModuleLinker.link(modules)
        _erase_aliases(modules)

        return modules