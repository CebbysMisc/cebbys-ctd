#!/usr/bin/env python3
"""Build script for cebbys-ctd-resolver module.

Builds the module artifact.
Triggers install first.
"""
import pathlib as Pathlib
import sys as System

MODULE_ROOT = Pathlib.Path(__file__).parent.parent


def build() -> int:
    """Build the module."""
    # Import and run install
    from install import install
    if install() != 0:
        return 1

    print("\n" + "=" * 70)
    print("Building cebbys-ctd-resolver")
    print("=" * 70)

    # No additional build steps required for this module
    print("\n[OK] Build completed successfully")
    return 0


if __name__ == "__main__":
    System.exit(build())
