"""Alias Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['AliasMeta']


class AliasMeta(Api.DeclarationMeta):
    """Metadata for an alias declaration.

    Alias provide metadata for simple type renaming without creating a new type.
    When the type is actually resolved, the referred datatype is used instead of alias.
    Alias is defined the same way as type definition is defined but with keyword alias.

    Examples:
    ```
        alias byte              Int1
        alias signed byte       Snt1
        alias unsigned byte     Unt1
    ```
    """

    def __init__(
        self,
        name: str,
        type_spec: str,
        namespace: Api.ModulePath,
        decorators: list[Api.DecoratorMeta] = []
    ) -> None:
        """Initialize alias metadata.

        Args:
            name: The alias identifier
            type_spec: The type specification string
            namespace: Qualified namespace path
        """
        super().__init__(namespace, name, decorators)
        self._type_spec = type_spec

    @property
    def type_spec(self):
        """Get the type specification."""
        return self._type_spec
