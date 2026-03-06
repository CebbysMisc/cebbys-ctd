import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)

# Builtin C type name → bit width
_BUILTIN_BITS: dict[str, int] = {
    "char":  8,
    "short": 16,
    "int":   32,
    "long":  64,
}


def _resolve_integer_range(decl: Ctd.Declaration) -> tuple[int, int] | None:
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


def _next_flag_value(prev: int) -> int:
    """Return the smallest power of 2 strictly greater than prev."""
    if prev < 0:
        return 1
    return 1 << prev.bit_length()


class ModuleLinker:
    def __init__(self, modules: dict[str, Ctd.Module]) -> None:
        self._resolver = TypespecResolverApi()
        self.modules = modules

    def _resolve_typespec(self, module: Ctd.Module, namespace: Ctd.Namespace, typespec: Meta.TypespecMeta) -> Ctd.Declaration:
        results = self._resolver.resolve(module, namespace, typespec)
        if not results:
            raise BaseException(f"Type '{typespec}' not found in module '{module.name}'")
        if len(results) > 1:
            LOGGER.warning(f"Ambiguous type '{typespec}': {len(results)} matches found, using first")
        return results[0]

    def _link_typedef(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Typedef) -> None:
        type_spec = declaration.meta.type_spec

        # Extract signed from the base TypedTypespecMeta before resolving
        base_spec = type_spec
        while isinstance(base_spec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
            base_spec = base_spec.base
        if isinstance(base_spec, Meta.TypedTypespecMeta):
            declaration.signed = base_spec.signed

        declaration.base = self._resolve_typespec(module, namespace, type_spec)
        LOGGER.warning(f"{declaration}")

    def _link_alias(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Alias) -> None:
        declaration.base = self._resolve_typespec(module, namespace, declaration.meta.type_spec)
        LOGGER.warning(f"{declaration}")

    def _link_enum(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Enum) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = self._resolve_typespec(module, namespace, declaration.meta.base_type)

        int_range: tuple[int, int] | None = _resolve_integer_range(declaration.base) if declaration.base else None

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

        LOGGER.warning(f"{declaration}")

    def _link_flag(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Flag) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = self._resolve_typespec(module, namespace, declaration.meta.base_type)

        int_range: tuple[int, int] | None = _resolve_integer_range(declaration.base) if declaration.base else None

        next_offset: int = 1  # flags auto-index as powers of 2, starting at 2^0
        for member_meta in declaration.meta.members:
            member = Ctd.FlagMember()
            member.name = member_meta.name
            member.offset = member_meta.value if member_meta.value is not None else next_offset
            next_offset = _next_flag_value(member.offset)
            if int_range is not None and not (int_range[0] <= member.offset <= int_range[1]):
                raise ValueError(
                    f"Flag member '{declaration.name}::{member.name}' value {member.offset} "
                    f"is out of range [{int_range[0]}, {int_range[1]}] for base type '{declaration.base}'"
                )
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.warning(f"{declaration}")

    def _link_structure(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Structure) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = self._resolve_typespec(module, namespace, declaration.meta.base_type)

        for member_meta in declaration.meta.members:
            member = Ctd.StructureMember()
            member.name = member_meta.name
            member.type = self._resolve_typespec(module, namespace, member_meta.type_spec)
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.warning(f"{declaration}")

    def _link_function(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Function) -> None:
        declaration.return_type = self._resolve_typespec(module, namespace, declaration.meta.return_type)

        for param_meta in declaration.meta.parameters:
            param = Ctd.Parameter()
            param.name = param_meta.name
            param.type = self._resolve_typespec(module, namespace, param_meta.type_spec)
            param.meta = param_meta
            declaration.parameters.append(param)

        LOGGER.warning(f"{declaration}")

    def _link_interface(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Interface) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = self._resolve_typespec(module, namespace, declaration.meta.base_type)

        for method_meta in declaration.meta.methods:
            method = Ctd.Function()
            method.meta = method_meta
            method.name = method_meta.name
            method.return_type = self._resolve_typespec(module, namespace, method_meta.return_type)
            for param_meta in method_meta.parameters:
                param = Ctd.Parameter()
                param.name = param_meta.name
                param.type = self._resolve_typespec(module, namespace, param_meta.type_spec)
                param.meta = param_meta
                method.parameters.append(param)
            declaration.methods.append(method)

        LOGGER.warning(f"{declaration}")

    @staticmethod
    def link(modules: dict[str, Ctd.Module]):
        instance = ModuleLinker(modules)

        for _, module in modules.items():
            module.includes = [ modules[i.path] for i in module.meta.includes ]
            for namespace in module.namespaces:
                for declaration in namespace.declarations:
                    if isinstance(declaration, Ctd.Typedef):
                        instance._link_typedef(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Alias):
                        instance._link_alias(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Enum):
                        instance._link_enum(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Flag):
                        instance._link_flag(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Structure):
                        instance._link_structure(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Function):
                        instance._link_function(module, namespace, declaration)

                    elif isinstance(declaration, Ctd.Interface):
                        instance._link_interface(module, namespace, declaration)
