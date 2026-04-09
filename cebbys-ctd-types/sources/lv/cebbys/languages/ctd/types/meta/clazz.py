"""Class Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api
import lv.cebbys.languages.ctd.types.meta.function as FunctionModule

from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar,
)

__all__ = ['ClassMemberMeta', 'ClassMeta']


class ClassMemberMeta:
    """Metadata for a class member (property/attribute).

    Class members represent individual fields within a class declaration.
    Each member has a type specification, name, and optional decorators.

    Examples:
    ```
        Unt4 numerator
        @Nullable Any* ptr
        Unt1[8] data
    ```
    """

    def __init__(
        self,
        name: str,
        type_spec: Api.TypespecMeta,
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize class member metadata.

        Args:
            name: The member identifier
            type_spec: The type specification
            decorators: List of decorators applied to this member
        """
        self._name = name
        self._type_spec = type_spec
        self._decorators = tuple(decorators)

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def type_spec(self) -> Api.TypespecMeta:
        """Get the type specification."""
        return self._type_spec

    @property
    def decorators(self) -> tuple[Api.DecoratorMeta, ...]:
        """Get the member decorators (immutable)."""
        return self._decorators


class ClassMeta(Api.DeclarationMeta[CtdGrammar.ClassDeclarationContext]):
    """Metadata for a class declaration.

    Classes combine structure (properties) and interface (methods) into a
    single declaration. A class may extend multiple base types via comma-
    separated list. Properties must appear before methods in the body.

    Examples:
    ```
        class MyClass {
            Unt4 x
            Unt4 y
            void Move(Int4 dx, Int4 dy)
        }

        class Shape : IDrawable, BaseShape {
            Any* data
            Int4 Draw()
        }

        class Empty {}
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        ctx: CtdGrammar.ClassDeclarationContext,
        bases: list[Api.TypespecMeta] = [],
        members: list[ClassMemberMeta] = [],
        methods: list[FunctionModule.FunctionMeta] = [],
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize class metadata.

        Args:
            name: The class identifier
            namespace: Qualified namespace path
            ctx: ANTLR4 parse context
            bases: List of base type specifications (empty if no extension)
            members: List of class members (properties, ordered first)
            methods: List of class methods (functions, ordered after members)
            decorators: List of decorators applied to the class
        """
        super().__init__(namespace, name, ctx, decorators)
        self._bases = list(bases)
        self._members = list(members)
        self._methods = list(methods)

    @property
    def bases(self) -> list[Api.TypespecMeta]:
        """Get the base type specifications."""
        return list(self._bases)

    @property
    def members(self) -> list[ClassMemberMeta]:
        """Get the class members (properties)."""
        return list(self._members)

    @property
    def methods(self) -> list[FunctionModule.FunctionMeta]:
        """Get the class methods."""
        return list(self._methods)
