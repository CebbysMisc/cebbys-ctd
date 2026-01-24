"""Typedef Definition Module"""
import lv.cebbys.languages.ctd.define.__api__ as Api

__all__ = ['TypedefDefinition']


class TypedefDefinition(Api.BaseDefinition):
    """Resolved typedef definition."""

    def __init__(self, name: str, namespace: str, type_spec: Api.TypeSpec | None = None):
        """Initialize typedef definition.

        Args:
            name: Typedef name
            namespace: Namespace path
            type_spec: Resolved type specification (can be set later via set_type_spec)
        """
        self._name: str
        self._namespace: str
        self._type_spec: Api.TypeSpec | None

        self._name = name
        self._namespace = namespace
        self._type_spec = type_spec

    def set_type_spec(self, type_spec: Api.TypeSpec) -> None:
        """Set the type specification (for deferred resolution).

        Args:
            type_spec: The resolved type specification
        """
        self._type_spec = type_spec

    @property
    def name(self) -> str:
        """Get the typedef name."""
        return self._name

    @property
    def namespace(self) -> str:
        """Get the namespace."""
        return self._namespace

    @property
    def qualified_name(self) -> str:
        """Get the fully qualified name."""
        return f"{self._namespace}::{self._name}"

    @property
    def type_spec(self) -> Api.TypeSpec:
        """Get the type specification."""
        if self._type_spec is None:
            raise RuntimeError(
                f"Type spec not yet resolved for {self.qualified_name}")
        return self._type_spec

    def __repr__(self) -> str:
        """String representation."""
        return f"TypedefDefinition({self.qualified_name} = {self._type_spec})"
