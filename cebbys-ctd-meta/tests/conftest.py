"""Pytest configuration for meta tests."""
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


@Pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for test runs - enable DEBUG level."""
    CtdLogging.configure_logging(
        level=CtdLogging.LogLevel.TRACE,
        colored=True
    )


__all__ = ['TestLogger', 'configure_logging']
