"""Shared test utilities for all modules."""
import pathlib as Pathlib


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


def get_workspace_root() -> Pathlib.Path:
    """Get the workspace root directory."""
    return Pathlib.Path(__file__).parent


def get_module_root(module_name: str) -> Pathlib.Path:
    """Get the root path of a module within the workspace."""
    return get_workspace_root() / module_name
