"""Function Meta Module"""
from __future__ import annotations
import typing as Typing

if Typing.TYPE_CHECKING:
    import lv.cebbys.languages.ctd.meta.loader.decorator as DecoratorModule

import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['ParameterMeta', 'FunctionMeta']


class ParameterMeta:
    """Metadata for a function parameter."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

    def __init__(
        self,
        name: str,
        type_spec: str,
        decorators: list[DecoratorModule.DecoratorMeta] | None = None
    ):
        """Initialize parameter metadata.

        Args:
            name: The parameter identifier
            type_spec: The type specification string
            decorators: Optional list of decorators (e.g., @Nullable)
        """
        self._name: str
        self._type_spec: str
        self._decorators: tuple[DecoratorModule.DecoratorMeta, ...]

        self._name = name
        self._type_spec = type_spec
        self._decorators = tuple(decorators) if decorators is not None else ()

    @property
    def name(self) -> str:
        """Get the parameter name."""
        return self._name

    @property
    def type_spec(self) -> str:
        """Get the type specification."""
        return self._type_spec

    @property
    def decorators(self) -> tuple[DecoratorModule.DecoratorMeta, ...]:
        """Get the parameter decorators (immutable)."""
        return self._decorators


class FunctionMeta:
    """Metadata for a function declaration."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        return_type: str,
        parameters: list[ParameterMeta] | None = None,
        decorators: list[DecoratorModule.DecoratorMeta] | None = None
    ):
        """Initialize function metadata.

        Args:
            name: The function identifier
            namespace: Qualified namespace path
            return_type: The return type specification
            parameters: List of function parameters
            decorators: Optional list of decorators (e.g., @WinApi)
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._return_type: str
        self._parameters: list[ParameterMeta]
        self._decorators: tuple[DecoratorModule.DecoratorMeta, ...]

        self._name = name
        self._namespace = namespace
        self._return_type = return_type
        self._parameters = parameters if parameters is not None else []
        self._decorators = tuple(decorators) if decorators is not None else ()

    @property
    def name(self) -> str:
        """Get the function name."""
        return self._name

    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace

    @property
    def return_type(self) -> str:
        """Get the return type."""
        return self._return_type

    @property
    def parameters(self) -> list[ParameterMeta]:
        """Get the function parameters."""
        return self._parameters

    @property
    def decorators(self) -> tuple[DecoratorModule.DecoratorMeta, ...]:
        """Get the function decorators (immutable)."""
        return self._decorators
