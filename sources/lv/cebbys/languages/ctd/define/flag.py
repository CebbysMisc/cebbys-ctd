"""Flag Definition Module"""
import typing as Typing
import lv.cebbys.languages.ctd.define.__api__ as Api

__all__ = ['FlagMemberDefinition', 'FlagDefinition']


class FlagMemberDefinition:
    """Resolved flag member definition.

    Flags use bit-shifted values instead of sequential values.
    """

    def __init__(self, name: str, value: int):
        """Initialize flag member.

        Args:
            name: Member name
            value: Member value (bit-shifted, e.g., 0x1, 0x2, 0x4, 0x8, 0x20, etc.)
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
        return f"FlagMember({self._name} = 0x{self._value:X})"


class FlagDefinition(Api.BaseDefinition):
    """Resolved flag definition.

    Flags are similar to enums but use bit-shifted values:
    - First member: 0x1 (1)
    - Second member: 0x2 (2)
    - Third member: 0x4 (4)
    - etc.
    Manual offsets can be specified, and bit-shifting continues from there.
    """

    def __init__(
        self,
        name: str,
        namespace: str,
        base_type: Api.TypeSpec | None = None,
        members: list[FlagMemberDefinition] | None = None
    ):
        """Initialize flag definition.

        Args:
            name: Flag name
            namespace: Namespace path
            base_type: Optional resolved base type (can be set later)
            members: List of flag members (can be set later)
        """
        self._name: str
        self._namespace: str
        self._base_type: Api.TypeSpec | None
        self._members: tuple[FlagMemberDefinition, ...]

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

    def set_members(self, members: list[FlagMemberDefinition]) -> None:
        """Set the members (for deferred resolution).

        Args:
            members: List of resolved flag members
        """
        self._members = tuple(members)

    @property
    def name(self) -> str:
        """Get the flag name."""
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
    def members(self) -> Typing.Sequence[FlagMemberDefinition]:
        """Get the flag members (immutable)."""
        return self._members

    def __repr__(self) -> str:
        """String representation."""
        base = f" : {self._base_type}" if self._base_type else ""
        return f"FlagDefinition({self.qualified_name}{base})"
