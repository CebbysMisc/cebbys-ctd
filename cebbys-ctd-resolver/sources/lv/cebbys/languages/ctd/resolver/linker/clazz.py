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
    ClassMember,
    Namespace,
    Class,
)

LOGGER = get_logger(__name__)

__all__ = ["ClassLinker"]


class ClassLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Class,
    ) -> None:
        # Resolve all base type references
        for base_typespec in declaration.meta.bases:
            declaration.bases.append(resolve_typespec_in_namespace(base_typespec, namespace))

        # Resolve each member's type
        for member_meta in declaration.meta.members:
            member = ClassMember()
            member.name = member_meta.name
            member.type = resolve_typespec_in_namespace(member_meta.type_spec, namespace)
            member.meta = member_meta
            declaration.members.append(member)

        # Link each method (same as InterfaceLinker delegates to FunctionLinker)
        for method in declaration.methods:
            FunctionLinker.link(namespace, method)

        LOGGER.debug(f"{declaration}")
