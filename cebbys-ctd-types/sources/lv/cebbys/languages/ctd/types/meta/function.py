"""Function Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['ParameterMeta', 'FunctionMeta']


class ParameterMeta:
    """Metadata for a function parameter.

    Parameters represent individual arguments in a function declaration.
    Each parameter has a type specification and name, and can optionally
    have decorators like @Nullable to indicate special semantics.

    Examples:
    ```
        Unt4                    sdkVersion      // Simple parameter
        FeatureLevel*           featureLevels   // Pointer parameter
        @Nullable Adapter*      adapter         // Decorated parameter
    ```
    """

    def __init__(
        self,
        name: str,
        type_spec: Api.TypespecMeta,
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize parameter metadata.

        Args:
            name: The parameter identifier
            type_spec: The type specification string
            decorators: List of decorators (e.g., @Nullable)
        """
        self._name = name
        self._type_spec = type_spec
        self._decorators = tuple(decorators)

    @property
    def name(self) -> str:
        """Get the parameter name."""
        return self._name

    @property
    def type_spec(self) -> Api.TypespecMeta:
        """Get the type specification."""
        return self._type_spec

    @property
    def decorators(self) -> tuple[Api.DecoratorMeta, ...]:
        """Get the parameter decorators (immutable)."""
        return self._decorators


class FunctionMeta(Api.DeclarationMeta):
    """Metadata for a function declaration.

    Functions define callable signatures with a return type, name, and parameters.
    Functions can have decorators (e.g., @WinApi) and parameters can also be
    decorated (e.g., @Nullable). Functions are declared at namespace scope.

    Examples:
    ```
        @WinApi
        ResultCode CreateDeviceAndSwapChain(
            @Nullable Adapter*  adapter,
            DriverType          driverType,
            Unt4                sdkVersion,
        )

        Unt4 AddRef()
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        return_type: str,
        parameters: list[ParameterMeta] = [],
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize function metadata.

        Args:
            name: The function identifier
            namespace: Qualified namespace path
            return_type: The return type specification
            parameters: List of function parameters
            decorators: List of decorators (e.g., @WinApi)
        """
        super().__init__(namespace, name, decorators)
        self._return_type = return_type
        self._parameters = list(parameters)

    @property
    def return_type(self) -> str:
        """Get the return type."""
        return self._return_type

    @property
    def parameters(self) -> list[ParameterMeta]:
        """Get the function parameters."""
        return list(self._parameters)
