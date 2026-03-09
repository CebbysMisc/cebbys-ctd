import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
from lv.cebbys.languages.ctd.resolver.constructor.declaration import DeclarationConstructor
from lv.cebbys.languages.ctd.resolver.manager import (
    CtdDeclarationStorage
)

from lv.cebbys.languages.ctd.types.meta import (
    NamespaceMeta
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
    Module,
)

logger = Logging.get_logger(__name__)


class NamespaceConstructor:
    @staticmethod
    def construct(module: Module, meta:NamespaceMeta) -> Namespace:
        """Construct a CTD namespace from metadata.
        
        Args:
            meta: Namespace metadata to construct from
            
        Returns:
            Constructed namespace object
        """
        logger.trace(f"Constructing namespace: {meta.path}")
        
        namespace = Ctd.Namespace(module, meta)

        namespace.declarations = []
        for declaration_meta in meta.declarations:
            declaration = DeclarationConstructor.construct(namespace, declaration_meta)
            namespace.declarations.append(declaration)
            CtdDeclarationStorage.register(declaration)

        logger.debug(f"Namespace '{meta.path}' constructed with {len(namespace.declarations)} declaration(s)")
        
        return namespace