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

    def __init__(self, name: str, type_spec: str):
        """Initialize structure member metadata.

        Args:
            name: The member identifier
            type_spec: The type specification string
        """
        self._name: str
        self._type_spec: str

        self._name = name
        self._type_spec = type_spec

    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name

    @property
    def type_spec(self) -> str:
        """Get the type specification."""
        return self._type_spec


class StructureMeta:
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
        base_type: str | None = None,
        members: list[StructureMemberMeta] | None = None
    ):
        """Initialize structure metadata.

        Args:
            name: The structure identifier
            namespace: Qualified namespace path
            members: List of structure members
        """

        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = members if members is not None else []

    @property
    def name(self):
        """Get the structure name."""
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
    def members(self):
        """Get the structure members."""
        return self._members
