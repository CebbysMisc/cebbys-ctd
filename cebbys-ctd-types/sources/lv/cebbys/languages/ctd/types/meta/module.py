"""Definition Collection Meta Module"""
import lv.cebbys.languages.ctd.types.meta.namespace as NamespaceModule
import lv.cebbys.languages.ctd.types.meta.include as IncludeModule

__all__ = ['ModuleMeta']


class ModuleMeta:
    # TODO: Add code comments as TypedefMeta

    def __init__(self):
        self._namespaces: list[NamespaceModule.NamespaceMeta] = []
        self._includes: list[IncludeModule.IncludeMeta] = []

    @property
    def namespaces(self):
        return tuple(self._namespaces)

    @property
    def includes(self):
        return tuple(self._includes)

    def add_namespace(self, value: NamespaceModule.NamespaceMeta) -> None:
        self._namespaces.append(value)

    def add_include(self, value: IncludeModule.IncludeMeta) -> None:
        self._includes.append(value)
