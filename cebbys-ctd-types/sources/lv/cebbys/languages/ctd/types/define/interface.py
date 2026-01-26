import lv.cebbys.languages.ctd.types.define.function as FunctionModule
import lv.cebbys.languages.ctd.types.define.__api__ as Api

__all__ = ['InterfaceDefinition']


class InterfaceDefinition(Api.BaseDefinition):
    """Resolved structure definition."""

    def __init__(
        self,
        name: str,
        namespace: str
    ):
        """Initialize interface definition.

        Args:
            name: Interface name
            namespace: Namespace path
            members: List of interface members (can be set later)
        """
        self._name: str
        self._namespace: str
        self._members: tuple[FunctionModule.FunctionDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._members = ()

    def set_members(self, members: list[FunctionModule.FunctionDefinition]) -> None:
        """Set the members (for deferred resolution).

        Args:
            members: List of resolved interface members
        """
        self._members = tuple(members)

    @property
    def name(self):
        """Get the interface name."""
        return self._name

    @property
    def namespace(self):
        """Get the namespace."""
        return self._namespace

    @property
    def qualified_name(self):
        """Get the fully qualified name."""
        return f"{self._namespace}::{self._name}"

    @property
    def members(self):
        """Get the structure members (immutable)."""
        return self._members

    def __repr__(self) -> str:
        """String representation."""
        return f"InterfaceDefinition({self.qualified_name})"
