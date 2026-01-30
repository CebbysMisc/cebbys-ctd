"""Meta Parser

This module provides the MetaParser class for parsing CTD content strings
into ANTLR4 parse trees.
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4

__all__ = ['MetaParser']


class MetaParser:
    """Parser for CTD content strings.

    MetaParser provides a high-level API for parsing CTD source code into
    ANTLR4 parse trees. It handles the creation of lexer, token stream,
    and parser internally.

    Examples:
    ```python
        parser = MetaParser()
        parse_tree = parser.parseCompilationUnit('''
            namespace example {
                typedef int MyInt
            }
        ''')
    ```
    """

    def parseCompilationUnit(self, content: str) -> Antlr4.CtdParser.CompilationUnitContext:
        """Parse a CTD source string into a CompilationUnitContext.

        Takes a string containing CTD source code and parses it using ANTLR4,
        returning the root of the parse tree (CompilationUnitContext).

        Args:
            content: CTD source code as a string

        Returns:
            The root CompilationUnitContext of the parse tree
        """
        input_stream: Antlr4.InputStream
        lexer: Antlr4.CtdLexer
        token_stream: Antlr4.CommonTokenStream
        parser: Antlr4.CtdParser

        input_stream = Antlr4.InputStream(content)
        lexer = Antlr4.CtdLexer(input_stream)
        token_stream = Antlr4.CommonTokenStream(lexer)
        parser = Antlr4.CtdParser(token_stream)

        return parser.compilationUnit()
