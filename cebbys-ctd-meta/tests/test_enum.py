"""Stage 1: Test enum meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from tests.conftest import parse_ctd_file
from test_utils import TestLogger


def test_enum_parsing() -> None:
    """Test that enum declarations are parsed into EnumMeta."""
    TestLogger.header("Stage 1: Enum Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/enums.ctd'))

    # enums.ctd should have 2 enums
    assert len(visitor.collection.enums) == 2
    TestLogger.success(f"Parsed {len(visitor.collection.enums)} enums")

    # Check DriverType enum
    driver_type = visitor.collection.enums[0]
    assert driver_type.name == "DriverType"
    assert driver_type.base_type == "Int4"
    assert len(driver_type.members) == 6
    TestLogger.success(f"Enum: {driver_type.name} : {driver_type.base_type}")

    # Check member names
    expected_members = ['UNKNOWN', 'HARDWARE', 'REFERENCE', 'NULL', 'SOFTWARE', 'WARP']
    for i, member in enumerate(driver_type.members):
        assert member.name == expected_members[i]
        TestLogger.info(f"{member.name} = {member.value}", indent=2)

    TestLogger.complete("Enum meta loading test passed")


def test_enum_with_hex_values() -> None:
    """Test enum with hexadecimal values."""
    TestLogger.header("Stage 1: Enum with Hex Values")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/enums.ctd'))

    # FeatureLevel enum has hex values
    feature_level = visitor.collection.enums[1]
    assert feature_level.name == "FeatureLevel"
    assert len(feature_level.members) == 10
    TestLogger.success(f"Enum: {feature_level.name} with {len(feature_level.members)} members")

    # Check first member has hex value
    first_member = feature_level.members[0]
    assert first_member.name == "LEVEL_9_1"
    assert first_member.value == 0x9100
    TestLogger.success(f"First member: {first_member.name} = 0x{first_member.value:X}")

    TestLogger.complete("Enum hex values test passed")


def test_enum_auto_increment() -> None:
    """Test enum members without explicit values (auto-increment)."""
    TestLogger.header("Stage 1: Enum Auto-Increment")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/enums.ctd'))

    driver_type = visitor.collection.enums[0]

    # Members without explicit values should have None at meta stage
    # Actual value assignment (auto-increment) happens during resolution phase
    for member in driver_type.members:
        assert member.value is None
        TestLogger.info(f"{member.name} value is None (deferred)", indent=2)

    TestLogger.complete("Enum auto-increment test passed")
