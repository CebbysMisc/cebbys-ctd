"""Interface Meta Module"""
import lv.cebbys.languages.ctd.types.meta.function as FunctionModule
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['InterfaceMeta']


class InterfaceMeta:
    """Metadata for an interface declaration."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

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
