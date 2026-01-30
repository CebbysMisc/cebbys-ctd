"""Interface Meta Module"""
import lv.cebbys.languages.ctd.types.meta.function as FunctionModule
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['InterfaceMeta']


class InterfaceMeta:
    """Metadata for an interface declaration.

    Interfaces define contracts with method signatures that implementations must provide.
    An interface can optionally extend another interface (base type) and contains
    zero or more method declarations. Methods are defined using function syntax.

    Examples:
    ```
        interface IUnknown {
            Int4 QueryInterface(Unt4 interfaceId, Any* vtable)
            Unt4 AddRef()
            Unt4 Release()
        }

        interface IDispatch : IUnknown {
            Int4 GetTypeInfoCount(Unt4* count)
            Int4 GetTypeInfo(Unt4 index, Unt4 lcid, Any* typeInfo)
        }
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        methods: list[FunctionModule.FunctionMeta] | None = None
    ):
        """Initialize interface metadata.

        Args:
            name: The interface identifier
            namespace: Qualified namespace path
            methods: List of interface method definitions
        """
        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._methods = methods if methods is not None else []

    @property
    def name(self):
        """Get the interface name."""
        return self._name

    @property
    def namespace(self):
        """Get the namespace."""
        return self._namespace

    @property
    def base_type(self):
        """Get the base type."""
        return self._base_type

    @property
    def methods(self):
        """Get the interface methods."""
        return self._methods
