"""CTD Module Loader

This module handles loading and parsing CTD (Custom Type Definition) files.
"""
import typing as Typing
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as TypeMeta
import lv.cebbys.languages.ctd.antlr4 as Antlr4

from lv.cebbys.languages.ctd.resolver.resolver import CtdMetaResolver
from lv.cebbys.languages.ctd.meta.parser import CtdMetaParser

__all__ = ['CtdLoader']


class CtdLoader:
    """Loads and parses CTD module files.
    
    Implements a four-stage transformation pipeline:
    1. list[Path] - Gather all .ctd files from directories
    2. list[ModuleDeclarationContext] - Parse files to ANTLR4 contexts
    3. list[ModuleMeta] - Convert contexts to Meta objects
    4. Resolve and link types via CtdMetaResolver (ModuleConstructor + ModuleLinker)
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
        self.ctds: list[tuple[Api.FilePath, str]]
        self.ctds = self._list_ctd_from_dirs(dirs)

        # Stage 2: Parse each file to ANTLR4 ModuleDeclarationContext
        self.contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
        self.contexts = self._parse_files_to_contexts(self.ctds)

        # Stage 3: Convert each context to ModuleMeta
        self.metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
        self.metas = self._convert_contexts_to_metas(self.contexts)

        # Stage 4: Resolve and link via ModuleConstructor + ModuleLinker
        self.definitions = self._build_type_definitions(self.metas)
        print(self.definitions)

    # =========================================================================
    # Stage 1: List all .ctd files from directories
    # =========================================================================

    def _list_ctd_from_dirs(self, dirs: list[Api.FilePath]) -> list[tuple[Api.FilePath, str]]:
        ctd_files: list[tuple[Api.FilePath, str]]
        directory: Api.FilePath
        ctd_file: Api.FilePath

        ctd_files = []

        for directory in dirs:
            if not directory.is_dir():
                continue

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
        contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
        ctd_file: Api.FilePath
        content: str
        parser: Antlr4.CtdParser
        context: Antlr4.CtdGrammar.ModuleDeclarationContext

        contexts = []

        for (ctd_file, module_name) in ctd_files:
            try:
                content = ctd_file.read_text(encoding='utf-8')
                parser = Antlr4.CtdParser()
                context = parser.moduleDeclaration(content)
                contexts.append((ctd_file, module_name, context))
            except Exception:
                pass

        return contexts

    # =========================================================================
    # Stage 3: Convert ANTLR4 contexts to Meta objects
    # =========================================================================

    def _convert_contexts_to_metas(
        self,
        module_contexts: list[tuple[Api.FilePath, str, Antlr4.CtdGrammar.ModuleDeclarationContext]]
    ) -> list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]:
        module_context: Antlr4.CtdGrammar.ModuleDeclarationContext
        module_metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
        ctd_file: Api.FilePath

        module_metas = []

        for ctd_file, module_name, module_context in module_contexts:
            try:
                module_metas.append((
                    ctd_file,
                    module_name,
                    CtdMetaParser.parse_module(module_context)
                ))
            except Exception:
                pass

        return module_metas

    # =========================================================================
    # Stage 4: Resolve and link types
    # =========================================================================

    def _build_type_definitions(
        self,
        module_metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
    ) -> Typing.Any:
        return CtdMetaResolver.resolve({
            module_name: module for _, module_name, module in module_metas
        })

