"""Pytest configuration for resolver tests."""
import pathlib as Pathlib
import pytest as Pytest
import lv.cebbys.languages.ctd.utility.logging as CtdLogging


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


def get_resource_path(relative_path: str) -> Pathlib.Path:
    """Get absolute path to a resource file relative to module root."""
    module_root = Pathlib.Path(__file__).parent.parent
    return module_root / relative_path


def load_meta_collection(paths: list[Pathlib.Path]) -> tuple:
    """Load meta collection from CTD files."""
    # Import here to avoid top-level cross-module dependencies
    import antlr4 as Antlr4
    import lv.cebbys.languages.ctd.antlr4 as CtdAntlr4
    import lv.cebbys.languages.ctd.meta.parser as MetaParser
    import lv.cebbys.languages.ctd.types.meta as TypeMeta
    
    meta_collection = TypeMeta.DefinitionCollectionMeta()
    namespace_uses = {}
    
    for file_path in paths:
        content = file_path.read_text(encoding='utf-8')
        input_stream = Antlr4.InputStream(content)
        lexer = CtdAntlr4.CtdLexer(input_stream)
        token_stream = Antlr4.CommonTokenStream(lexer)
        parser = CtdAntlr4.CtdGrammar(token_stream)
        parse_tree = parser.moduleDeclaration()
        
        # Parse module
        module_meta = MetaParser.CtdMetaParser.parse_module(parse_tree)
        
        # Extract declarations from all namespaces
        for namespace_meta in module_meta.namespaces:
            # Add each declaration individually to the meta_collection
            for decl in namespace_meta.declarations:
                if hasattr(decl, '__class__'):
                    add_method_name = f"add_{decl.__class__.__name__.replace('Meta', '').lower()}"
                    if hasattr(meta_collection, add_method_name):
                        getattr(meta_collection, add_method_name)(decl)
            
            # Collect namespace uses
            for used_ns in namespace_meta.uses:
                ns_path = namespace_meta.path
                if ns_path not in namespace_uses:
                    namespace_uses[ns_path] = []
                namespace_uses[ns_path].append(used_ns)
    
    return meta_collection, namespace_uses


@Pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for test runs - enable TRACE level."""
    CtdLogging.configure_logging(
        level=CtdLogging.LogLevel.TRACE,
        colored=True
    )


__all__ = ['TestLogger', 'configure_logging', 'get_resource_path', 'load_meta_collection']
