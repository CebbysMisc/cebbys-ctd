from lv.cebbys.languages.ctd.resolver.linker.__api__ import (
    resolve_typespec_in_namespace
)
from lv.cebbys.languages.ctd.utility.logging import (
    get_logger
)
from lv.cebbys.languages.ctd.types.meta import (
    PointerTypespecMeta,
    ArrayTypespecMeta,
    TypedTypespecMeta
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
    Typedef
)
LOGGER = get_logger(__name__)

__all__ = ["TypedefLinker"]


class TypedefLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Typedef,
    ) -> None:
        type_spec = declaration.meta.type_spec

        # Extract signed from the base TypedTypespecMeta before resolving
        base_spec = type_spec
        while isinstance(base_spec, (ArrayTypespecMeta, PointerTypespecMeta)):
            base_spec = base_spec.base
        if isinstance(base_spec, TypedTypespecMeta):
            declaration.signed = base_spec.signed

        declaration.base = resolve_typespec_in_namespace(type_spec, namespace)
        LOGGER.debug(f"{declaration}")
