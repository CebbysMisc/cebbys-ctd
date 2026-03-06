import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["TypedefLinker"]


class TypedefLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Typedef,
        manager: CtdDeclarationManager,
    ) -> None:
        type_spec = declaration.meta.type_spec

        # Extract signed from the base TypedTypespecMeta before resolving
        base_spec = type_spec
        while isinstance(base_spec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            base_spec = base_spec.base
        if isinstance(base_spec, Meta.TypedTypespecMeta):
            declaration.signed = base_spec.signed

        declaration.base = resolve_typespec(resolver, module, namespace, type_spec)
        LOGGER.debug(f"{declaration}")
