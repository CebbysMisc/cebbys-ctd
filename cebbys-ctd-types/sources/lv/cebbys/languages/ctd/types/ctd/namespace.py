from typing import TYPE_CHECKING

from lv.cebbys.languages.ctd.types.meta import NamespaceMeta

if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
    from lv.cebbys.languages.ctd.types.ctd.module import Module


class Namespace:
    declarations: "list[Declaration]"
    _meta: NamespaceMeta

    def __init__(
        self,
        module: "Module",
        meta: NamespaceMeta
    ) -> None:
        self._module = module
        self._meta = meta

        self.declarations = []

    @property
    def module(self):
        return self._module

    @property
    def path(self):
        """
        Namespace path, e.g. "foo::bar::baz".
        String elements are separated by "::" and represent nested namespaces.
        """
        return self._meta.path

    @property
    def meta(self):
        return self._meta

    @property
    def source(self) -> str:
        ctx = self._meta.ctx
        stream = ctx.start.getInputStream()
        return stream.getText(ctx.start.start, ctx.stop.stop)

    def __str__(self) -> str:
        return f"{self.path} {{ {len(self.declarations)} declarations }}"

    def __repr__(self) -> str:
        return f"Namespace({self.path!r})"
