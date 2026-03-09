import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
from lv.cebbys.languages.ctd.resolver.constructor.namespace import (
    NamespaceConstructor
)

logger = Logging.get_logger(__name__)


class ModuleConstructor:
    @staticmethod
    def construct(name: str, meta: Meta.ModuleMeta) -> Ctd.Module:
        """Construct a CTD module from metadata.
        
        Args:
            name: Module name (typically the file path)
            meta: Module metadata to construct from
            
        Returns:
            Constructed module object
        """
        logger.debug(f"Constructing module: {name}")
        
        module = Ctd.Module(meta)
        for namespace_meta in meta.namespaces:
            module.namespaces.append(NamespaceConstructor.construct(module, namespace_meta))

        logger.info(f"Module '{name}' constructed with {len(module.namespaces)} namespace(s)")
        
        return module

