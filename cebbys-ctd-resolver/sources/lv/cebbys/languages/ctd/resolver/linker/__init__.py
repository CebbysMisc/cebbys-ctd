import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from lv.cebbys.languages.ctd.resolver.linker.resolver import TypespecResolverApi

import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


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

        next_value: int = 0
        for member_meta in declaration.meta.members:
            member = Ctd.EnumMember()
            member.name = member_meta.name
            member.value = member_meta.value if member_meta.value is not None else next_value
            next_value = member.value + 1
            member.meta = member_meta
            declaration.members.append(member)

        LOGGER.warning(f"{declaration}")

    def _link_flag(self, module: Ctd.Module, namespace: Ctd.Namespace, declaration: Ctd.Flag) -> None:
        if declaration.meta.base_type is not None:
            declaration.base = self._resolve_typespec(module, namespace, declaration.meta.base_type)

        next_offset: int = 0
        for member_meta in declaration.meta.members:
            member = Ctd.FlagMember()
            member.name = member_meta.name
            member.offset = member_meta.value if member_meta.value is not None else next_offset
            next_offset = member.offset + 1
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
