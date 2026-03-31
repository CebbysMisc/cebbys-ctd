"""Interface Meta Module"""
import lv.cebbys.languages.ctd.types.meta.function as FunctionModule
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['InterfaceMeta']


class InterfaceMeta(Api.DeclarationMeta):
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
        base_type: Api.TypespecMeta | None = None,
        methods: list[FunctionModule.FunctionMeta] = [],
        decorators: list[Api.DecoratorMeta] = [],
        ctx=None
    ):
        """Initialize interface metadata.

        Args:
            name: The interface identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            methods: List of interface method definitions
            decorators: List of decorators
            ctx: ANTLR4 parse context
        """
        super().__init__(namespace, name, decorators, ctx)
        self._base_type = base_type
        self._methods = list(methods)

    @property
    def base_type(self):
        """Get the base type."""
        return self._base_type

    @property
    def methods(self):
        """Get the interface methods."""
        return list(self._methods)
