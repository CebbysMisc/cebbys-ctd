"""Enum Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['EnumMemberMeta', 'EnumMeta']


class EnumMemberMeta:
    """Metadata for an enum member."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

    def __init__(self, name: str, value: int | None = None):
        """Initialize enum member metadata.

        Args:
            name: The member identifier
            value: Optional explicit integer value
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


class EnumMeta:
    """Metadata for an enum declaration."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        members: list[EnumMemberMeta] | None = None
    ):
        """Initialize enum metadata.

        Args:
            name: The enum identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of enum members
        """
        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = members if members is not None else []

    @property
    def name(self) -> str:
        """Get the enum name."""
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
    def members(self) -> list[EnumMemberMeta]:
        """Get the enum members."""
        return self._members
