"""Structure Meta Module"""
import lv.cebbys.languages.ctd.meta.loader.__api__ as Api

__all__ = ['StructureMemberMeta', 'StructureMeta']


class StructureMemberMeta:
    """Metadata for a structure member."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

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
    """Metadata for a structure declaration."""
    # TODO: Update class documentation to add description about usage and examples as in the alias.py, decorator.py, typedef.py

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
