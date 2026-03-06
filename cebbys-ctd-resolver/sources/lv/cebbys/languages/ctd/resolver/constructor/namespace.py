import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.utility.logging as Logging
from lv.cebbys.languages.ctd.resolver.constructor.declaration import DeclarationConstructor
from lv.cebbys.languages.ctd.resolver.manager import (
    CtdDeclarationStorage
)

logger = Logging.get_logger(__name__)


class NamespaceConstructor:
    @staticmethod
    def construct(meta: Meta.NamespaceMeta) -> Ctd.Namespace:
        """Construct a CTD namespace from metadata.
        
        Args:
            meta: Namespace metadata to construct from
            
        Returns:
            Constructed namespace object
        """
        logger.trace(f"Constructing namespace: {meta.path}")
        
        out = Ctd.Namespace()
        out.path = meta.path
        out.meta = meta

        out.declarations = []
        for declaration_meta in meta.declarations:
            declaration = DeclarationConstructor.construct(declaration_meta)
            declaration.namespace = out
            out.declarations.append(declaration)
            CtdDeclarationStorage.register(declaration)

        logger.debug(f"Namespace '{meta.path}' constructed with {len(out.declarations)} declaration(s)")
        
        return out

