"""Flag Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['FlagMemberMeta', 'FlagMeta']


class FlagMemberMeta:
    """Metadata for a flag member."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

    def __init__(self, name: str, value: int | None = None):
        """Initialize flag member metadata.

        Args:
            name: The member identifier
            value: Optional explicit hex value (e.g., 0x20)
        """
        self._name: str
        self._value: int | None

        self._name = name
        self._value = value

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def value(self) -> int | None:
        """Get the member value (if explicitly set)."""
        return self._value


class FlagMeta:
    """Metadata for a flag declaration.

    Flags are similar to enums but with bit-shifted values:
    - First member starts at 0x1 (1)
    - Each subsequent member is bit-shifted: 0x2, 0x4, 0x8, etc.
    - Manual offsets can be specified (e.g., BGRA_SUPPORT = 0x20)
    - After a manual offset, bit-shifting continues from that value
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        members: list[FlagMemberMeta] | None = None
    ):
        """Initialize flag metadata.

        Args:
            name: The flag identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of flag members
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._base_type: str | None
        self._members: list[FlagMemberMeta]

        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = members if members is not None else []

    @property
    def name(self) -> str:
        """Get the flag name."""
        return self._name

    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace

    @property
    def base_type(self) -> str | None:
        """Get the base type."""
        return self._base_type

    @property
    def members(self) -> list[FlagMemberMeta]:
        """Get the flag members."""
        return self._members
