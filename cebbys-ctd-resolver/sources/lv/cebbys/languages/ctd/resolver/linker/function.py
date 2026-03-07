from lv.cebbys.languages.ctd.resolver.linker.__api__ import (
    resolve_typespec_in_namespace
)
from lv.cebbys.languages.ctd.utility.logging import (
    get_logger
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
    Parameter,
    Function
)
LOGGER = get_logger(__name__)

__all__ = ["FunctionLinker"]


class FunctionLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Function,
    ) -> None:
        declaration.return_type = resolve_typespec_in_namespace(declaration.meta.return_type, namespace)

        for param_meta in declaration.meta.parameters:
            param = Parameter()
            param.name = param_meta.name
            param.type = resolve_typespec_in_namespace(param_meta.type_spec, namespace)
            param.meta = param_meta
            declaration.parameters.append(param)

        LOGGER.debug(f"{declaration}")
