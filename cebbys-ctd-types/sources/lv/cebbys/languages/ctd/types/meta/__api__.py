"""CTD Meta API

This module contains common types for metadata classes.
"""
import lv.cebbys.languages.ctd.types.__api__ as Api
from lv.cebbys.languages.ctd.types.meta.decorator import DecoratorMeta

__all__ = ['ModulePath', 'Meta', 'DecoratorMeta', 'DecoratableMeta']

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
