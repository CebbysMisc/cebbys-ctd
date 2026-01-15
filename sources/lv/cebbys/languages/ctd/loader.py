"""CTD Module Loader

This module handles loading and parsing CTD (Custom Type Definition) files.
"""
import typing as Typing
import pathlib as Pathlib
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.__api__ as Api
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.definitions as Definitions
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.resolver as Resolver
import lv.cebbys.languages.ctd.antlr4.GtdLexer as GtdLexer
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser

__all__ = ['CtdLoader']


class CtdLoader:
    """Loads and parses CTD module files."""
    
    def __init__(self, paths: list[Api.FilePath]):
        """Initialize the loader with paths to search.
        
        Args:
            paths: List of file or directory paths to search for .gtd files
        """
        self._paths: Typing.Final[list[Api.FilePath]]
        self._paths = paths
    
    def load(self) -> Definitions.DefinitionCollection:
        """Load and parse all CTD modules from configured paths.
        
        Returns:
            DefinitionCollection containing all resolved type definitions
        """
        meta_collection: Meta.DefinitionCollectionMeta
        namespace_uses: dict[str, list[str]]
        resolver: Resolver.DefinitionResolver
        path: Api.FilePath
        
        # First, load all metadata
        meta_collection = Meta.DefinitionCollectionMeta()
        namespace_uses = {}
        
        for path in self._paths:
            if path.is_file() and path.suffix == '.gtd':
                self._load_file(path, meta_collection, namespace_uses)
            elif path.is_dir():
                self._load_directory(path, meta_collection, namespace_uses)
        
        # Then resolve all type references
        resolver = Resolver.DefinitionResolver()
        return resolver.resolve(meta_collection, namespace_uses)
    
    def _load_directory(
        self,
        directory: Api.FilePath,
        collection: Meta.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> None:
        """Recursively load all .gtd files from a directory.
        
        Args:
            directory: Directory path to search
            collection: Collection to add parsed types to
            namespace_uses: Dictionary to merge namespace use declarations
        """
        gtd_file: Api.FilePath
        
        for gtd_file in directory.rglob('*.gtd'):
            if gtd_file.is_file():
                self._load_file(gtd_file, collection, namespace_uses)
    
    def _load_file(
        self,
        file_path: Api.FilePath,
        collection: Meta.DefinitionCollectionMeta,
        namespace_uses: dict[str, list[str]]
    ) -> None:
        """Load and parse a single CTD file.
        
        Args:
            file_path: Path to the .gtd file
            collection: Collection to add parsed types to
            namespace_uses: Dictionary to merge namespace use declarations
        """
        parse_tree: GtdParser.GtdParser.CompilationUnitContext
        visitor: Visitor.MetaVisitor
        typedef: Meta.TypedefMeta
        enum: Meta.EnumMeta
        
        # Parse the file
        parse_tree = self._parse_file(file_path)
        
        # Create visitor and visit parse tree
        visitor = Visitor.MetaVisitor()
        visitor.visitCompilationUnit(parse_tree)
        
        # Merge visitor's collection into main collection
        for typedef in visitor.collection.typedefs:
            collection.add_typedef(typedef)
        
        for enum in visitor.collection.enums:
            collection.add_enum(enum)
        
        for structure in visitor.collection.structures:
            collection.add_structure(structure)
        
        for function in visitor.collection.functions:
            collection.add_function(function)
        
        # Merge namespace uses
        for ns, used_list in visitor.namespace_uses.items():
            if ns not in namespace_uses:
                namespace_uses[ns] = []
            namespace_uses[ns].extend(used_list)
    
    def _parse_file(self, file_path: Api.FilePath) -> GtdParser.GtdParser.CompilationUnitContext:
        """Parse a CTD file using ANTLR4.
        
        Args:
            file_path: Path to the .gtd file
            
        Returns:
            Parse tree root node
        """
        content: str
        input_stream: Antlr4.InputStream
        lexer: GtdLexer.GtdLexer
        token_stream: Antlr4.CommonTokenStream
        parser: GtdParser.GtdParser
        
        # Read file content
        content = file_path.read_text(encoding='utf-8')
        
        # Create ANTLR4 input stream
        input_stream = Antlr4.InputStream(content)
        
        # Create lexer
        lexer = GtdLexer.GtdLexer(input_stream)
        
        # Create token stream
        token_stream = Antlr4.CommonTokenStream(lexer)
        
        # Create parser
        parser = GtdParser.GtdParser(token_stream)
        
        # Parse and return compilation unit
        return parser.compilationUnit()
