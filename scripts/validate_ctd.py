#!/usr/bin/env python3
"""Validate CTD files and display loaded datatypes.

This script loads all CTD files from resources/ctd and displays
the loaded datatypes. If an error occurs, it logs the exception.
"""
import pathlib as Pathlib
import sys
import traceback

# Add sources to path (must be before importing lv.cebbys modules)
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent / 'sources'))

import lv.cebbys.languages.ctd as Ctd


def main() -> int:
    """Load and validate CTD files."""
    ctd_path = Pathlib.Path('resources/ctd')

    print("=" * 70)
    print("CTD Validation")
    print("=" * 70)
    print(f"Loading from: {ctd_path.absolute()}")
    print()

    try:
        loader = Ctd.Loader.CtdLoader([ctd_path])
        collection = loader.load()

        # Print typedefs
        if collection.typedefs:
            print(f"Typedefs ({len(collection.typedefs)}):")
            print("-" * 40)
            for name, typedef in sorted(collection.typedefs.items()):
                print(f"  {name} ({typedef} basetype)")
            print()

        # Print enums
        if collection.enums:
            print(f"Enums ({len(collection.enums)}):")
            print("-" * 40)
            for name, enum in sorted(collection.enums.items()):
                print(f"  {name} ({len(enum.members)} members)")
            print()

        # Print flags
        if collection.flags:
            print(f"Flags ({len(collection.flags)}):")
            print("-" * 40)
            for name, flag in sorted(collection.flags.items()):
                print(f"  {name} ({len(flag.members)} members)")
            print()

        # Print structures
        if collection.structures:
            print(f"Structures ({len(collection.structures)}):")
            print("-" * 40)
            for name, struct in sorted(collection.structures.items()):
                print(f"  {name} ({len(struct.members)} members)")
            print()

        # Print functions
        if collection.functions:
            print(f"Functions ({len(collection.functions)}):")
            print("-" * 40)
            for name, func in sorted(collection.functions.items()):
                print(f"  {name} ({len(func.parameters)} params)")
            print()

        # Summary
        total = (len(collection.typedefs) + len(collection.enums) +
                 len(collection.flags) + len(collection.structures) +
                 len(collection.functions))

        print("=" * 70)
        print(f"[OK] Validation passed - {total} definitions loaded")
        print("=" * 70)
        return 0

    except Exception as e:
        print("=" * 70)
        print(f"[ERROR] Validation failed")
        print("=" * 70)
        print()
        print(f"Exception: {type(e).__name__}")
        print(f"Message: {e}")
        print()
        print("Traceback:")
        print("-" * 40)
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
