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

                    # TODO implement the rest of Ctd.* parsing
