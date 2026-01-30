"""Shared test fixtures and utilities for the workspace."""
import pathlib as Pathlib
import pytest as Pytest
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.visitor as Visitor
import lv.cebbys.languages.ctd.antlr4 as CtdAntlr4

# Workspace root
_WORKSPACE_ROOT = Pathlib.Path(__file__).parent


def get_module_root(module_name: str) -> Pathlib.Path:
    """Get the root path of a module within the workspace."""
    return _WORKSPACE_ROOT / module_name


def get_resource_path(relative_path: str, module_name: str = 'cebbys-ctd-resolver') -> Pathlib.Path:
    """Get absolute path to a resource file relative to a module root.

    Args:
        relative_path: Path relative to the module root
        module_name: Module name (defaults to cebbys-ctd-resolver for backwards compatibility)

    Returns:
        Absolute path to the resource
    """
    return get_module_root(module_name) / relative_path


def parse_ctd_file(file_path: Pathlib.Path, module_root: Pathlib.Path | None = None) -> Visitor.MetaVisitor:
    """Parse a CTD file and return the visitor with collected meta objects.

    Args:
        file_path: Path to the CTD file (absolute or relative to module_root)
        module_root: Root path for resolving relative paths (defaults to cebbys-ctd-meta)

    Returns:
        MetaVisitor with parsed meta objects in visitor.collection
    """
    if module_root is None:
        module_root = get_module_root('cebbys-ctd-meta')

    # Resolve relative paths to module root
    if not file_path.is_absolute():
        file_path = module_root / file_path

    content = file_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = CtdAntlr4.CtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = CtdAntlr4.CtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    return visitor


# Meta module fixtures
@Pytest.fixture
def meta_module_root() -> Pathlib.Path:
    """Root path of cebbys-ctd-meta module."""
    return get_module_root('cebbys-ctd-meta')


@Pytest.fixture
def meta_std_types_path(meta_module_root: Pathlib.Path) -> Pathlib.Path:
    """Path to std-types.ctd file in meta module."""
    return meta_module_root / 'resources/test/ctd/std-types.ctd'


@Pytest.fixture
def meta_test_ctd_path(meta_module_root: Pathlib.Path) -> Pathlib.Path:
    """Path to resources/test/ctd directory in meta module."""
    return meta_module_root / 'resources/test/ctd'


# Resolver module fixtures
@Pytest.fixture
def resolver_module_root() -> Pathlib.Path:
    """Root path of cebbys-ctd-resolver module."""
    return get_module_root('cebbys-ctd-resolver')


@Pytest.fixture
def resolver_std_types_path(resolver_module_root: Pathlib.Path) -> Pathlib.Path:
    """Path to std-types.ctd file in resolver module."""
    return resolver_module_root / 'resources/test/ctd/std-types.ctd'


@Pytest.fixture
def resolver_test_ctd_path(resolver_module_root: Pathlib.Path) -> Pathlib.Path:
    """Path to resources/test/ctd directory in resolver module."""
    return resolver_module_root / 'resources/test/ctd'


# Backwards compatibility - generic fixtures that use meta module paths
@Pytest.fixture
def std_types_path(meta_std_types_path: Pathlib.Path) -> Pathlib.Path:
    """Path to std-types.ctd file (defaults to meta module)."""
    return meta_std_types_path


@Pytest.fixture
def test_ctd_path(meta_test_ctd_path: Pathlib.Path) -> Pathlib.Path:
    """Path to resources/test/ctd directory (defaults to meta module)."""
    return meta_test_ctd_path


# Shared test utilities
class TestLogger:
    """Unified test logging utility."""

    @staticmethod
    def header(title: str) -> None:
        """Print a test section header."""
        print("\n" + "=" * 70)
        print(title)
        print("=" * 70)

    @staticmethod
    def success(message: str) -> None:
        """Print a success message."""
        print(f"[OK] {message}")

    @staticmethod
    def info(message: str, indent: int = 0) -> None:
        """Print an info message."""
        prefix = " " * indent
        print(f"{prefix}{message}")

    @staticmethod
    def complete(message: str = "Test complete") -> None:
        """Print test completion message."""
        print(f"\n[PASS] {message}")

    @staticmethod
    def section_break() -> None:
        """Print a section break."""
        print()
