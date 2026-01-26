"""Meta Loader

This module handles loading and parsing CTD files into metadata.
"""
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta.collection as CollectionModule
import lv.cebbys.languages.ctd.meta.visitor as Visitor

import typing as Typing
import antlr4 as Antlr4

from lv.cebbys.languages.ctd.antlr4 import CtdParser as GtdParser
from lv.cebbys.languages.ctd.antlr4 import CtdLexer as GtdLexer

__all__ = ['MetaLoader']


class MetaLoader:
    """Loads and parses CTD files into metadata."""

    def __init__(self, paths: list[Api.FilePath]):
        """Initialize the loader with paths to search.

        Args:
            paths: List of file or directory paths to search for .ctd files
        """
        self._paths: Typing.Final[list[Api.FilePath]]
        self._paths = paths

    def load(self) -> tuple[CollectionModule.DefinitionCollectionMeta, dict[str, list[str]]]:
        """Load and parse all CTD modules from configured paths.

        Returns:
            Tuple of (DefinitionCollectionMeta, namespace_uses dictionary)
        """
        meta_collection: CollectionModule.DefinitionCollectionMeta
        namespace_uses: dict[str, list[str]]
        path: Api.FilePath

        meta_collection = CollectionModule.DefinitionCollectionMeta()
        namespace_uses = {}

        for path in self._paths:
            if path.is_file() and path.suffix == '.ctd':
                self._load_file(path, meta_collection, namespace_uses)
            elif path.is_dir():
                self._load_directory(path, meta_collection, namespace_uses)

        return meta_collection, namespace_uses

    def _load_directory(
        self,
        directory: Api.FilePath,
        collection: CollectionModule.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> None:
        """Recursively load all .ctd files from a directory.

        Args:
            directory: Directory path to search
            collection: Collection to add parsed types to
            namespace_uses: Dictionary to merge namespace use declarations
        """
        ctd_file: Api.FilePath

        for ctd_file in directory.rglob('*.ctd'):
            if ctd_file.is_file():
                self._load_file(ctd_file, collection, namespace_uses)

    def _load_file(
        self,
        file_path: Api.FilePath,
        collection: CollectionModule.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> None:
        """Load and parse a single CTD file.

        Args:
            file_path: Path to the .ctd file
            collection: Collection to add parsed types to
            namespace_uses: Dictionary to merge namespace use declarations
        """
        parse_tree: GtdParser.CompilationUnitContext
        visitor: Visitor.MetaVisitor

        # Parse the file
        parse_tree = self._parse_file(file_path)

        # Create visitor and visit parse tree
        visitor = Visitor.MetaVisitor()
        visitor.visitCompilationUnit(parse_tree)

        # Merge visitor's collection into main collection
        collection.add_all(visitor.collection)

        # Merge namespace uses
        for ns, used_list in visitor.namespace_uses.items():
            if ns not in namespace_uses:
                namespace_uses[ns] = []
            namespace_uses[ns].extend(used_list)

    def _parse_file(self, file_path: Api.FilePath) -> GtdParser.CompilationUnitContext:
        """Parse a CTD file using ANTLR4.

        Args:
            file_path: Path to the .ctd file

        Returns:
            Parse tree root node
        """
        content: str
        input_stream: Antlr4.InputStream
        lexer: GtdLexer
        token_stream: Antlr4.CommonTokenStream
        parser: GtdParser

        # Read file content
        content = file_path.read_text(encoding='utf-8')

        # Create ANTLR4 input stream
        input_stream = Antlr4.InputStream(content)

        # Create lexer
        lexer = GtdLexer(input_stream)

        # Create token stream
        token_stream = Antlr4.CommonTokenStream(lexer)

        # Create parser
        parser = GtdParser(token_stream)

        # Parse and return compilation unit
        return parser.compilationUnit()
