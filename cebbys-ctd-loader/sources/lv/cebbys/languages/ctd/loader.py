"""CTD Module Loader

This module handles loading and parsing CTD (Custom Type Definition) files.
"""
import typing as Typing
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as TypeMeta
import lv.cebbys.languages.ctd.types.define as Define
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.resolver as Resolver

__all__ = ['CtdLoader']


class CtdLoader:
    """Loads and parses CTD module files."""

    def __init__(self, paths: list[Api.FilePath]):
        """Initialize the loader with paths to search.

        Args:
            paths: List of file or directory paths to search for .ctd files
        """
        self._paths: Typing.Final[list[Api.FilePath]]
        self._paths = paths

    def load(self) -> Define.DefinitionCollection:
        """Load and parse all CTD modules from configured paths.

        Returns:
            DefinitionCollection containing all resolved type definitions
        """
        meta_collection: TypeMeta.DefinitionCollectionMeta
        namespace_uses: dict[str, list[str]]
        loader: Meta.MetaLoader
        resolver: Resolver.MetaResolver

        # Load metadata using MetaLoader
        loader = Meta.MetaLoader(self._paths)
        meta_collection, namespace_uses = loader.load()

        # Resolve type references using MetaResolver
        resolver = Resolver.MetaResolver()
        return resolver.resolve(meta_collection, namespace_uses)

