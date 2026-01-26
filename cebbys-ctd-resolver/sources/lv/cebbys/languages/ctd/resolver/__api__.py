"""Resolver API

This module contains common API classes and types for resolvers.
"""
import lv.cebbys.languages.ctd.types.define as Define
import lv.cebbys.languages.ctd.types.meta as Types
import abc as Abc

__all__ = ['ResolutionError', 'ResolverContext', 'BaseResolver']


class ResolutionError(Exception):
    """Exception raised when type resolution fails."""
    pass


class ResolverContext:
    """Shared context for type resolution.

    This context provides access to the type cache and namespace information
    needed by all resolvers.
    """

    def __init__(
        self,
        type_cache: dict[str, Define.BaseDefinition],
        meta_collection: Types.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ):
        """Initialize resolver context.

        Args:
            type_cache: Cache of all type instances by qualified name
            meta_collection: Metadata collection being resolved
            namespace_uses: Mapping of namespace to list of used namespaces
        """
        self._type_cache: dict[str, Define.BaseDefinition]
        self._meta_collection: Types.DefinitionCollectionMeta
        self._namespace_uses: dict[str, list[str]]

        self._type_cache = type_cache
        self._meta_collection = meta_collection
        self._namespace_uses = namespace_uses

    @property
    def type_cache(self) -> dict[str, Define.BaseDefinition]:
        """Get the type cache."""
        return self._type_cache

    @property
    def meta_collection(self) -> Types.DefinitionCollectionMeta:
        """Get the metadata collection."""
        return self._meta_collection

    @property
    def namespace_uses(self) -> dict[str, list[str]]:
        """Get the namespace uses mapping."""
        return self._namespace_uses


class BaseResolver(Abc.ABC):
    """Base class for all type resolvers.

    Provides common functionality including type specification parsing.
    """

    def __init__(self, context: ResolverContext):
        """Initialize base resolver.

        Args:
            context: Resolver context with type cache and metadata
        """
        self._context: ResolverContext
        self._context = context

    @Abc.abstractmethod
    def create_instances(self) -> None:
        """Create type instances and add them to the type cache.

        This method must be implemented by subclasses to create their
        specific type instances.
        """
        pass

    @Abc.abstractmethod
    def resolve_instances(self) -> None:
        """Resolve type references in created instances.

        This method must be implemented by subclasses to resolve their
        specific type references and set all deferred properties.
        """
        pass

    def parse_type_spec(self, type_spec_str: str, context_namespace: str) -> Define.TypeSpec:
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
        base_type: Define.BaseType

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
            raise ResolutionError(
                f"Invalid type specification: {type_spec_str}")

        type_name = parts[0]

        # Check if it's a primitive type
        if type_name in ('char', 'short', 'int', 'long', 'void'):
            base_type = Define.PrimitiveType(type_name, signed)
        else:
            # It's a type reference - resolve it
            base_type = self._resolve_type_reference(
                type_name, context_namespace)

        return Define.TypeSpec(base_type, is_pointer)

    def _resolve_type_reference(
        self,
        type_name: str,
        context_namespace: str
    ) -> Define.TypeReference:
        """Resolve a type reference by name.

        Args:
            type_name: Type name (qualified or unqualified)
            context_namespace: Namespace context for resolving unqualified names

        Returns:
            TypeReference pointing to the resolved type

        Raises:
            ResolutionError: If type cannot be found
        """
        target_type: Define.BaseDefinition | None
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
            if target_type is None and context_namespace in self._context.namespace_uses:
                for used_namespace in self._context.namespace_uses[context_namespace]:
                    qualified_name = f"{used_namespace}::{type_name}"
                    target_type = self._find_type(qualified_name)
                    if target_type is not None:
                        break

        if target_type is None:
            raise ResolutionError(
                f"Cannot resolve type reference '{type_name}' in namespace '{context_namespace}'. "
                f"Type must be in the same namespace, imported via 'use' declaration, "
                f"or referenced with a fully qualified name."
            )

        return Define.TypeReference(target_type)

    def _find_type(self, qualified_name: str) -> Define.BaseDefinition | None:
        """Find a type by qualified name in the cache.

        Args:
            qualified_name: Fully qualified type name

        Returns:
            The type definition or None if not found
        """
        return self._context.type_cache.get(qualified_name)
