"""CTD Meta Classes

This module defines metadata classes for parsed CTD (Custom Type Definition) structures.
These classes represent the remapped ANTLR4 parse tree in a more Pythonic form.
"""
import typing as Typing
import lv.cebbys.languages.ctd.__api__ as Api

__all__ = [
    'TypedefMeta', 
    'EnumMemberMeta', 
    'EnumMeta',
    'FlagMemberMeta',
    'FlagMeta',
    'StructureMemberMeta',
    'StructureMeta',
    'ParameterMeta',
    'FunctionMeta',
    'DefinitionCollectionMeta'
]


class TypedefMeta:
    """Metadata for a typedef declaration."""
    
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
        self._name: str
        self._type_spec: str
        self._namespace: Api.ModulePath
        
        self._name = name
        self._type_spec = type_spec
        self._namespace = namespace
    
    @property
    def name(self) -> str:
        """Get the typedef name."""
        return self._name
    
    @property
    def type_spec(self) -> str:
        """Get the type specification."""
        return self._type_spec
    
    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace


class EnumMemberMeta:
    """Metadata for an enum member."""
    
    def __init__(self, name: str, value: int | None = None):
        """Initialize enum member metadata.
        
        Args:
            name: The member identifier
            value: Optional explicit integer value
        """
        self._name: str
        self._value: int | None
        
        self._name = name
        self._value = value
    
    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name
    
    @property
    def value(self) -> int | None:
        """Get the member value (if explicitly set)."""
        return self._value


class EnumMeta:
    """Metadata for an enum declaration."""
    
    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        members: list[EnumMemberMeta] | None = None
    ):
        """Initialize enum metadata.
        
        Args:
            name: The enum identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of enum members
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._base_type: str | None
        self._members: list[EnumMemberMeta]
        
        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = members if members is not None else []
    
    @property
    def name(self) -> str:
        """Get the enum name."""
        return self._name
    
    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace
    
    @property
    def base_type(self) -> str | None:
        """Get the base type."""
        return self._base_type
    
    @property
    def members(self) -> list[EnumMemberMeta]:
        """Get the enum members."""
        return self._members


class FlagMemberMeta:
    """Metadata for a flag member."""
    
    def __init__(self, name: str, value: int | None = None):
        """Initialize flag member metadata.
        
        Args:
            name: The member identifier
            value: Optional explicit hex value (e.g., 0x20)
        """
        self._name: str
        self._value: int | None
        
        self._name = name
        self._value = value
    
    @property
    def name(self) -> str:
        """Get the member name."""
        return self._name
    
    @property
    def value(self) -> int | None:
        """Get the member value (if explicitly set)."""
        return self._value


class FlagMeta:
    """Metadata for a flag declaration.
    
    Flags are similar to enums but with bit-shifted values:
    - First member starts at 0x1 (1)
    - Each subsequent member is bit-shifted: 0x2, 0x4, 0x8, etc.
    - Manual offsets can be specified (e.g., BGRA_SUPPORT = 0x20)
    - After a manual offset, bit-shifting continues from that value
    """
    
    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        base_type: str | None = None,
        members: list[FlagMemberMeta] | None = None
    ):
        """Initialize flag metadata.
        
        Args:
            name: The flag identifier
            namespace: Qualified namespace path
            base_type: Optional base type specification
            members: List of flag members
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._base_type: str | None
        self._members: list[FlagMemberMeta]
        
        self._name = name
        self._namespace = namespace
        self._base_type = base_type
        self._members = members if members is not None else []
    
    @property
    def name(self) -> str:
        """Get the flag name."""
        return self._name
    
    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace
    
    @property
    def base_type(self) -> str | None:
        """Get the base type."""
        return self._base_type
    
    @property
    def members(self) -> list[FlagMemberMeta]:
        """Get the flag members."""
        return self._members


class StructureMemberMeta:
    """Metadata for a structure member."""
    
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
    
    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        members: list[StructureMemberMeta] | None = None
    ):
        """Initialize structure metadata.
        
        Args:
            name: The structure identifier
            namespace: Qualified namespace path
            members: List of structure members
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._members: list[StructureMemberMeta]
        
        self._name = name
        self._namespace = namespace
        self._members = members if members is not None else []
    
    @property
    def name(self) -> str:
        """Get the structure name."""
        return self._name
    
    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace
    
    @property
    def members(self) -> list[StructureMemberMeta]:
        """Get the structure members."""
        return self._members


class ParameterMeta:
    """Metadata for a function parameter."""
    
    def __init__(self, name: str, type_spec: str, annotation: str | None = None):
        """Initialize parameter metadata.
        
        Args:
            name: The parameter identifier
            type_spec: The type specification string
            annotation: Optional annotation (e.g., "Nullable")
        """
        self._name: str
        self._type_spec: str
        self._annotation: str | None
        
        self._name = name
        self._type_spec = type_spec
        self._annotation = annotation
    
    @property
    def name(self) -> str:
        """Get the parameter name."""
        return self._name
    
    @property
    def type_spec(self) -> str:
        """Get the type specification."""
        return self._type_spec
    
    @property
    def annotation(self) -> str | None:
        """Get the annotation."""
        return self._annotation


class FunctionMeta:
    """Metadata for a function declaration."""
    
    def __init__(
        self,
        name: str,
        namespace: Api.ModulePath,
        return_type: str,
        parameters: list[ParameterMeta] | None = None,
        annotation: str | None = None
    ):
        """Initialize function metadata.
        
        Args:
            name: The function identifier
            namespace: Qualified namespace path
            return_type: The return type specification
            parameters: List of function parameters
            annotation: Optional annotation (e.g., 'WinApi')
        """
        self._name: str
        self._namespace: Api.ModulePath
        self._return_type: str
        self._parameters: list[ParameterMeta]
        self._annotation: str | None
        
        self._name = name
        self._namespace = namespace
        self._return_type = return_type
        self._parameters = parameters if parameters is not None else []
        self._annotation = annotation
    
    @property
    def name(self) -> str:
        """Get the function name."""
        return self._name
    
    @property
    def namespace(self) -> Api.ModulePath:
        """Get the namespace."""
        return self._namespace
    
    @property
    def return_type(self) -> str:
        """Get the return type."""
        return self._return_type
    
    @property
    def parameters(self) -> list[ParameterMeta]:
        """Get the function parameters."""
        return self._parameters
    
    @property
    def annotation(self) -> str | None:
        """Get the annotation."""
        return self._annotation


class DefinitionCollectionMeta:
    """Collection of parsed type definitions from CTD modules."""
    
    def __init__(self):
        """Initialize an empty definition collection."""
        self._typedefs: list[TypedefMeta]
        self._enums: list[EnumMeta]
        self._flags: list[FlagMeta]
        self._structures: list[StructureMeta]
        self._functions: list[FunctionMeta]
        
        self._typedefs = []
        self._enums = []
        self._flags = []
        self._structures = []
        self._functions = []
    
    @property
    def typedefs(self) -> list[TypedefMeta]:
        """Get the list of typedef definitions."""
        return self._typedefs
    
    @property
    def enums(self) -> list[EnumMeta]:
        """Get the list of enum definitions."""
        return self._enums
    
    @property
    def flags(self) -> list[FlagMeta]:
        """Get the list of flag definitions."""
        return self._flags
    
    @property
    def structures(self) -> list[StructureMeta]:
        """Get the list of structure definitions."""
        return self._structures
    
    @property
    def functions(self) -> list[FunctionMeta]:
        """Get the list of function definitions."""
        return self._functions
    
    def add_typedef(self, typedef: TypedefMeta) -> None:
        """Add a typedef to the collection.
        
        Args:
            typedef: TypedefMeta instance to add
        """
        self._typedefs.append(typedef)
    
    def add_enum(self, enum: EnumMeta) -> None:
        """Add an enum to the collection.
        
        Args:
            enum: EnumMeta instance to add
        """
        self._enums.append(enum)
    
    def add_flag(self, flag: FlagMeta) -> None:
        """Add a flag to the collection.
        
        Args:
            flag: FlagMeta instance to add
        """
        self._flags.append(flag)
    
    def add_structure(self, structure: StructureMeta) -> None:
        """Add a structure to the collection.
        
        Args:
            structure: StructureMeta instance to add
        """
        self._structures.append(structure)
    
    def add_function(self, function: FunctionMeta) -> None:
        """Add a function to the collection.
        
        Args:
            function: FunctionMeta instance to add
        """
        self._functions.append(function)
