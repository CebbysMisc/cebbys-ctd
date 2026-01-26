#!/usr/bin/env python3
"""Build script for cebbys-ctd-antlr4 module.

Generates ANTLR4 parser from grammar.
Triggers install first.
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


def build() -> int:
    """Build the module."""
    # Import and run install
    from install import install
    if install() != 0:
        return 1

    print("\n" + "=" * 70)
    print("Building cebbys-ctd-antlr4")
    print("=" * 70)

    grammar_file = MODULE_ROOT / "resources" / "grammar" / "Ctd.g4"
    output_dir = MODULE_ROOT / "sources" / "lv" / "cebbys" / \
        "languages" / "ctd" / "antlr4" / "__generated__"

    print("\nGenerating ANTLR4 parser...")
    if not grammar_file.exists():
        print(f"[ERROR] Grammar file not found: {grammar_file}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    antlr_args = [
        "uv", "run", "antlr4",
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        str(grammar_file),
        "-o", str(output_dir)
    ]
    if not run_command(antlr_args, cwd=MODULE_ROOT):
        print("[ERROR] Failed to generate ANTLR4 parser")
        return 1

    print("\n[OK] Build completed successfully")
    return 0


if __name__ == "__main__":
    System.exit(build())
