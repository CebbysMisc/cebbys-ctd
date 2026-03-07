from lv.cebbys.languages.ctd.resolver.linker.__api__ import (
    resolve_typespec_in_namespace
)
from lv.cebbys.languages.ctd.utility.logging import (
    get_logger
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
    Alias
)
LOGGER = get_logger(__name__)

__all__ = ["AliasLinker"]


class AliasLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Alias,
    ) -> None:
        declaration.base = resolve_typespec_in_namespace(declaration.meta.type_spec, namespace)
        LOGGER.debug(f"{declaration}")
