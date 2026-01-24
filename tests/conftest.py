"""Shared test fixtures and utilities."""
import pathlib as Pathlib
import pytest as Pytest
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.meta.loader as MetaLoader
import lv.cebbys.languages.ctd.antlr4.GtdLexer as GtdLexer
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser


@Pytest.fixture
def std_types_path() -> Pathlib.Path:
    """Path to std-types.ctd file."""
    return Pathlib.Path('resources/ctd/std-types.ctd')


@Pytest.fixture
def d3d11_path() -> Pathlib.Path:
    """Path to d3d11.ctd file."""
    return Pathlib.Path('resources/ctd/d3d11.ctd')


@Pytest.fixture
def dxgi_path() -> Pathlib.Path:
    """Path to dxgi.ctd file."""
    return Pathlib.Path('resources/ctd/dxgi.ctd')


@Pytest.fixture
def guiddef_path() -> Pathlib.Path:
    """Path to guiddef.ctd file."""
    return Pathlib.Path('resources/ctd/microsoft/guiddef.ctd')


@Pytest.fixture
def unknown_path() -> Pathlib.Path:
    """Path to unknown.ctd (IUnknown interface)."""
    return Pathlib.Path('resources/ctd/microsoft/unknown.ctd')


@Pytest.fixture
def resources_ctd_path() -> Pathlib.Path:
    """Path to resources/ctd directory."""
    return Pathlib.Path('resources/ctd')


def parse_ctd_file(file_path: Pathlib.Path) -> Visitor.MetaVisitor:
    """Parse a CTD file and return the visitor with collected meta objects.

    Args:
        file_path: Path to the CTD file

    Returns:
        MetaVisitor with parsed meta objects in visitor.collection
    """
    content = file_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    return visitor
