"""CTD Context Parser

This module provides the CtdContextParser class for parsing CTD content strings
into ANTLR4 parse tree contexts.
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4

__all__ = ['CtdContextParser']


class CtdContextParser:
    """Parser for CTD content strings.

    CtdContextParser provides a high-level API for parsing CTD source code into
    ANTLR4 parse tree contexts. It handles the creation of lexer, token stream,
    and parser internally.

    Examples:
    ```python
        parser = CtdContextParser()

        # Parse a full compilation unit
        parse_tree = parser.parseCompilationUnit('''
            namespace example {
                typedef int MyInt
            }
        ''')

        # Parse just a namespace declaration
        ns_tree = parser.parseNamespaceDeclaration('''
            namespace example::nested {
                typedef int MyInt
            }
        ''')

        # Parse just an interface declaration
        iface_tree = parser.parseInterfaceDeclaration('''
            interface IExample {
                Void doSomething()
            }
        ''')
    ```
    """

    def _createParser(self, content: str) -> Antlr4.CtdParser:
        """Create an ANTLR4 parser for the given content.

        Args:
            content: CTD source code as a string

        Returns:
            Configured CtdParser ready for parsing
        """
        input_stream: Antlr4.InputStream
        lexer: Antlr4.CtdLexer
        token_stream: Antlr4.CommonTokenStream

        input_stream = Antlr4.InputStream(content)
        lexer = Antlr4.CtdLexer(input_stream)
        token_stream = Antlr4.CommonTokenStream(lexer)

        return Antlr4.CtdParser(token_stream)

    # =========================================================================
    # Top-level parsing methods
    # =========================================================================

    def parseCompilationUnit(self, content: str) -> Antlr4.CtdParser.CompilationUnitContext:
        """Parse a complete CTD source file.

        Args:
            content: Complete CTD source code

        Returns:
            CompilationUnitContext parse tree
        """
        return self._createParser(content).compilationUnit()

    def parseNamespaceDeclaration(self, content: str) -> Antlr4.CtdParser.NamespaceDeclarationContext:
        """Parse a namespace declaration.

        Args:
            content: Namespace declaration (e.g., "namespace foo::bar { ... }")

        Returns:
            NamespaceDeclarationContext parse tree
        """
        return self._createParser(content).namespaceDeclaration()

    def parseImportDeclaration(self, content: str) -> Antlr4.CtdParser.ImportDeclarationContext:
        """Parse an import declaration.

        Args:
            content: Import declaration (e.g., 'import "std-types"')

        Returns:
            ImportDeclarationContext parse tree
        """
        return self._createParser(content).importDeclaration()

    def parseUseDeclaration(self, content: str) -> Antlr4.CtdParser.UseDeclarationContext:
        """Parse a use declaration.

        Args:
            content: Use declaration (e.g., "use std::lib")

        Returns:
            UseDeclarationContext parse tree
        """
        return self._createParser(content).useDeclaration()

    def parseDeclaration(self, content: str) -> Antlr4.CtdParser.DeclarationContext:
        """Parse any declaration (typedef, enum, struct, interface, function, etc.).

        Args:
            content: Any type declaration

        Returns:
            DeclarationContext parse tree
        """
        return self._createParser(content).declaration()

    # =========================================================================
    # Type declaration parsing methods
    # =========================================================================

    def parseTypedefDeclaration(self, content: str) -> Antlr4.CtdParser.TypedefDeclarationContext:
        """Parse a typedef declaration.

        Args:
            content: Typedef declaration (e.g., "typedef signed int Int4")

        Returns:
            TypedefDeclarationContext parse tree
        """
        return self._createParser(content).typedefDeclaration()

    def parseAliasDeclaration(self, content: str) -> Antlr4.CtdParser.AliasDeclarationContext:
        """Parse an alias declaration.

        Args:
            content: Alias declaration (e.g., "alias Guid InterfaceId")

        Returns:
            AliasDeclarationContext parse tree
        """
        return self._createParser(content).aliasDeclaration()

    def parseEnumDeclaration(self, content: str) -> Antlr4.CtdParser.EnumDeclarationContext:
        """Parse an enum declaration.

        Args:
            content: Enum declaration (e.g., "enum Color : Int4 { RED GREEN BLUE }")

        Returns:
            EnumDeclarationContext parse tree
        """
        return self._createParser(content).enumDeclaration()

    def parseFlagDeclaration(self, content: str) -> Antlr4.CtdParser.FlagDeclarationContext:
        """Parse a flag declaration.

        Args:
            content: Flag declaration (e.g., "flag Options : Unt4 { OPT_A OPT_B }")

        Returns:
            FlagDeclarationContext parse tree
        """
        return self._createParser(content).flagDeclaration()

    def parseStructureDeclaration(self, content: str) -> Antlr4.CtdParser.StructureDeclarationContext:
        """Parse a structure declaration.

        Args:
            content: Structure declaration (e.g., "structure Point { Int4 x Int4 y }")

        Returns:
            StructureDeclarationContext parse tree
        """
        return self._createParser(content).structureDeclaration()

    def parseInterfaceDeclaration(self, content: str) -> Antlr4.CtdParser.InterfaceDeclarationContext:
        """Parse an interface declaration.

        Args:
            content: Interface declaration (e.g., "interface IFoo { Void bar() }")

        Returns:
            InterfaceDeclarationContext parse tree
        """
        return self._createParser(content).interfaceDeclaration()

    def parseFunctionDeclaration(self, content: str) -> Antlr4.CtdParser.FunctionDeclarationContext:
        """Parse a function declaration.

        Args:
            content: Function declaration (e.g., "Int4 add(Int4 a, Int4 b)")

        Returns:
            FunctionDeclarationContext parse tree
        """
        return self._createParser(content).functionDeclaration()

    # =========================================================================
    # Component parsing methods
    # =========================================================================

    def parseTypeSpec(self, content: str) -> Antlr4.CtdParser.TypeSpecContext:
        """Parse a type specification.

        Args:
            content: Type specification (e.g., "Int4", "Void *", "Unt1[8]")

        Returns:
            TypeSpecContext parse tree
        """
        return self._createParser(content).typeSpec()
