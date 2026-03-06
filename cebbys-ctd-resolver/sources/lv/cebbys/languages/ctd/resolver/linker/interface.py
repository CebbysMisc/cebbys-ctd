import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec

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
            declaration.base = resolve_typespec(resolver, module, namespace, declaration.meta.base_type)

        for method_meta in declaration.meta.methods:
            method = Ctd.Function()
            method.meta = method_meta
            method.name = method_meta.name
            method.return_type = resolve_typespec(resolver, module, namespace, method_meta.return_type)
            for param_meta in method_meta.parameters:
                param = Ctd.Parameter()
                param.name = param_meta.name
                param.type = resolve_typespec(resolver, module, namespace, param_meta.type_spec)
                param.meta = param_meta
                method.parameters.append(param)
            declaration.methods.append(method)

        LOGGER.debug(f"{declaration}")
