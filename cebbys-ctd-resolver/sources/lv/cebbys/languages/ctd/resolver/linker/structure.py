import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["StructureLinker"]


class StructureLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Structure,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec(resolver, module, namespace, declaration.meta.base_type)

        for member_meta in declaration.meta.members:
            member = Ctd.StructureMember()
            member.name = member_meta.name
            member.type = resolve_typespec(resolver, module, namespace, member_meta.type_spec)
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.debug(f"{declaration}")
