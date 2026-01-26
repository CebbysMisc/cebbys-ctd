#!/usr/bin/env python3
"""Test script for cebbys-ctd-antlr4 module.

Runs tests for the module.
Triggers install and build first.
"""
import pathlib as Pathlib
import subprocess as Subprocess
import sys as System

MODULE_ROOT = Pathlib.Path(__file__).parent.parent


def run_command(args: list[str], cwd: Pathlib.Path | None = None) -> bool:
    """Run a command and return success status."""
    print(f"  Running: {' '.join(args)}")
    result = Subprocess.run(args, cwd=cwd)
    return result.returncode == 0


def test() -> int:
    """Test the module."""
    # Import and run build (which runs install)
    from build import build
    if build() != 0:
        return 1

    print("\n" + "=" * 70)
    print("Testing cebbys-ctd-antlr4")
    print("=" * 70)

    test_dir = MODULE_ROOT / "tests"
    test_files = list(test_dir.glob("test_*.py")) if test_dir.exists() else []

    if not test_files:
        print("\n[SKIP] No tests found")
        return 0

    print("\nRunning tests...")
    if not run_command(["uv", "run", "pytest", "tests/", "-v", "-s"], cwd=MODULE_ROOT):
        print("[ERROR] Tests failed")
        return 1

    print("\n[OK] All tests passed")
    return 0


if __name__ == "__main__":
    System.exit(test())
