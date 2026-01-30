"""Meta Loader

This module handles loading and parsing CTD files into metadata.
"""
import lv.cebbys.languages.ctd.types.__api__ as Api
import lv.cebbys.languages.ctd.types.meta.collection as CollectionModule
import lv.cebbys.languages.ctd.meta.visitor as Visitor
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import typing as Typing

__all__ = ['MetaLoader']


# class CtdParser:
#     # TODO: This will be the class exposing API to parse the contents into the ANTLR types
#     def parse_file(self, *args: Typing.Any):
#         content: str

#         length = len(args)
#         if length == 1:
#             argument: Typing.Any = args[0]
#             if isinstance(argument, Pathlib.Path):
#                 # TODO: Implement file type validation, if path points to file, only then read it
#                 content = argument.read_text(encoding="utf-8")
#             else:
#                 content = argument
#             return self._create_parser(content)
#         types = [type(a) for a in args]
#         raise BaseException(f"Not implemented 'CtdParser.parse_file' for arguments ({types})")

#     def _create_parser(self, content: str):
#         try:
#             input = Antlr4.InputStream(content)
#             lexer = Generated.CtdLexer(input)
#             stream = Antlr4.CommonTokenStream(lexer)
#             parser = Generated.CtdParser(stream)
#             return parser
#         except BaseException as e:
#             raise BaseException("Failed to parse CTD content") from e


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
        parse_tree: Antlr4.CtdParser.ModuleDeclarationContext
        visitor: Visitor.MetaVisitor

        # Parse the file
        parse_tree = self._parse_file(file_path)

        # Create visitor and visit parse tree
        visitor = Visitor.MetaVisitor()
        visitor.visitModuleDeclaration(parse_tree)

        # Merge visitor's collection into main collection
        collection.add_all(visitor.collection)

        # Merge namespace uses
        for ns, used_list in visitor.namespace_uses.items():
            if ns not in namespace_uses:
                namespace_uses[ns] = []
            namespace_uses[ns].extend(used_list)

    def _parse_file(self, file_path: Api.FilePath) -> Antlr4.CtdParser.ModuleDeclarationContext:
        """Parse a CTD file using ANTLR4.

        Args:
            file_path: Path to the .ctd file

        Returns:
            Parse tree root node
        """
        content:        str
        input_stream:   Antlr4.InputStream
        lexer:          Antlr4.CtdLexer
        token_stream:   Antlr4.CommonTokenStream
        parser:         Antlr4.CtdParser

        # Read file content
        content = file_path.read_text(encoding='utf-8')

        # Create ANTLR4 input stream
        input_stream = Antlr4.InputStream(content)

        # Create lexer
        lexer = Antlr4.CtdLexer(input_stream)

        # Create token stream
        token_stream = Antlr4.CommonTokenStream(lexer)

        # Create parser
        parser = Antlr4.CtdParser(token_stream)

        # Parse and return module declaration
        return parser.moduleDeclaration()
