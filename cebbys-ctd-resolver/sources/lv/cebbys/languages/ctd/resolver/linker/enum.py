import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi
from lv.cebbys.languages.ctd.resolver.linker.__api__ import resolve_typespec, resolve_integer_range
from lv.cebbys.languages.ctd.resolver.manager import CtdDeclarationManager

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = ["EnumLinker"]


class EnumLinker:
    @staticmethod
    def link(
        resolver: TypespecResolverApi,
        module: Ctd.Module,
        namespace: Ctd.Namespace,
        declaration: Ctd.Enum,
        manager: CtdDeclarationManager,
    ) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = resolve_typespec(resolver, module, namespace, declaration.meta.base_type)

        int_range: tuple[int, int] | None = resolve_integer_range(declaration.base) if declaration.base else None

        next_value: int = 0
        for member_meta in declaration.meta.members:
            member = Ctd.EnumMember()
            member.name = member_meta.name
            member.value = member_meta.value if member_meta.value is not None else next_value
            next_value = member.value + 1
            if int_range is not None and not (int_range[0] <= member.value <= int_range[1]):
                raise ValueError(
                    f"Enum member '{declaration.name}::{member.name}' value {member.value} "
                    f"is out of range [{int_range[0]}, {int_range[1]}] for base type '{declaration.base}'"
                )
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.debug(f"{declaration}")
