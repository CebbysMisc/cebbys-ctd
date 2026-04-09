"""CTD Parser

This module provides the CtdParser class for parsing CTD content strings
into ANTLR4 parse tree contexts.
"""
from antlr4 import InputStream, CommonTokenStream
from lv.cebbys.languages.ctd.antlr4.__generated__.CtdLexer import CtdLexer
from lv.cebbys.languages.ctd.antlr4.__generated__ import CtdParser as GeneratedCtdParser

__all__ = ['CtdParser']


class CtdParser:
    """Parser for CTD content strings.

    CtdParser provides a high-level API for parsing CTD source code into
    ANTLR4 parse tree contexts. It handles the creation of lexer, token stream,
    and parser internally.

    Examples:
    ```python
        parser = CtdParser()

        # Parse a full compilation unit
        parse_tree = parser.moduleDeclaration('''
            namespace example {
                typedef int MyInt
            }
        ''')

        # Parse just a namespace declaration
        ns_tree = parser.namespaceDeclaration('''
            namespace example::nested {
                typedef int MyInt
            }
        ''')

        # Parse just an interface declaration
        iface_tree = parser.interfaceDeclaration('''
            interface IExample {
                Void doSomething()
            }
        ''')
    ```
    """

    @staticmethod
    def _parse(content: str) -> GeneratedCtdParser.CtdParser:
        """Create an ANTLR4 parser for the given content.

        Args:
            content: CTD source code as a string

        Returns:
            Configured CtdParser ready for parsing
        """
        input_stream = InputStream(content)
        lexer = CtdLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        return GeneratedCtdParser.CtdParser(token_stream)

    # =========================================================================
    # Top-level parsing methods
    # =========================================================================

    @staticmethod
    def moduleDeclaration(content: str) -> GeneratedCtdParser.CtdParser.ModuleDeclarationContext:
        """Parse a complete CTD source file.

        Args:
            content: Complete CTD source code

        Returns:
            ModuleDeclarationContext parse tree
        """
        return CtdParser._parse(content).moduleDeclaration()

    def namespaceDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.NamespaceDeclarationContext:
        """Parse a namespace declaration.

        Args:
            content: Namespace declaration (e.g., "namespace foo::bar { ... }")

        Returns:
            NamespaceDeclarationContext parse tree
        """
        return CtdParser._parse(content).namespaceDeclaration()

    def importDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.ImportDeclarationContext:
        """Parse an import declaration.

        Args:
            content: Import declaration (e.g., 'import "std-types"')

        Returns:
            ImportDeclarationContext parse tree
        """
        return CtdParser._parse(content).importDeclaration()

    def useDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.UseDeclarationContext:
        """Parse a use declaration.

        Args:
            content: Use declaration (e.g., "use std::lib")

        Returns:
            UseDeclarationContext parse tree
        """
        return CtdParser._parse(content).useDeclaration()

    def declaration(self, content: str) -> GeneratedCtdParser.CtdParser.DeclarationContext:
        """Parse any declaration (typedef, enum, struct, interface, function, etc.).

        Args:
            content: Any type declaration

        Returns:
            DeclarationContext parse tree
        """
        return CtdParser._parse(content).declaration()

    # =========================================================================
    # Type declaration parsing methods
    # =========================================================================

    def typedefDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.TypedefDeclarationContext:
        """Parse a typedef declaration.

        Args:
            content: Typedef declaration (e.g., "typedef signed int Int4")

        Returns:
            TypedefDeclarationContext parse tree
        """
        return CtdParser._parse(content).typedefDeclaration()

    def aliasDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.AliasDeclarationContext:
        """Parse an alias declaration.

        Args:
            content: Alias declaration (e.g., "alias Guid InterfaceId")

        Returns:
            AliasDeclarationContext parse tree
        """
        return CtdParser._parse(content).aliasDeclaration()

    def enumDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.EnumDeclarationContext:
        """Parse an enum declaration.

        Args:
            content: Enum declaration (e.g., "enum Color : Int4 { RED GREEN BLUE }")

        Returns:
            EnumDeclarationContext parse tree
        """
        return CtdParser._parse(content).enumDeclaration()

    def flagDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.FlagDeclarationContext:
        """Parse a flag declaration.

        Args:
            content: Flag declaration (e.g., "flag Options : Unt4 { OPT_A OPT_B }")

        Returns:
            FlagDeclarationContext parse tree
        """
        return CtdParser._parse(content).flagDeclaration()

    def structureDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.StructureDeclarationContext:
        """Parse a structure declaration.

        Args:
            content: Structure declaration (e.g., "structure Point { Int4 x Int4 y }")

        Returns:
            StructureDeclarationContext parse tree
        """
        return CtdParser._parse(content).structureDeclaration()

    def interfaceDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.InterfaceDeclarationContext:
        """Parse an interface declaration.

        Args:
            content: Interface declaration (e.g., "interface IFoo { Void bar() }")

        Returns:
            InterfaceDeclarationContext parse tree
        """
        return CtdParser._parse(content).interfaceDeclaration()

    def functionDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.FunctionDeclarationContext:
        """Parse a function declaration.

        Args:
            content: Function declaration (e.g., "Int4 add(Int4 a, Int4 b)")

        Returns:
            FunctionDeclarationContext parse tree
        """
        return CtdParser._parse(content).functionDeclaration()

    def classDeclaration(self, content: str) -> GeneratedCtdParser.CtdParser.ClassDeclarationContext:
        """Parse a class declaration.

        Args:
            content: Class declaration (e.g., "class Foo : Bar, IBaz { Int4 x void move() }")

        Returns:
            ClassDeclarationContext parse tree
        """
        return CtdParser._parse(content).classDeclaration()

    # =========================================================================
    # Component parsing methods
    # =========================================================================

    def typeSpec(self, content: str) -> GeneratedCtdParser.CtdParser.TypeSpecContext:
        """Parse a type specification.

        Args:
            content: Type specification (e.g., "Int4", "Void *", "Unt1[8]")

        Returns:
            TypeSpecContext parse tree
        """
        return CtdParser._parse(content).typeSpec()
