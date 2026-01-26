"""Structure Definition Module"""
import typing as Typing
import lv.cebbys.languages.ctd.types.define.__api__ as Api

__all__ = ['StructureMemberDefinition', 'StructureDefinition']


class StructureMemberDefinition:
    """Resolved structure member definition."""

    def __init__(self, name: str, type_spec: Api.TypeSpec):
        """Initialize structure member.

        Args:
            name: Member name
            type_spec: Resolved type specification
        """
        self._name: str
        self._type_spec: Api.TypeSpec

        self._name = name
        self._type_spec = type_spec

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def type_spec(self) -> Api.TypeSpec:
        """Get the member type specification."""
        return self._type_spec

    def __repr__(self) -> str:
        """String representation."""
        return f"StructureMember({self._type_spec} {self._name})"


class StructureDefinition(Api.BaseDefinition):
    """Resolved structure definition."""

    def __init__(
        self,
        name: str,
        namespace: str,
        members: list[StructureMemberDefinition] | None = None
    ):
        """Initialize structure definition.

        Args:
            name: Structure name
            namespace: Namespace path
            members: List of structure members (can be set later)
        """
        self._name: str
        self._namespace: str
        self._members: tuple[StructureMemberDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._members = tuple(members) if members is not None else ()

    def set_members(self, members: list[StructureMemberDefinition]) -> None:
        """Set the members (for deferred resolution).

        Args:
            members: List of resolved structure members
        """
        self._members = tuple(members)

    @property
    def name(self) -> str:
        """Get the structure name."""
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
    def members(self) -> Typing.Sequence[StructureMemberDefinition]:
        """Get the structure members (immutable)."""
        return self._members

    def __repr__(self) -> str:
        """String representation."""
        return f"StructureDefinition({self.qualified_name})"
