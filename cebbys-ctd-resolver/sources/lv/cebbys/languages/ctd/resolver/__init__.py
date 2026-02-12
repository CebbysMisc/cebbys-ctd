"""Meta Resolver Module

This module resolves type references in metadata to create fully resolved definitions.
"""
import typing as Typing
import lv.cebbys.languages.ctd.types.meta as Types
import lv.cebbys.languages.ctd.types.define as Define
import lv.cebbys.languages.ctd.resolver.__api__ as Api
import lv.cebbys.languages.ctd.resolver.typedef as TypedefModule
import lv.cebbys.languages.ctd.resolver.enum as EnumModule
import lv.cebbys.languages.ctd.resolver.flag as FlagModule
import lv.cebbys.languages.ctd.resolver.structure as StructureModule
import lv.cebbys.languages.ctd.resolver.function as FunctionModule
import lv.cebbys.languages.ctd.resolver.dependency_graph as DependencyGraphModule

__all__ = ['MetaResolver', 'ResolutionError', 'DependencyGraph', 'DependencyGraphBuilder']

# Re-export ResolutionError from API
ResolutionError = Api.ResolutionError

# Re-export dependency graph classes
DependencyGraph = DependencyGraphModule.DependencyGraph
DependencyGraphBuilder = DependencyGraphModule.DependencyGraphBuilder


class MetaResolver:
    """Resolves metadata into fully resolved definitions."""

    # List of resolver classes to use
    _RESOLVER_CLASSES: Typing.Final[list[type[Api.BaseResolver]]] = [
        TypedefModule.TypedefResolver,
        EnumModule.EnumResolver,
        FlagModule.FlagResolver,
        StructureModule.StructureResolver,
        FunctionModule.FunctionResolver,
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

        def filter[T](datatype: type[T]) -> dict[str, T]:
            return {
                qn: dt for qn, dt in type_cache.items()
                if isinstance(dt, datatype)
            }

        # Build final immutable collection
        typedefs = filter(Define.TypedefDefinition)
        enums = filter(Define.EnumDefinition)
        flags = filter(Define.FlagDefinition)
        structures = filter(Define.StructureDefinition)
        functions = filter(Define.FunctionDefinition)
        interfaces = filter(Define.FunctionDefinition)

        return Define.DefinitionCollection(
            typedefs,
            enums,
            flags,
            structures,
            functions
        )
