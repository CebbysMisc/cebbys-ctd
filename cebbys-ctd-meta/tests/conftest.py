"""Shared test fixtures and utilities."""
import pathlib as Pathlib
import pytest as Pytest
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.visitor as Visitor
import lv.cebbys.languages.ctd.meta as MetaLoader
import lv.cebbys.languages.ctd.antlr4 as CtdAntlr4

# Resources are in the module directory
_MODULE_ROOT = Pathlib.Path(__file__).parent.parent


def get_resource_path(relative_path: str) -> Pathlib.Path:
    """Get absolute path to a resource file relative to module root."""
    return _MODULE_ROOT / relative_path


@Pytest.fixture
def std_types_path() -> Pathlib.Path:
    """Path to std-types.ctd file."""
    return _MODULE_ROOT / 'resources/test/ctd/std-types.ctd'


@Pytest.fixture
def test_ctd_path() -> Pathlib.Path:
    """Path to resources/test/ctd directory."""
    return _MODULE_ROOT / 'resources/test/ctd'


def parse_ctd_file(file_path: Pathlib.Path) -> Visitor.MetaVisitor:
    """Parse a CTD file and return the visitor with collected meta objects.

    Args:
        file_path: Path to the CTD file (relative to project root or absolute)

    Returns:
        MetaVisitor with parsed meta objects in visitor.collection
    """
    # Resolve relative paths to module root
    if not file_path.is_absolute():
        file_path = _MODULE_ROOT / file_path

    content = file_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = CtdAntlr4.CtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = CtdAntlr4.CtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    return visitor
