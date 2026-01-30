"""CTD Meta API

This module contains common types for metadata classes.
"""
import lv.cebbys.languages.ctd.types.__api__ as Api

__all__ = ['ModulePath', 'Meta', 'DecoratorMeta', 'DecoratableMeta', 'DeclarationMeta']

# Re-export ModulePath for use in meta classes
ModulePath = Api.ModulePath


class Meta:
    """Metadata base type."""

    def __init__(self, namespace: ModulePath, name: str) -> None:
        """Initialize metadata basetype.

        Args:
            namespace: Qualified namespace path
            name: The metadata basetype name
        """
        self._namespace = namespace
        self._name = name

    @property
    def namespace(self):
        """Get the namespace."""
        return self._namespace

    @property
    def name(self):
        """Get the alias name."""
        return self._name


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
        arguments: list[str] = []
    ):
        """Initialize decorator metadata.

        Args:
            name: The decorator name (e.g., "WinApi", "Nullable")
            arguments: List of argument values as strings
        """
        self._name = name
        self._arguments = tuple(arguments)

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


class DecoratableMeta(Meta):
    """Metadata base type with decorator support."""

    def __init__(self, namespace: str, name: str, decorators: list[DecoratorMeta] = []) -> None:
        """Initialize decoratable metadata basetype.

        Args:
            namespace: Qualified namespace path
            name: The metadata basetype name
            decorators: List of decorators (e.g., @Nullable)
        """
        super().__init__(namespace, name)
        self._decorators = tuple(decorators)

    @property
    def decorators(self) -> tuple[DecoratorMeta, ...]:
        return self._decorators


class DeclarationMeta(DecoratableMeta):
    ...
