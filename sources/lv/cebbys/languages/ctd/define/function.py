"""Function Definition Module"""
from __future__ import annotations
import typing as Typing

if Typing.TYPE_CHECKING:
    import lv.cebbys.languages.ctd.define.decorator as DecoratorModule

import lv.cebbys.languages.ctd.define.__api__ as Api

__all__ = ['ParameterDefinition', 'FunctionDefinition']


class ParameterDefinition:
    """Resolved function parameter definition."""

    def __init__(
        self,
        name: str,
        type_spec: Api.TypeSpec,
        decorators: list[DecoratorModule.DecoratorDefinition] | None = None
    ):
        """Initialize parameter definition.

        Args:
            name: Parameter name
            type_spec: Resolved type specification
            decorators: Optional list of decorators (e.g., @Nullable)
        """
        self._name: str
        self._type_spec: Api.TypeSpec
        self._decorators: tuple[DecoratorModule.DecoratorDefinition, ...]

        self._name = name
        self._type_spec = type_spec
        self._decorators = tuple(decorators) if decorators is not None else ()

    @property
    def name(self) -> str:
        """Get the parameter name."""
        return self._name

    @property
    def type_spec(self) -> Api.TypeSpec:
        """Get the parameter type specification."""
        return self._type_spec

    @property
    def decorators(self) -> tuple[DecoratorModule.DecoratorDefinition, ...]:
        """Get the parameter decorators (immutable)."""
        return self._decorators

    def __repr__(self) -> str:
        """String representation."""
        decorators_str = " ".join(str(d) for d in self._decorators)
        if decorators_str:
            decorators_str += " "
        return f"Parameter({decorators_str}{self._type_spec} {self._name})"


class FunctionDefinition(Api.BaseDefinition):
    """Resolved function definition."""

    def __init__(
        self,
        name: str,
        namespace: str,
        return_type: Api.TypeSpec | None = None,
        parameters: list[ParameterDefinition] | None = None,
        decorators: list[DecoratorModule.DecoratorDefinition] | None = None
    ):
        """Initialize function definition.

        Args:
            name: Function name
            namespace: Namespace path
            return_type: Resolved return type specification (can be set later)
            parameters: List of function parameters (can be set later)
            decorators: Optional list of decorators (e.g., @WinApi)
        """
        self._name: str
        self._namespace: str
        self._return_type: Api.TypeSpec | None
        self._parameters: tuple[ParameterDefinition, ...]
        self._decorators: tuple[DecoratorModule.DecoratorDefinition, ...]

        self._name = name
        self._namespace = namespace
        self._return_type = return_type
        self._parameters = tuple(parameters) if parameters is not None else ()
        self._decorators = tuple(decorators) if decorators is not None else ()

    def set_return_type(self, return_type: Api.TypeSpec) -> None:
        """Set the return type (for deferred resolution).

        Args:
            return_type: The resolved return type specification
        """
        self._return_type = return_type

    def set_parameters(self, parameters: list[ParameterDefinition]) -> None:
        """Set the parameters (for deferred resolution).

        Args:
            parameters: List of resolved parameter definitions
        """
        self._parameters = tuple(parameters)

    @property
    def name(self) -> str:
        """Get the function name."""
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
    def return_type(self) -> Api.TypeSpec:
        """Get the return type specification."""
        if self._return_type is None:
            raise RuntimeError(
                f"Return type not yet resolved for {self.qualified_name}")
        return self._return_type

    @property
    def parameters(self) -> Typing.Sequence[ParameterDefinition]:
        """Get the function parameters (immutable)."""
        return self._parameters

    @property
    def decorators(self) -> tuple[DecoratorModule.DecoratorDefinition, ...]:
        """Get the function decorators (immutable)."""
        return self._decorators

    def __repr__(self) -> str:
        """String representation."""
        decorators_str = " ".join(str(d) for d in self._decorators)
        if decorators_str:
            decorators_str += " "
        return f"FunctionDefinition({decorators_str}{self.qualified_name})"
