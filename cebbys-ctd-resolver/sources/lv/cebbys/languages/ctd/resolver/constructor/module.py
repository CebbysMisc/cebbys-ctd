import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
from lv.cebbys.languages.ctd.resolver.constructor.namespace import (
    NamespaceConstructor
)
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

logger = Logging.get_logger(__name__)


def _declaration_key(namespace_path: str, declaration_name: str) -> str:
    return f"{namespace_path}::{declaration_name}"


class ModuleConstructor:
    @staticmethod
    def construct(name: str, meta: Meta.ModuleMeta, manager: CtdDeclarationManager) -> Ctd.Module:
        """Construct a CTD module from metadata and pre-register all named declarations.
        
        Args:
            name: Module name (typically the file path)
            meta: Module metadata to construct from
            manager: Declaration manager for pre-registration
            
        Returns:
            Constructed module object
        """
        logger.debug(f"Constructing module: {name}")
        
        out = Ctd.Module()
        out.meta = meta
        out.name = name
        out.includes = []
        out.namespaces = []

        for namespace_meta in meta.namespaces:
            namespace = NamespaceConstructor.construct(namespace_meta)
            out.namespaces.append(namespace)
            for declaration in namespace.declarations:
                key = _declaration_key(namespace_meta.path, declaration.name)
                manager.register(key, declaration)

        logger.info(f"Module '{name}' constructed with {len(out.namespaces)} namespace(s)")
        
        return out

