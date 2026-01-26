"""Stage 1: Test flag meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from tests.conftest import parse_ctd_file
from test_utils import TestLogger


def test_flag_parsing() -> None:
    """Test that flag declarations are parsed into FlagMeta."""
    TestLogger.header("Stage 1: Flag Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/flags.ctd'))

    # flags.ctd should have 1 flag
    assert len(visitor.collection.flags) == 1
    TestLogger.success(f"Parsed {len(visitor.collection.flags)} flags")

    # Check CreateDeviceFlag
    create_device_flag = visitor.collection.flags[0]
    assert create_device_flag.name == "CreateDeviceFlag"
    assert create_device_flag.base_type == "Unt4"
    assert len(create_device_flag.members) == 9
    TestLogger.success(f"Flag: {create_device_flag.name} : {create_device_flag.base_type}")

    # Check member names
    expected_members = [
        'SINGLETHREADED', 'DEBUG', 'SWITCH_TO_REF',
        'PREVENT_INTERNAL_THREADING_OPTIMIZATIONS', 'BGRA_SUPPORT',
        'DEBUGGABLE', 'PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY',
        'DISABLE_GPU_TIMEOUT', 'VIDEO_SUPPORT'
    ]
    for i, member in enumerate(create_device_flag.members):
        assert member.name == expected_members[i]
        TestLogger.info(f"{member.name}", indent=2)

    TestLogger.complete("Flag meta loading test passed")


def test_flag_with_manual_offset() -> None:
    """Test flag members with manual bit offset."""
    TestLogger.header("Stage 1: Flag with Manual Offset")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/flags.ctd'))

    create_device_flag = visitor.collection.flags[0]

    # BGRA_SUPPORT has manual offset = 5 (which means bit 5, value 0x20)
    bgra_member = next(m for m in create_device_flag.members if m.name == 'BGRA_SUPPORT')
    # In meta, this is stored as the raw offset value from the grammar
    assert bgra_member.value == 0x20  # hex literal parsed from file
    TestLogger.success(f"BGRA_SUPPORT has offset value 0x{bgra_member.value:X}")

    # Members without explicit value have None
    first_member = create_device_flag.members[0]
    assert first_member.value is None
    TestLogger.success("SINGLETHREADED has None (auto bit-shift)")

    TestLogger.complete("Flag manual offset test passed")
