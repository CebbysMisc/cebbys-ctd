import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec_in_namespace

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["FunctionLinker"]


class FunctionLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Function,
    ) -> None:
        declaration.return_type = resolve_typespec_in_namespace(declaration.meta.return_type, namespace)

        for param_meta in declaration.meta.parameters:
            param = Ctd.Parameter()
            param.name = param_meta.name
            param.type = resolve_typespec_in_namespace(param_meta.type_spec, namespace)
            param.meta = param_meta
            declaration.parameters.append(param)

        LOGGER.debug(f"{declaration}")
