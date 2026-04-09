"""Typedef Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar,
)

__all__ = ['TypedefMeta']


class TypedefMeta(Api.DeclarationMeta[CtdGrammar.TypedefDeclarationContext]):
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
        type_spec: Api.TypespecMeta,
        namespace: Api.ModulePath,
        ctx: CtdGrammar.TypedefDeclarationContext,
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize typedef metadata.

        Args:
            name: The typedef identifier
            type_spec: The type specification string
            namespace: Qualified namespace path
            decorators: List of decorators
            ctx: ANTLR4 parse context
        """
        super().__init__(namespace, name, ctx, decorators)
        self._type_spec = type_spec

    @property
    def type_spec(self) -> Api.TypespecMeta:
        """Get the type specification."""
        return self._type_spec
