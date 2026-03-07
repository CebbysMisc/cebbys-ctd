from lv.cebbys.languages.ctd.resolver.linker.function import (
    FunctionLinker
)
from lv.cebbys.languages.ctd.resolver.linker.__api__ import (
    resolve_typespec_in_namespace
)
from lv.cebbys.languages.ctd.utility.logging import (
    get_logger
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
    Interface,
    Function
)
LOGGER = get_logger(__name__)

__all__ = ["InterfaceLinker"]


class InterfaceLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Interface,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec_in_namespace(declaration.meta.base_type, namespace)

        for method_meta in declaration.meta.methods:
            method = Function()
            method.meta = method_meta
            method.name = method_meta.name
            FunctionLinker.link(namespace, method)
            declaration.methods.append(method)

        LOGGER.debug(f"{declaration}")
