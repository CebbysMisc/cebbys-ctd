import typing as Typing
import sys as System

# fmt: off
import pathlib as Pathlib
import sys as System
path = Pathlib.Path(__file__).parent.parent.parent / "sources"
System.path.insert(0, str(path))
# fmt: on


def test_ctd_visitor() -> None:
    """Test that the visitor is correctly working."""
    import lv.cebbys.languages.ctd.antlr4 as Ctd
    import antlr4 as Antlr4
    
    Antlr4.ParseTreeVisitor

    content: str
    input_stream: Antlr4.InputStream
    lexer: Ctd.CtdLexer
    token_stream: Antlr4.CommonTokenStream
    parser: Ctd.CtdParser

    # Read file content
    # fmt: off
    content = \
"""
namespace test::name {
    typedef int Int4
}
"""
    # fmt: on

    # Create ANTLR4 input stream
    input_stream = Antlr4.InputStream(content)

    # Create lexer
    lexer = Ctd.CtdLexer(input_stream)

    # Create token stream
    token_stream = Antlr4.CommonTokenStream(lexer)

    # Create parser
    parser = Ctd.CtdParser(token_stream)

    # Parse and return compilation unit
    unit = parser.compilationUnit()


def main() -> int:
    test_ctd_visitor()
    return 0


def log_properties(clazz: Typing.Any):
    properties = {
        p: getattr(type, p) for p in dir(type) if not p.startswith("__")
    }
    for k, v in properties.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    System.exit(main())
