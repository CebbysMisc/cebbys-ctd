"""Typedef Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['TypedefMeta']


class TypedefMeta:
    """Metadata for a typedef declaration.

    Typedef provide metadata for simple type definition by creating new instances.
    It consists of the `typedef` keyword, optional `signed|unsigned` keyword, basetype and the typename.

    Examples:
    ```
        typedef byte              Int1
        typedef signed byte       Snt1
        typedef unsigned byte     Unt1
    ```
    """

    def __init__(
        self,
        name: str,
        type_spec: str,
        namespace: Api.ModulePath
    ):
        """Initialize typedef metadata.

        Args:
            name: The typedef identifier
            type_spec: The type specification string
            namespace: Qualified namespace path
        """
        self._name = name
        self._type_spec = type_spec
        self._namespace = namespace

    @property
    def name(self):
        """Get the typedef name."""
        return self._name

    @property
    def type_spec(self):
        """Get the type specification."""
        return self._type_spec

    @property
    def namespace(self):
        """Get the namespace."""
        return self._namespace
