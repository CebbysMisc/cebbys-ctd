import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.constructor import (
    ModuleConstructor
)
from lv.cebbys.languages.ctd.resolver.linker import (
    ModuleLinker
)
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


class CtdMetaResolver:
    @staticmethod
    def resolve(module_tree: dict[str, Meta.ModuleMeta]):
        manager: CtdDeclarationManager = CtdDeclarationManager()
        modules: dict[str, Ctd.Module] = {}

        for name, module_meta in module_tree.items():
            LOGGER.debug(f"Constructing module '{name}'")
            modules[name] = ModuleConstructor.construct(name, module_meta, manager)

        ModuleLinker.link(modules, manager)
        for module in modules.values():
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    yield declaration
        