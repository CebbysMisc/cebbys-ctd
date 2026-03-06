import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec, resolve_integer_range, next_flag_value
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["FlagLinker"]


class FlagLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Flag,
        manager: CtdDeclarationManager,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec(resolver, module, namespace, declaration.meta.base_type)

        int_range: tuple[int, int] | None = resolve_integer_range(declaration.base) if declaration.base else None

        next_offset: int = 1  # flags auto-index as powers of 2, starting at 2^0
        for member_meta in declaration.meta.members:
            member = Ctd.FlagMember()
            member.name = member_meta.name
            member.offset = member_meta.value if member_meta.value is not None else next_offset
            next_offset = next_flag_value(member.offset)
            if int_range is not None and not (int_range[0] <= member.offset <= int_range[1]):
                raise ValueError(
                    f"Flag member '{declaration.name}::{member.name}' value {member.offset} "
                    f"is out of range [{int_range[0]}, {int_range[1]}] for base type '{declaration.base}'"
                )
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.debug(f"{declaration}")
