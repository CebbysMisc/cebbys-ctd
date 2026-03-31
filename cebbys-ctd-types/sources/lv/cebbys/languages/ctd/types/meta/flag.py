"""Flag Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['FlagMemberMeta', 'FlagMeta']


class FlagMemberMeta:
    """Metadata for a flag member.

    Flag members represent individual bit flags within a flag declaration.
    Members use bit-shifted values (0x1, 0x2, 0x4, 0x8, etc.) by default,
    or can specify explicit hex values. After an explicit value, bit-shifting
    continues from that position.

    Examples:
    ```
        SINGLETHREADED              // 0x1 (auto bit-shift)
        DEBUG                       // 0x2 (auto bit-shift)
        BGRA_SUPPORT = 0x20         // Explicit value
        DEBUGGABLE                  // 0x40 (continues from 0x20)
    ```
    """

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


class FlagMeta(Api.DeclarationMeta):
    """Metadata for a flag declaration.

    Flags are similar to enums but with bit-shifted values.
    The first member starts at 0x1, and each subsequent member is bit-shifted
    (0x2, 0x4, 0x8, etc.). Manual offsets can be specified, after which
    bit-shifting continues from that value.

    Examples:
    ```
        flag CreateDeviceFlag : Unt4 {
            SINGLETHREADED
            DEBUG
            SWITCH_TO_REF
            BGRA_SUPPORT = 0x20
            DEBUGGABLE
            VIDEO_SUPPORT
        }
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: Api.TypespecMeta | None = None,
        members: list[FlagMemberMeta] = [],
        decorators: list[Api.DecoratorMeta] = [],
        ctx=None
    ):
        """Initialize flag metadata.

        Args:
            name: The flag identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of flag members
            decorators: List of decorators
            ctx: ANTLR4 parse context
        """
        super().__init__(namespace, name, decorators, ctx)
        self._base_type = base_type
        self._members = list(members)

    @property
    def base_type(self) -> Api.TypespecMeta | None:
        """Get the base type."""
        return self._base_type

    @property
    def members(self) -> list[FlagMemberMeta]:
        """Get the flag members."""
        return list(self._members)
