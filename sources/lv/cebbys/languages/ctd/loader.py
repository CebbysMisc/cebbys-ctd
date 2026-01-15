"""GTD Module Loader

This module handles loading and parsing GTD (Generic Type Definition) files.
"""
import typing as Typing
import pathlib as Pathlib
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.__api__ as Api
import lv.cebbys.languages.ctd.antlr4.GtdLexer as GtdLexer
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser

__all__ = ['ModuleInfo', 'ModuleLoader']


class ModuleInfo:
    """Information about a loaded GTD module."""
    
    def __init__(self, module_path: Api.ModulePath, file_path: Api.FilePath):
        """Initialize module information.
        
        Args:
            module_path: Module path (e.g., 'this/is/path/module')
            file_path: File system path to the .gtd file
        """
        self._module_path: Api.ModulePath
        self._file_path: Api.FilePath
        self._parse_tree: GtdParser.GtdParser.CompilationUnitContext | None
        
        self._module_path = module_path
        self._file_path = file_path
        self._parse_tree = None
    
    @property
    def module_path(self) -> Api.ModulePath:
        """Get the module path."""
        return self._module_path
    
    @property
    def file_path(self) -> Api.FilePath:
        """Get the file path."""
        return self._file_path
    
    @property
    def parse_tree(self) -> GtdParser.GtdParser.CompilationUnitContext | None:
        """Get the parse tree."""
        return self._parse_tree
    
    @parse_tree.setter
    def parse_tree(self, tree: GtdParser.GtdParser.CompilationUnitContext) -> None:
        """Set the parse tree."""
        self._parse_tree = tree


class ModuleLoader:
    """Loads and parses GTD module files."""
    
    def load_modules(self, paths: list[Api.FilePath]) -> list[ModuleInfo]:
        """Load GTD modules from the given paths.
        
        Iterates through paths recursively, discovering .gtd files and parsing them.
        
        Args:
            paths: List of file or directory paths to search for .gtd files
            
        Returns:
            List of ModuleInfo objects containing parsed module data
        """
        modules: list[ModuleInfo]
        path: Api.FilePath
        
        modules = []
        
        for path in paths:
            if path.is_file() and path.suffix == '.gtd':
                module_info = self._load_module_file(path)
                modules.append(module_info)
            elif path.is_dir():
                discovered = self._discover_modules(path)
                modules.extend(discovered)
        
        return modules
    
    def _discover_modules(self, directory: Api.FilePath) -> list[ModuleInfo]:
        """Recursively discover GTD modules in a directory.
        
        Args:
            directory: Directory path to search
            
        Returns:
            List of discovered ModuleInfo objects
        """
        modules: list[ModuleInfo]
        gtd_file: Api.FilePath
        
        modules = []
        
        for gtd_file in directory.rglob('*.gtd'):
            if gtd_file.is_file():
                module_info = self._load_module_file(gtd_file)
                modules.append(module_info)
        
        return modules
    
    def _load_module_file(self, file_path: Api.FilePath) -> ModuleInfo:
        """Load and parse a single GTD module file.
        
        Args:
            file_path: Path to the .gtd file
            
        Returns:
            ModuleInfo object with parsed data
        """
        module_path: Api.ModulePath
        module_info: ModuleInfo
        
        # Convert file path to module path (e.g., 'path/to/module.gtd' -> 'path/to/module')
        module_path = str(file_path.with_suffix('')).replace('\\', '/')
        
        # Create module info
        module_info = ModuleInfo(module_path, file_path)
        
        # Parse the file
        parse_tree = self._parse_file(file_path)
        module_info.parse_tree = parse_tree
        
        return module_info
    
    def _parse_file(self, file_path: Api.FilePath) -> GtdParser.GtdParser.CompilationUnitContext:
        """Parse a GTD file using ANTLR4.
        
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
