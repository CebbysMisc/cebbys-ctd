"""Enum Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['EnumMemberMeta', 'EnumMeta']


class EnumMemberMeta:
    """Metadata for an enum member.

    Enum members represent individual named values within an enum declaration.
    Members can have explicit integer values or use auto-increment starting from 0.

    Examples:
    ```
        UNKNOWN                 // Auto-increment value
        HARDWARE                // Next auto-increment value
        LEVEL_9_1  = 0x9100     // Explicit hex value
        LEVEL_10_0 = 0xa000     // Explicit hex value
    ```
    """

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


class EnumMeta(Api.DeclarationMeta):
    """Metadata for an enum declaration.

    Enums provide metadata for enumerated types with named integer constants.
    An enum can optionally specify a base type and contains one or more members.
    Members use sequential integer values starting from 0 unless explicit values are provided.

    Examples:
    ```
        enum DriverType : Int4 {
            UNKNOWN
            HARDWARE
            REFERENCE
        }

        enum FeatureLevel : Unt4 {
            LEVEL_9_1  = 0x9100
            LEVEL_10_0 = 0xa000
            LEVEL_11_0 = 0xb000
        }
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        members: list[EnumMemberMeta] = [],
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize enum metadata.

        Args:
            name: The enum identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of enum members
            decorators: List of decorators
        """
        super().__init__(namespace, name, decorators)
        self._base_type = base_type
        self._members = list(members)

    @property
    def base_type(self) -> str | None:
        """Get the base type."""
        return self._base_type

    @property
    def members(self) -> list[EnumMemberMeta]:
        """Get the enum members."""
        return list(self._members)
