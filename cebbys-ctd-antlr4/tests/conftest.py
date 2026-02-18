"""Pytest configuration for antlr4 tests."""


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


__all__ = ['TestLogger']
