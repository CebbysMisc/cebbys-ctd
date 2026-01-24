"""Decorator Definition Module"""

__all__ = ['DecoratorDefinition']


class DecoratorDefinition:
    """Resolved decorator definition.

    Decorators provide metadata for definitions and parameters.
    They can have optional arguments of various types.

    Examples:
        @WinApi
        @Nullable
        @Storage("reg", "ecx")
        @Offset(0x10)
    """

    def __init__(
        self,
        name: str,
        arguments: tuple[str, ...] | None = None
    ):
        """Initialize decorator definition.

        Args:
            name: The decorator name (e.g., "WinApi", "Nullable")
            arguments: Optional tuple of argument values as strings
        """
        self._name: str
        self._arguments: tuple[str, ...]

        self._name = name
        self._arguments = arguments if arguments is not None else ()

    @property
    def name(self) -> str:
        """Get the decorator name."""
        return self._name

    @property
    def arguments(self) -> tuple[str, ...]:
        """Get the decorator arguments (immutable)."""
        return self._arguments

    def __repr__(self) -> str:
        """String representation."""
        if self._arguments:
            args_str = ", ".join(self._arguments)
            return f"@{self._name}({args_str})"
        return f"@{self._name}"
