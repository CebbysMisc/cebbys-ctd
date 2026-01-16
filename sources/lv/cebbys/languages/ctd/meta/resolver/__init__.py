"""Meta Resolver Module

This module resolves type references in metadata to create fully resolved definitions.
"""
import typing as Typing
import lv.cebbys.languages.ctd.meta.types as Types
import lv.cebbys.languages.ctd.define.types as Define
import lv.cebbys.languages.ctd.meta.resolver.__api__ as Api
import lv.cebbys.languages.ctd.meta.resolver.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.resolver.enum as EnumModule
import lv.cebbys.languages.ctd.meta.resolver.flag as FlagModule
import lv.cebbys.languages.ctd.meta.resolver.structure as StructureModule

__all__ = ['MetaResolver', 'ResolutionError']

# Re-export ResolutionError from API
ResolutionError = Api.ResolutionError


class MetaResolver:
    """Resolves metadata into fully resolved definitions."""

    # List of resolver classes to use
    _RESOLVER_CLASSES: Typing.Final[list[type[Api.BaseResolver]]] = [
        TypedefModule.TypedefResolver,
        EnumModule.EnumResolver,
        FlagModule.FlagResolver,
        StructureModule.StructureResolver,
    ]

    def __init__(self):
        """Initialize the resolver."""
        pass

    def resolve(
        self,
        meta_collection: Types.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> Define.DefinitionCollection:
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
        type_cache: dict[str, Define.BaseDefinition]
        context: Api.ResolverContext
        resolvers: list[Api.BaseResolver]
        resolver_class: type[Api.BaseResolver]
        resolver: Api.BaseResolver
        typedefs: dict[str, Define.TypedefDefinition]
        enums: dict[str, Define.EnumDefinition]
        flags: dict[str, Define.FlagDefinition]
        structures: dict[str, Define.StructureDefinition]

        # Create context
        type_cache = {}
        context = Api.ResolverContext(
            type_cache, meta_collection, namespace_uses)

        # Instantiate all resolvers
        resolvers = []
        for resolver_class in self._RESOLVER_CLASSES:
            resolvers.append(resolver_class(context))

        # Phase 1: Create all type instances and cache them
        for resolver in resolvers:
            resolver.create_instances()

        # Phase 2: Resolve all type references
        for resolver in resolvers:
            resolver.resolve_instances()

        # Build final immutable collection
        typedefs = {qn: t for qn, t in type_cache.items()
                    if isinstance(t, Define.TypedefDefinition)}
        enums = {qn: e for qn, e in type_cache.items()
                 if isinstance(e, Define.EnumDefinition)}
        flags = {qn: f for qn, f in type_cache.items()
                 if isinstance(f, Define.FlagDefinition)}
        structures = {qn: s for qn, s in type_cache.items()
                      if isinstance(s, Define.StructureDefinition)}

        return Define.DefinitionCollection(typedefs, enums, flags, structures)
