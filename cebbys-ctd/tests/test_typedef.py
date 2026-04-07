"""Test for Typedef declaration resolution to builtin types."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.types.ctd as Ctd
from conftest import TestLogger

_BUILTIN_BYTE_SIZES: dict[str, int] = {
    "byte":  1,
    "short": 2,
    "int":   4,
    "long":  8,
}


def test_typedef_resolution_to_builtin_numbers() -> None:
    """Test typedef declarations resolve to correct builtin base types and signedness."""
    loader: Loader.CtdLoader
    test_dir: Pathlib.Path
    typedefs: dict[str, Ctd.Typedef]

    TestLogger.header("Typedef: Resolution to Builtin Numbers")

    test_dir = Pathlib.Path(__file__).parent / "resources" / "cases" / "0001-typedef-resolution-to-builtin-numbers"
    assert test_dir.exists(), f"Test directory not found: {test_dir}"

    loader = Loader.CtdLoader([test_dir])
    typedefs = {
        key: decl
        for key, decl in loader.definitions.items()
        if isinstance(decl, Ctd.Typedef)
    }

    builtin_count = len(loader.definitions) - len(typedefs)
    TestLogger.info(f"Found {len(typedefs)} typedef(s), filtered {builtin_count} builtin(s)")
    assert len(typedefs) == 12, f"Expected 12 typedefs, got {len(typedefs)}"

    def check(name: str, expected_size: int, expected_signed: bool | None) -> None:
        key = f"test::resolution::{name}"
        typedef = typedefs.get(key)
        assert typedef is not None, f"Typedef '{name}' not found (key: '{key}')"

        base: Ctd.Declaration = typedef.base.value
        assert isinstance(base, Ctd.Builtin), (
            f"{name}: expected Builtin base, got {type(base).__name__}"
        )

        actual_size = _BUILTIN_BYTE_SIZES.get(base.name)
        assert actual_size is not None, f"{name}: unknown builtin name '{base.name}'"
        assert actual_size == expected_size, (
            f"{name}: expected byte size {expected_size}, got {actual_size} (base: '{base.name}')"
        )

        assert typedef.signed == expected_signed, (
            f"{name}: expected signed={expected_signed!r}, got {typedef.signed!r}"
        )
        TestLogger.info(f"  {name}: base={base.name} size={actual_size} signed={typedef.signed} OK")

    config: list[tuple[str, bool|None]] = [ ("U", False), ("S", True), ("I", None) ]
    for l, sign in config:
        TestLogger.info(f"Checking {l}nt{{N}} typedefs (signed: {sign})...")
        for i in [1, 2, 4, 8]:
            check(f"{l}nt{i}", i, sign)

    TestLogger.success("All typedef declarations resolved correctly")
    TestLogger.complete("Test passed")
