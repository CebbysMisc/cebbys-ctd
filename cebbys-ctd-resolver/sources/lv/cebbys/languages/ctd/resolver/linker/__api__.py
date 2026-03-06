import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from lv.cebbys.languages.ctd.types.ctd.__api__ import Reference
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

__all__ = [
    "resolve_typespec",
    "resolve_integer_range",
    "next_flag_value",
]

# Builtin C type name → bit width
_BUILTIN_BITS: dict[str, int] = {
    "char":  8,
    "short": 16,
    "int":   32,
    "long":  64,
}


def resolve_typespec(
    resolver: TypespecResolverApi,
    module: Ctd.Module,
    namespace: Ctd.Namespace,
    typespec: Meta.TypespecMeta,
) -> Reference:
    results = resolver.resolve(module, namespace, typespec)
    if not results:
        raise BaseException(f"Type '{typespec}' not found in module '{module.name}'")
    if len(results) > 1:
        LOGGER.warning(f"Ambiguous type '{typespec}': {len(results)} matches found, using first")
    return results[0]


def resolve_integer_range(decl: Ctd.Declaration) -> tuple[int, int] | None:
    """Walk the type chain to determine the integer range of a declaration.

    Returns (min, max) inclusive, or None if the range cannot be determined.
    Signed info is taken from the first Typedef encountered in the chain.
    """
    visited: set[int] = set()
    current: Ctd.Declaration | None = decl
    signed: bool | None = None

    while current is not None:
        if id(current) in visited:
            break
        visited.add(id(current))

        if isinstance(current, Ctd.Builtin):
            bits = _BUILTIN_BITS.get(current.name)
            if bits is None:
                return None
            is_unsigned = (signed is False) if signed is not None else False
            if is_unsigned:
                return (0, (1 << bits) - 1)
            else:
                return (-(1 << (bits - 1)), (1 << (bits - 1)) - 1)

        if isinstance(current, Ctd.Typedef):
            if signed is None and current.signed is not None:
                signed = current.signed
            current = getattr(current, "base", None)
            continue

        if isinstance(current, Ctd.Alias):
            current = getattr(current, "base", None)
            continue

        break

    return None


def next_flag_value(prev: int) -> int:
    """Return the smallest power of 2 strictly greater than prev."""
    if prev < 0:
        return 1
    return 1 << prev.bit_length()
