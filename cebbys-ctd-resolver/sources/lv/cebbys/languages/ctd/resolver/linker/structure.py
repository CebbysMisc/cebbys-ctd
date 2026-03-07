from lv.cebbys.languages.ctd.resolver.linker.__api__ import (
    resolve_typespec_in_namespace
)
from lv.cebbys.languages.ctd.utility.logging import (
    get_logger
)
from lv.cebbys.languages.ctd.types.ctd import (
    StructureMember,
    Namespace,
    Structure
)
LOGGER = get_logger(__name__)

__all__ = ["StructureLinker"]


class StructureLinker:
    @staticmethod
    def link(
        namespace: Namespace,
        declaration: Structure,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec_in_namespace(declaration.meta.base_type, namespace)

        for member_meta in declaration.meta.members:
            member = StructureMember()
            member.name = member_meta.name
            member.type = resolve_typespec_in_namespace(member_meta.type_spec, namespace)
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.debug(f"{declaration}")
