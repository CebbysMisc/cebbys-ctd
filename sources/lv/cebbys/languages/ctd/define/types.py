"""CTD Resolved Definitions

This module contains resolved definition classes where all type references
point to actual type instances.
"""
import typing as Typing
import types as Types

__all__ = [
    'PrimitiveType',
    'TypeReference',
    'TypeSpec',
    'TypedefDefinition',
    'EnumMemberDefinition',
    'EnumDefinition',
    'DefinitionCollection'
]


class PrimitiveType:
    """Represents a primitive type (char, short, int, long, void)."""

    def __init__(self, name: str, signed: bool | None = None):
        """Initialize primitive type.

        Args:
            name: Primitive type name (char, short, int, long, void)
            signed: True for signed, False for unsigned, None for default
        """
        self._name: str
        self._signed: bool | None

        self._name = name
        self._signed = signed

    @property
    def name(self) -> str:
        """Get the primitive type name."""
        return self._name

    @property
    def signed(self) -> bool | None:
        """Get the sign modifier (True=signed, False=unsigned, None=default)."""
        return self._signed

    def __repr__(self) -> str:
        """String representation."""
        sign = ""
        if self._signed is True:
            sign = "signed "
        elif self._signed is False:
            sign = "unsigned "
        return f"PrimitiveType({sign}{self._name})"


class TypeReference:
    """Reference to another type definition."""

    def __init__(self, target: 'TypedefDefinition | EnumDefinition | FlagDefinition'):
        """Initialize type reference.

        Args:
            target: The referenced type definition
        """
        self._target: TypedefDefinition | EnumDefinition | FlagDefinition
        self._target = target

    @property
    def target(self) -> 'TypedefDefinition | EnumDefinition | FlagDefinition':
        """Get the referenced type."""
        return self._target

    def __repr__(self) -> str:
        """String representation."""
        return f"TypeReference({self._target.qualified_name})"


class TypeSpec:
    """Type specification with optional pointer modifier."""

    def __init__(
        self,
        base_type: PrimitiveType | TypeReference,
        is_pointer: bool = False
    ):
        """Initialize type specification.

        Args:
            base_type: The base type (primitive or reference)
            is_pointer: Whether this is a pointer type
        """
        self._base_type: PrimitiveType | TypeReference
        self._is_pointer: bool

        self._base_type = base_type
        self._is_pointer = is_pointer

    @property
    def base_type(self) -> PrimitiveType | TypeReference:
        """Get the base type."""
        return self._base_type

    @property
    def is_pointer(self) -> bool:
        """Check if this is a pointer type."""
        return self._is_pointer

    def __repr__(self) -> str:
        """String representation."""
        ptr = " *" if self._is_pointer else ""
        return f"TypeSpec({self._base_type}{ptr})"


class TypedefDefinition:
    """Resolved typedef definition."""

    def __init__(self, name: str, namespace: str, type_spec: TypeSpec | None = None):
        """Initialize typedef definition.

        Args:
            name: Typedef name
            namespace: Namespace path
            type_spec: Resolved type specification (can be set later via set_type_spec)
        """
        self._name: str
        self._namespace: str
        self._type_spec: TypeSpec | None

        self._name = name
        self._namespace = namespace
        self._type_spec = type_spec

    def set_type_spec(self, type_spec: TypeSpec) -> None:
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
    def type_spec(self) -> TypeSpec:
        """Get the type specification."""
        if self._type_spec is None:
            raise RuntimeError(
                f"Type spec not yet resolved for {self.qualified_name}")
        return self._type_spec

    def __repr__(self) -> str:
        """String representation."""
        return f"TypedefDefinition({self.qualified_name} = {self._type_spec})"


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


class EnumDefinition:
    """Resolved enum definition."""

    def __init__(
        self,
        name: str,
        namespace: str,
        base_type: TypeSpec | None = None,
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
        self._base_type: TypeSpec | None
        self._members: tuple[EnumMemberDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = tuple(members) if members is not None else ()

    def set_base_type(self, base_type: TypeSpec | None) -> None:
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
        self._members = members

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
    def base_type(self) -> TypeSpec | None:
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


class FlagDefinition:
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
        base_type: TypeSpec | None = None,
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
        self._base_type: TypeSpec | None
        self._members: tuple[FlagMemberDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = tuple(members) if members is not None else ()

    def set_base_type(self, base_type: TypeSpec | None) -> None:
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
        self._members = members

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
    def base_type(self) -> TypeSpec | None:
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


class DefinitionCollection:
    """Immutable collection of resolved type definitions."""

    def __init__(
        self,
        typedefs: dict[str, TypedefDefinition] | None = None,
        enums: dict[str, EnumDefinition] | None = None,
        flags: dict[str, FlagDefinition] | None = None
    ):
        """Initialize collection.

        Args:
            typedefs: Dictionary of typedefs indexed by qualified name
            enums: Dictionary of enums indexed by qualified name
            flags: Dictionary of flags indexed by qualified name
        """
        self._typedefs: Typing.Final[Types.MappingProxyType[str, TypedefDefinition]]
        self._enums: Typing.Final[Types.MappingProxyType[str, EnumDefinition]]
        self._flags: Typing.Final[Types.MappingProxyType[str, FlagDefinition]]
        
        # Create immutable copies using MappingProxyType
        self._typedefs = Types.MappingProxyType(
            typedefs if typedefs is not None else {})
        self._enums = Types.MappingProxyType(
            enums if enums is not None else {})
        self._flags = Types.MappingProxyType(
            flags if flags is not None else {})

    @property
    def typedefs(self) -> Typing.Mapping[str, TypedefDefinition]:
        """Get immutable view of typedefs indexed by qualified name."""
        return self._typedefs

    @property
    def enums(self) -> Typing.Mapping[str, EnumDefinition]:
        """Get immutable view of enums indexed by qualified name."""
        return self._enums

    @property
    def flags(self) -> Typing.Mapping[str, FlagDefinition]:
        """Get immutable view of flags indexed by qualified name."""
        return self._flags

    def find_type(self, qualified_name: str) -> TypedefDefinition | EnumDefinition | FlagDefinition | None:
        """Find a type by qualified name.

        Args:
            qualified_name: Fully qualified type name

        Returns:
            The type definition or None if not found
        """
        if qualified_name in self._typedefs:
            return self._typedefs[qualified_name]
        if qualified_name in self._enums:
            return self._enums[qualified_name]
        if qualified_name in self._flags:
            return self._flags[qualified_name]
        return None
