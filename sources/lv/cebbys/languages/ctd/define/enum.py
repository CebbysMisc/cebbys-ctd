"""Enum Definition Module"""
import typing as Typing
import lv.cebbys.languages.ctd.define.__api__ as Api

__all__ = ['EnumMemberDefinition', 'EnumDefinition']


class EnumMemberDefinition:
    """Resolved enum member definition."""

    def __init__(self, name: str, value: int):
        """Initialize enum member.

        Args:
            name: Member name
            value: Member value (resolved)
        """
        self._name: str
        self._value: int

        self._name = name
        self._value = value

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def value(self) -> int:
        """Get the member value."""
        return self._value

    def __repr__(self) -> str:
        """String representation."""
        return f"EnumMember({self._name} = {self._value})"


class EnumDefinition(Api.BaseDefinition):
    """Resolved enum definition."""

    def __init__(
        self,
        name: str,
        namespace: str,
        base_type: Api.TypeSpec | None = None,
        members: list[EnumMemberDefinition] | None = None
    ):
        """Initialize enum definition.

        Args:
            name: Enum name
            namespace: Namespace path
            base_type: Optional resolved base type (can be set later)
            members: List of enum members (can be set later)
        """
        self._name: str
        self._namespace: str
        self._base_type: Api.TypeSpec | None
        self._members: tuple[EnumMemberDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = tuple(members) if members is not None else ()

    def set_base_type(self, base_type: Api.TypeSpec | None) -> None:
        """Set the base type (for deferred resolution).

        Args:
            base_type: The resolved base type
        """
        self._base_type = base_type

    def set_members(self, members: list[EnumMemberDefinition]) -> None:
        """Set the members (for deferred resolution).

        Args:
            members: List of resolved enum members
        """
        self._members = tuple(members)

    @property
    def name(self) -> str:
        """Get the enum name."""
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
    def base_type(self) -> Api.TypeSpec | None:
        """Get the base type."""
        return self._base_type

    @property
    def members(self) -> Typing.Sequence[EnumMemberDefinition]:
        """Get the enum members (immutable)."""
        return self._members

    def __repr__(self) -> str:
        """String representation."""
        base = f" : {self._base_type}" if self._base_type else ""
        return f"EnumDefinition({self.qualified_name}{base})"
