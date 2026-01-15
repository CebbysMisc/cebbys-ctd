"""Utilities for test logging and output."""

__all__ = ['TestLogger']


class TestLogger:
    """Unified test logging utility."""
    
    @staticmethod
    def header(title: str) -> None:
        """Print a test section header.
        
        Args:
            title: Section title
        """
        print("\n" + "=" * 70)
        print(title)
        print("=" * 70)
    
    @staticmethod
    def success(message: str) -> None:
        """Print a success message.
        
        Args:
            message: Success message
        """
        print(f"[OK] {message}")
    
    @staticmethod
    def info(message: str, indent: int = 0) -> None:
        """Print an info message.
        
        Args:
            message: Info message
            indent: Number of spaces to indent (default: 0)
        """
        prefix = " " * indent
        print(f"{prefix}{message}")
    
    @staticmethod
    def complete(message: str = "Test complete") -> None:
        """Print test completion message.
        
        Args:
            message: Completion message
        """
        print(f"\n[PASS] {message}")
    
    @staticmethod
    def section_break() -> None:
        """Print a section break."""
        print()
