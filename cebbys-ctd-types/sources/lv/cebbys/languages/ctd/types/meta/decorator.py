"""Decorator Meta Module"""

__all__ = ['DecoratorMeta']


class DecoratorMeta:
    """Metadata for a decorator.

    Decorators provide metadata for definitions and parameters.
    They can have optional arguments of various types (strings, integers, identifiers).

    Examples:
    ```
        @WinApi
        @Nullable
        @Storage("reg", "ecx")
        @Offset(0x10)
    ```
    """

    def __init__(
        self,
        name: str,
        arguments: list[str] | None = None
    ):
        """Initialize decorator metadata.

        Args:
            name: The decorator name (e.g., "WinApi", "Nullable")
            arguments: Optional list of argument values as strings
        """
        self._name: str
        self._arguments: tuple[str, ...]

        self._name = name
        self._arguments = tuple(arguments) if arguments is not None else ()

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
