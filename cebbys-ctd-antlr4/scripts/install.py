#!/usr/bin/env python3
"""Install script for cebbys-ctd-antlr4 module.

Downloads and installs all necessary dependencies.
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


def install() -> int:
    """Install dependencies."""
    print("=" * 70)
    print("Installing cebbys-ctd-antlr4 dependencies")
    print("=" * 70)

    print("\nSyncing dependencies...")
    if not run_command(["uv", "sync"], cwd=MODULE_ROOT):
        print("[ERROR] Failed to sync dependencies")
        return 1

    print("\n[OK] Dependencies installed successfully")
    return 0


if __name__ == "__main__":
    System.exit(install())
