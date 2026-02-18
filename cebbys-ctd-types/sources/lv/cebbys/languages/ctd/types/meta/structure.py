"""Structure Meta Module"""
import lv.cebbys.languages.ctd.types.meta.__api__ as Api

__all__ = ['StructureMemberMeta', 'StructureMeta']


class StructureMemberMeta:
    """Metadata for a structure member.

    Structure members represent individual fields within a structure declaration.
    Each member has a type specification and name. Types can include pointers,
    arrays, and references to other defined types.

    Examples:
    ```
        Unt4 numerator          // Simple member
        Any vtable              // Pointer-like member
        Unt1[8] data4           // Array member
    ```
    """

    def __init__(self, name: str, type_spec: Api.TypespecMeta):
        """Initialize structure member metadata.

        Args:
            name: The member identifier
            type_spec: The type specification string
        """
        self._type_spec = type_spec
        self._name = name

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def type_spec(self) -> Api.TypespecMeta:
        """Get the type specification."""
        return self._type_spec


class StructureMeta(Api.DeclarationMeta):
    """Metadata for a structure declaration.

    Structures define composite types with named member fields.
    A structure can optionally extend another structure (base type) and contains
    zero or more member declarations. Members are defined with their type and name.

    Examples:
    ```
        structure Rational {
            Unt4 numerator
            Unt4 denominator
        }

        structure Guid {
            Unt4 data1
            Unt2 data2
            Unt2 data3
            Unt1[8] data4
        }

        structure ExtendedRational : Rational {
            Unt4 precision
        }
    ```
    """

    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: Api.TypespecMeta | None = None,
        members: list[StructureMemberMeta] = [],
        decorators: list[Api.DecoratorMeta] = []
    ):
        """Initialize structure metadata.

        Args:
            name: The structure identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of structure members
            decorators: List of decorators
        """
        super().__init__(namespace, name, decorators)
        self._base_type = base_type
        self._members = list(members)

    @property
    def base_type(self) -> Api.TypespecMeta | None:
        """Get the base type."""
        return self._base_type

    @property
    def members(self):
        """Get the structure members."""
        return list(self._members)
