"""Resolver API

This module contains common API classes and types for resolvers.
"""
import typing as Typing
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define

__all__ = ['ResolutionError', 'ResolverContext']


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
        type_cache: dict[str, Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition],
        meta_collection: Types.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ):
        """Initialize resolver context.
        
        Args:
            type_cache: Cache of all type instances by qualified name
            meta_collection: Metadata collection being resolved
            namespace_uses: Mapping of namespace to list of used namespaces
        """
        self._type_cache: dict[str, Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition]
        self._meta_collection: Types.DefinitionCollectionMeta
        self._namespace_uses: dict[str, list[str]]
        
        self._type_cache = type_cache
        self._meta_collection = meta_collection
        self._namespace_uses = namespace_uses
    
    @property
    def type_cache(self) -> dict[str, Define.TypedefDefinition | Define.EnumDefinition | Define.FlagDefinition]:
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
