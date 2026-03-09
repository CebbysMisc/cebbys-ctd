"""CTD Module Loader

This module handles loading and parsing CTD (Custom Type Definition) files.
"""
import typing as Typing
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta as TypeMeta

from lv.cebbys.languages.ctd.resolver.resolver import (
    CtdMetaResolver
)
from lv.cebbys.languages.ctd.loader.file import (
    CtdFileCtxLoader
)
from lv.cebbys.languages.ctd.loader.antlr import (
    CtdAntlrCtxLoader
)
from lv.cebbys.languages.ctd.loader.meta import (
    CtdMetaLoader
)

__all__ = ['CtdLoader']

class CtdLoader:
    """Loads and parses CTD module files.
    
    Implements a four-stage transformation pipeline:
    1. list[Path] - Gather all .ctd files from directories
    2. list[ModuleDeclarationContext] - Parse files to ANTLR4 contexts
    3. list[ModuleMeta] - Convert contexts to Meta objects
    4. Resolve and link types via CtdMetaResolver (ModuleConstructor + ModuleLinker)
    """

    def __init__(self, roots: list[Api.FilePath]):
        """Initialize the loader with directories to search.

        Args:
            dirs: List of directory paths to search for .ctd files
        """
        # Input directories
        self._roots: Typing.Final[list[Api.FilePath]]
        self._roots = roots

        # Stage 1: Gather all .ctd file paths from directories
        ctds = CtdFileCtxLoader.load(self._roots)
        # Stage 2: Parse each file to ANTLR4 ModuleDeclarationContext
        contexts = CtdAntlrCtxLoader.load(ctds)
        # Stage 3: Convert each context to ModuleMeta
        metas = CtdMetaLoader.load(contexts)

        # Stage 4: Resolve and link via ModuleConstructor + ModuleLinker
        self.definitions, self.tree = self._build_type_definitions([(m.path, m.name, m) for m in metas])


    # =========================================================================
    # Stage 4: Resolve and link types
    # =========================================================================

    def _build_type_definitions(
        self,
        module_metas: list[tuple[Api.FilePath, str, TypeMeta.ModuleMeta]]
    ):
        return CtdMetaResolver.resolve({
            module_name: module for _, module_name, module in module_metas
        })

