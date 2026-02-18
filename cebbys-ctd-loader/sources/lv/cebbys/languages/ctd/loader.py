"""CTD Module Loader

This module handles loading and parsing CTD (Custom Type Definition) files.
"""
import typing as Typing
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as TypeMeta
import lv.cebbys.languages.ctd.types.define as Define
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.resolver as Resolver

from lv.cebbys.languages.ctd.resolver.resolver import CtdMetaResolver
from lv.cebbys.languages.ctd.meta.parser import CtdMetaParser

__all__ = ['CtdLoader']


class CtdLoader:
    """Loads and parses CTD module files.
    
    Implements a four-stage transformation pipeline:
    1. list[Path] - Gather all .ctd files from directories
    2. list[ModuleDeclarationContext] - Parse files to ANTLR4 contexts
    3. list[ModuleMeta] - Convert contexts to Meta objects
    4. CebbysTypeDefinitions - Resolve and build singleton collection
    """

    def __init__(self, dirs: list[Api.FilePath]):
        """Initialize the loader with directories to search.

        Args:
            dirs: List of directory paths to search for .ctd files
        """
        # Input directories
        self._dirs: Typing.Final[list[Api.FilePath]]
        self._dirs = dirs

        # Stage 1: Gather all .ctd file paths from directories
        # list[Path] - file paths to load
        self.ctds: list[tuple[Api.FilePath, str]]
        self.ctds = self._list_ctd_from_dirs(dirs)

        # Stage 2: Parse each file to ANTLR4 ModuleDeclarationContext
        # list[tuple[Path, ModuleDeclarationContext]] - parsed contexts with file paths
        self.contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
        self.contexts = self._parse_files_to_contexts(self.ctds)

        # Stage 3: Convert each context to ModuleMeta
        # list[tuple[Path, ModuleMeta]] - meta objects with file paths
        self.metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
        self.metas = self._convert_contexts_to_metas(self.contexts)

        # Stage 4: TODO - Resolve and build CebbysTypeDefinitions
        # self._definitions: CebbysTypeDefinitions
        self._definitions = self._build_type_definitions(self.metas)

    def load(self) -> Define.DefinitionCollection:
        """Load and parse all CTD modules from configured paths.

        Returns:
            DefinitionCollection containing all resolved type definitions
        """
        # TODO: Implement using new transformation chain
        # For now, build collection from existing stages
        meta_collection: TypeMeta.DefinitionCollectionMeta
        namespace_uses: dict[str, list[str]]
        resolver: Resolver.MetaResolver
        file_path: Api.FilePath
        module_meta: TypeMeta.ModuleMeta
        visitor: Meta.MetaVisitor

        # Aggregate module_metas into DefinitionCollectionMeta
        meta_collection = TypeMeta.DefinitionCollectionMeta()
        namespace_uses = {}

        for file_path, module_meta in self.metas:
            # For each module, we need to extract its namespaces
            # Since ModuleMeta is currently empty, this won't work yet
            # TODO: Implement once MetaVisitor.to_module_meta() is ready
            pass

        # Temporary fallback: Re-parse using visitor directly
        # This duplicates work but allows load() to function until Stage 4 is complete
        for file_path, context in self.contexts:
            visitor = Meta.MetaVisitor()
            visitor.visitModuleDeclaration(context)
            
            # Merge visitor's collection
            meta_collection.add_all(visitor.collection)
            
            # Merge namespace uses
            for ns, used_list in visitor.namespace_uses.items():
                if ns not in namespace_uses:
                    namespace_uses[ns] = []
                namespace_uses[ns].extend(used_list)

        # Resolve type references using MetaResolver
        resolver = Resolver.MetaResolver()
        return resolver.resolve(meta_collection, namespace_uses)

    # =========================================================================
    # Stage 1: List all .ctd files from directories
    # =========================================================================

    def _list_ctd_from_dirs(self, dirs: list[Api.FilePath]) -> list[tuple[Api.FilePath, str]]:
        """Recursively gather all .ctd files from directories.

        Args:
            dirs: List of directories to search

        Returns:
            List of .ctd file paths found
        """
        ctd_files: list[tuple[Api.FilePath, str]]
        directory: Api.FilePath
        ctd_file: Api.FilePath

        ctd_files = []

        # Iterate each input directory
        for directory in dirs:
            if not directory.is_dir():
                # TODO: Collect error - not a directory
                continue

            # Recursively find all .ctd files in directory
            for ctd_file in directory.rglob('*.ctd'):
                if ctd_file.is_file():
                    name = str(ctd_file.absolute())
                    name = name.removeprefix(str(directory))[1:-4]
                    name = name.replace("\\", "/")
                    ctd_files.append((ctd_file, name))

        return ctd_files

    # =========================================================================
    # Stage 2: Parse files to ANTLR4 contexts
    # =========================================================================

    def _parse_files_to_contexts(
        self,
        ctd_files: list[tuple[Api.FilePath, str]]
    ) -> list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]:
        """Parse each .ctd file to ANTLR4 ModuleDeclarationContext.

        Args:
            ctd_files: List of .ctd file paths to parse

        Returns:
            List of tuples (file_path, parsed_context)
        """
        contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
        ctd_file: Api.FilePath
        content: str
        parser: Antlr4.CtdParser
        context: Antlr4.CtdGrammar.ModuleDeclarationContext

        contexts = []

        # Parse each file
        for (ctd_file, module_name) in ctd_files:
            try:
                # Read file content
                content = ctd_file.read_text(encoding='utf-8')

                # Parse content to ANTLR4 context
                parser = Antlr4.CtdParser()
                context = parser.moduleDeclaration(content)

                # Store file path with context
                contexts.append((ctd_file, module_name, context))

            except Exception as e:
                # TODO: Collect parse error
                # error = LoadError(
                #     file_path=ctd_file,
                #     error_type="parse_error",
                #     message=str(e)
                # )
                pass

        return contexts

    # =========================================================================
    # Stage 3: Convert ANTLR4 contexts to Meta objects
    # =========================================================================

    def _convert_contexts_to_metas(
        self,
        module_contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
    ) -> list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]:
        """Convert ANTLR4 contexts to ModuleMeta objects.

        Args:
            module_contexts: List of tuples (file_path, context)

        Returns:
            List of tuples (file_path, module_meta)
        """
        module_context: Antlr4.CtdGrammar.ModuleDeclarationContext
        module_metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
        ctd_file: Api.FilePath

        module_metas = []

        # Convert each context to ModuleMeta
        for ctd_file, module_name, module_context in module_contexts:
            try:
                module_metas.append((
                    ctd_file,
                    module_name,
                    CtdMetaParser.parse_module(module_context)
                ))

            except Exception as e:
                # TODO: Collect meta conversion error
                # error = LoadError(
                #     file_path=ctd_file,
                #     error_type="meta_error",
                #     message=str(e)
                # )
                pass

        return module_metas

    # =========================================================================
    # Stage 4: Build CebbysTypeDefinitions (TODO)
    # =========================================================================

    def _build_type_definitions(
        self,
        module_metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
    ) -> Typing.Any:
        """Resolve type references and build final type definitions.
    
        Args:
            module_metas: List of tuples (file_path, module_meta)
    
        Returns:
            CebbysTypeDefinitions with resolved singleton types
        """
        modules = CtdMetaResolver.resolve({
            module_name: module for _, module_name, module in module_metas
        })
        print(modules)
        # TODO: Implement resolution and singleton creation
        # 1. Aggregate ModuleMeta into DefinitionCollectionMeta
        # 2. Create singletons for all types
        # 3. Resolve type references
        # 4. Build file→definition metadata
        # 5. Construct CebbysTypeDefinitions
        pass

