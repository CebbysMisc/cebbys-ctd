"""Definition Collection Meta Module"""
from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar
)
from lv.cebbys.languages.ctd.types.meta.namespace import (
    NamespaceMeta
)
from lv.cebbys.languages.ctd.types.meta.include import (
    IncludeMeta
)
from pathlib import (
    Path
)


__all__ = ['ModuleMeta']


ModuleDeclarationContext = CtdGrammar.ModuleDeclarationContext


class ModuleMeta:
    # TODO: Add code comments as TypedefMeta

    def __init__(self):
        self._namespaces: list[NamespaceMeta] = []
        self._includes: list[IncludeMeta] = []
        self.path: Path
        self.root: Path
        self.name: str
        self.ctx: ModuleDeclarationContext

    @property
    def namespaces(self):
        return tuple(self._namespaces)

    @property
    def includes(self):
        return tuple(self._includes)

    def add_namespace(self, value: NamespaceMeta) -> None:
        self._namespaces.append(value)

    def add_include(self, value: IncludeMeta) -> None:
        self._includes.append(value)
