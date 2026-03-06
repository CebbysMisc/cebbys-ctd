import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

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
        manager: CtdDeclarationManager,
    ) -> None:
        ref = resolve_typespec(resolver, module, namespace, declaration.meta.type_spec)
        declaration.base = ref
        # Erase alias in manager: all DeclarationReferences pointing to this alias key
        # will now transparently return the resolved base type.
        manager.update(namespace.path, declaration.name, ref.value)
        LOGGER.debug(f"{declaration}")
