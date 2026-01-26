"""CTD Define API

This module contains base classes and common types for resolved definitions.
"""
import abc as Abc

__all__ = [
    'BaseDefinition',
    'BaseType',
    'PrimitiveType',
    'TypeReference',
    'TypeSpec',
]


class BaseDefinition(Abc.ABC):
    """Abstract base class for all type definitions."""

    @property
    @Abc.abstractmethod
    def name(self) -> str:
        """Get the definition name."""
        pass

    @property
    @Abc.abstractmethod
    def namespace(self) -> str:
        """Get the namespace."""
        pass

    @property
    @Abc.abstractmethod
    def qualified_name(self) -> str:
        """Get the fully qualified name."""
        pass


class BaseType(Abc.ABC):
    """Abstract base class for all type representations."""

    @Abc.abstractmethod
    def __repr__(self) -> str:
        """String representation."""
        pass


class PrimitiveType(BaseType):
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


class TypeReference(BaseType):
    """Reference to another type definition."""

    def __init__(self, target: BaseDefinition):
        """Initialize type reference.

        Args:
            target: The referenced type definition
        """
        self._target: BaseDefinition
        self._target = target

    @property
    def target(self) -> BaseDefinition:
        """Get the referenced type."""
        return self._target

    def __repr__(self) -> str:
        """String representation."""
        return f"TypeReference({self._target.qualified_name})"


class TypeSpec:
    """Type specification with optional pointer modifier."""

    def __init__(
        self,
        base_type: BaseType,
        is_pointer: bool = False
    ):
        """Initialize type specification.

        Args:
            base_type: The base type (primitive or reference)
            is_pointer: Whether this is a pointer type
        """
        self._base_type: BaseType
        self._is_pointer: bool

        self._base_type = base_type
        self._is_pointer = is_pointer

    @property
    def base_type(self) -> BaseType:
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
