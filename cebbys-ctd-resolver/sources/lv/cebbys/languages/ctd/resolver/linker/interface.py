import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec_in_namespace
from lv.cebbys.languages.ctd.resolver.linker.function import FunctionLinker

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["InterfaceLinker"]


class InterfaceLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Interface,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec_in_namespace(declaration.meta.base_type, namespace)

        for method_meta in declaration.meta.methods:
            method = Ctd.Function()
            method.meta = method_meta
            method.name = method_meta.name
            FunctionLinker.link(resolver, module, namespace, method)
            declaration.methods.append(method)

        LOGGER.debug(f"{declaration}")
