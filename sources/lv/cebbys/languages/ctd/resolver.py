"""CTD Definition Resolver

This module resolves type references in metadata to create fully resolved definitions.
"""
import typing as Typing
import re
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.definitions as Definitions

__all__ = ['DefinitionResolver', 'ResolutionError']


class ResolutionError(Exception):
    """Exception raised when type resolution fails."""
    pass


class DefinitionResolver:
    """Resolves metadata into fully resolved definitions."""
    
    def __init__(self):
        """Initialize the resolver."""
        # Cache of all type instances by qualified name
        self._type_cache: dict[str, Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition]
        self._meta_collection: Meta.DefinitionCollectionMeta | None
        self._namespace_uses: dict[str, list[str]]
        
        self._type_cache = {}
        self._meta_collection = None
        self._namespace_uses = {}
    
    def resolve(
        self,
        meta_collection: Meta.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> Definitions.DefinitionCollection:
        """Resolve metadata collection into definition collection.
        
        This follows a two-phase approach:
        1. Create all type instances and cache them by qualified name
        2. Resolve all type references by looking up cached instances
        
        This design naturally handles circular/recursive type references.
        
        Args:
            meta_collection: Metadata collection to resolve
            namespace_uses: Mapping of namespace to list of used namespaces
            
        Returns:
            Immutable resolved definition collection
            
        Raises:
            ResolutionError: If type resolution fails
        """
        self._meta_collection = meta_collection
        self._namespace_uses = namespace_uses
        self._type_cache = {}
        
        # Phase 1: Create all type instances and cache them
        self._create_type_instances()
        
        # Phase 2: Resolve all type references
        self._resolve_type_references()
        
        # Build final immutable collection
        typedefs = {qn: t for qn, t in self._type_cache.items() 
                    if isinstance(t, Definitions.TypedefDefinition)}
        enums = {qn: e for qn, e in self._type_cache.items() 
                 if isinstance(e, Definitions.EnumDefinition)}
        flags = {qn: f for qn, f in self._type_cache.items() 
                 if isinstance(f, Definitions.FlagDefinition)}
        
        return Definitions.DefinitionCollection(typedefs, enums, flags)
    
    def _create_type_instances(self) -> None:
        """Create all type instances and cache them by qualified name.
        
        This creates typedef, enum, and flag instances without resolving their type
        references yet. The instances are cached so they can be referenced
        during the resolution phase, enabling circular/recursive types.
        """
        typedef_meta: Meta.TypedefMeta
        enum_meta: Meta.EnumMeta
        flag_meta: Meta.FlagMeta
        qualified_name: str
        
        # Create typedef instances
        for typedef_meta in self._meta_collection.typedefs:
            qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
            typedef_instance = Definitions.TypedefDefinition(
                typedef_meta.name,
                typedef_meta.namespace
                # type_spec will be set in phase 2
            )
            self._type_cache[qualified_name] = typedef_instance
        
        # Create enum instances
        for enum_meta in self._meta_collection.enums:
            qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
            enum_instance = Definitions.EnumDefinition(
                enum_meta.name,
                enum_meta.namespace
                # base_type and members will be set in phase 2
            )
            self._type_cache[qualified_name] = enum_instance
        
        # Create flag instances
        for flag_meta in self._meta_collection.flags:
            qualified_name = f"{flag_meta.namespace}::{flag_meta.name}"
            flag_instance = Definitions.FlagDefinition(
                flag_meta.name,
                flag_meta.namespace
                # base_type and members will be set in phase 2
            )
            self._type_cache[qualified_name] = flag_instance
    
    def _resolve_type_references(self) -> None:
        """Resolve all type references by looking up cached instances.
        
        This sets the type specifications and members for all types created
        in phase 1. Since all instances are already cached, references to
        other types (including circular references) can be resolved.
        """
        typedef_meta: Meta.TypedefMeta
        enum_meta: Meta.EnumMeta
        flag_meta: Meta.FlagMeta
        
        # Resolve typedefs
        for typedef_meta in self._meta_collection.typedefs:
            qualified_name = f"{typedef_meta.namespace}::{typedef_meta.name}"
            typedef_instance = self._type_cache[qualified_name]
            if isinstance(typedef_instance, Definitions.TypedefDefinition):
                type_spec = self._parse_type_spec(typedef_meta.type_spec, typedef_meta.namespace)
                typedef_instance.set_type_spec(type_spec)
        
        # Resolve enums
        for enum_meta in self._meta_collection.enums:
            qualified_name = f"{enum_meta.namespace}::{enum_meta.name}"
            enum_instance = self._type_cache[qualified_name]
            if isinstance(enum_instance, Definitions.EnumDefinition):
                # Resolve base type if specified
                base_type = None
                if enum_meta.base_type:
                    base_type = self._parse_type_spec(enum_meta.base_type, enum_meta.namespace)
                enum_instance.set_base_type(base_type)
                
                # Resolve members
                members = self._resolve_enum_members(enum_meta.members)
                enum_instance.set_members(members)
        
        # Resolve flags
        for flag_meta in self._meta_collection.flags:
            qualified_name = f"{flag_meta.namespace}::{flag_meta.name}"
            flag_instance = self._type_cache[qualified_name]
            if isinstance(flag_instance, Definitions.FlagDefinition):
                # Resolve base type if specified
                base_type = None
                if flag_meta.base_type:
                    base_type = self._parse_type_spec(flag_meta.base_type, flag_meta.namespace)
                flag_instance.set_base_type(base_type)
                
                # Resolve members with bit-shifting
                members = self._resolve_flag_members(flag_meta.members)
                flag_instance.set_members(members)
    
    def _resolve_enum_members(
        self,
        members_meta: list[Meta.EnumMemberMeta]
    ) -> list[Definitions.EnumMemberDefinition]:
        """Resolve enum members with automatic value assignment.
        
        Args:
            members_meta: List of enum member metadata
            
        Returns:
            List of resolved enum member definitions
        """
        members: list[Definitions.EnumMemberDefinition]
        current_value: int
        member_meta: Meta.EnumMemberMeta
        value: int
        
        members = []
        current_value = 0
        
        for member_meta in members_meta:
            if member_meta.value is not None:
                value = member_meta.value
                current_value = value + 1
            else:
                value = current_value
                current_value += 1
            
            members.append(Definitions.EnumMemberDefinition(member_meta.name, value))
        
        return members
    
    def _resolve_flag_members(
        self,
        members_meta: list[Meta.FlagMemberMeta]
    ) -> list[Definitions.FlagMemberDefinition]:
        """Resolve flag members with bit-shifting value assignment.
        
        Flags start at 0x1 and each subsequent member is bit-shifted left:
        - First: 0x1 (1)
        - Second: 0x2 (2)
        - Third: 0x4 (4)
        - Fourth: 0x8 (8)
        - etc.
        
        Manual offsets can be specified (e.g., 0x20), and bit-shifting
        continues from that value for subsequent members.
        
        Args:
            members_meta: List of flag member metadata
            
        Returns:
            List of resolved flag member definitions
        """
        members: list[Definitions.FlagMemberDefinition]
        member_meta: Meta.FlagMemberMeta
        current_value: int
        value: int
        
        members = []
        current_value = 0x1  # Start at 0x1 (1)
        
        for member_meta in members_meta:
            if member_meta.value is not None:
                # Explicit value specified
                value = member_meta.value
                current_value = value << 1  # Next value is this value bit-shifted left
            else:
                # Auto-assign bit-shifted value
                value = current_value
                current_value = current_value << 1  # Bit-shift left for next member
            
            members.append(Definitions.FlagMemberDefinition(member_meta.name, value))
        
        return members
    
    def _parse_type_spec(self, type_spec_str: str, context_namespace: str) -> Definitions.TypeSpec:
        """Parse a type specification string into a TypeSpec object.
        
        Args:
            type_spec_str: Type specification string (e.g., "signed int", "Int4 *")
            context_namespace: Namespace context for resolving unqualified names
            
        Returns:
            Resolved TypeSpec object
            
        Raises:
            ResolutionError: If type cannot be resolved
        """
        parts: list[str]
        is_pointer: bool
        signed: bool | None
        base_type: Definitions.PrimitiveType | Definitions.TypeReference
        
        # Parse the type spec string
        parts = type_spec_str.strip().split()
        is_pointer = parts[-1] == '*' if parts else False
        
        if is_pointer:
            parts = parts[:-1]
        
        # Check for sign modifier
        signed = None
        if parts and parts[0] in ('signed', 'unsigned'):
            signed = parts[0] == 'signed'
            parts = parts[1:]
        
        if not parts:
            raise ResolutionError(f"Invalid type specification: {type_spec_str}")
        
        type_name = parts[0]
        
        # Check if it's a primitive type
        if type_name in ('char', 'short', 'int', 'long', 'void'):
            base_type = Definitions.PrimitiveType(type_name, signed)
        else:
            # It's a type reference - resolve it
            base_type = self._resolve_type_reference(type_name, context_namespace)
        
        return Definitions.TypeSpec(base_type, is_pointer)
    
    def _resolve_type_reference(
        self,
        type_name: str,
        context_namespace: str
    ) -> Definitions.TypeReference:
        """Resolve a type reference by name.
        
        Args:
            type_name: Type name (qualified or unqualified)
            context_namespace: Namespace context for resolving unqualified names
            
        Returns:
            TypeReference pointing to the resolved type
            
        Raises:
            ResolutionError: If type cannot be found
        """
        target_type: Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition | None
        qualified_name: str
        used_namespace: str
        
        # If the name contains '::', it's already qualified
        if '::' in type_name:
            qualified_name = type_name
            target_type = self._find_type(qualified_name)
        else:
            # Try in current namespace first
            qualified_name = f"{context_namespace}::{type_name}"
            target_type = self._find_type(qualified_name)
            
            # If not found, try in used namespaces
            if target_type is None and context_namespace in self._namespace_uses:
                for used_namespace in self._namespace_uses[context_namespace]:
                    qualified_name = f"{used_namespace}::{type_name}"
                    target_type = self._find_type(qualified_name)
                    if target_type is not None:
                        break
            
            # If still not found, search globally
            if target_type is None:
                target_type = self._find_type_globally(type_name)
        
        if target_type is None:
            raise ResolutionError(
                f"Cannot resolve type reference '{type_name}' in namespace '{context_namespace}'"
            )
        
        return Definitions.TypeReference(target_type)
    
    def _find_type_globally(self, type_name: str) -> Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition | None:
        """Search for a type by unqualified name across all namespaces.
        
        Args:
            type_name: Unqualified type name
            
        Returns:
            The type definition or None if not found or if ambiguous
        """
        found_type: Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition | None
        qualified_name: str
        type_def: Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition
        
        found_type = None
        
        # Search in all cached types
        for qualified_name, type_def in self._type_cache.items():
            if qualified_name.endswith(f"::{type_name}"):
                if found_type is not None:
                    # Ambiguous - found in multiple namespaces
                    raise ResolutionError(
                        f"Ambiguous type reference '{type_name}' - found in multiple namespaces"
                    )
                found_type = type_def
        
        return found_type
    
    def _find_type(self, qualified_name: str) -> Definitions.TypedefDefinition | Definitions.EnumDefinition | Definitions.FlagDefinition | None:
        """Find a type by qualified name in the cache.
        
        Args:
            qualified_name: Fully qualified type name
            
        Returns:
            The type definition or None if not found
        """
        return self._type_cache.get(qualified_name)
