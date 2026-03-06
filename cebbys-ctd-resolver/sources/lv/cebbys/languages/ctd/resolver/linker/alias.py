import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["AliasLinker"]


class AliasLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Alias,
    ) -> None:
        declaration.base = resolve_typespec(resolver, module, namespace, declaration.meta.type_spec)
        LOGGER.debug(f"{declaration}")
