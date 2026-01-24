"""Typedef Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['TypedefMeta']


class TypedefMeta:
    """Metadata for a typedef declaration."""

    def __init__(
        self,
        name: str,
        type_spec: str,
        namespace: Api.ModulePath
    ):
        """Initialize typedef metadata.

        Args:
            name: The typedef identifier
            type_spec: The type specification string
            namespace: Qualified namespace path
        """
        self._name: str
        self._type_spec: str
        self._namespace: Api.ModulePath

        self._name = name
        self._type_spec = type_spec
        self._namespace = namespace

    @property
    def name(self) -> str:
        """Get the typedef name."""
        return self._name

    @property
    def type_spec(self) -> str:
        """Get the type specification."""
        return self._type_spec

    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace
