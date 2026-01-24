"""Interface Meta Module"""
from __future__ import annotations
import typing as Typing

if Typing.TYPE_CHECKING:
    import lv.cebbys.languages.ctd.meta.loader.function as FunctionModule

import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['InterfaceMeta']


class InterfaceMeta:
    """Metadata for an interface declaration."""

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        methods: list[FunctionModule.FunctionMeta] | None = None
    ):
        """Initialize interface metadata.

        Args:
            name: The interface identifier
            namespace: Qualified namespace path
            methods: List of interface method definitions
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._methods: list[FunctionModule.FunctionMeta]

        self._name = name
        self._namespace = namespace
        self._methods = methods if methods is not None else []

    @property
    def name(self) -> str:
        """Get the interface name."""
        return self._name

    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace

    @property
    def methods(self) -> list[FunctionModule.FunctionMeta]:
        """Get the interface methods."""
        return self._methods
