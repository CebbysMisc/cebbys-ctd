"""Stage 1: Test structure meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_structure_parsing() -> None:
    """Test that structure declarations are parsed into StructureMeta."""
    TestLogger.header("Stage 1: Structure Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/dxgi.ctd'))

    # dxgi.ctd should have 5 structures
    assert len(visitor.collection.structures) == 5
    TestLogger.success(f"Parsed {len(visitor.collection.structures)} structures")

    # Check Rational structure
    rational = visitor.collection.structures[0]
    assert rational.name == "Rational"
    assert len(rational.members) == 2
    TestLogger.success(f"Structure: {rational.name} with {len(rational.members)} members")

    # Check member types and names
    assert rational.members[0].name == "numerator"
    assert rational.members[0].type_spec == "Unt4"
    assert rational.members[1].name == "denominator"
    assert rational.members[1].type_spec == "Unt4"

    for member in rational.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=2)

    TestLogger.complete("Structure meta loading test passed")


def test_structure_with_pointer_member() -> None:
    """Test structure with pointer type member."""
    TestLogger.header("Stage 1: Structure with Pointer Member")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/dxgi.ctd'))

    # Adapter structure has a pointer member
    adapter = next(s for s in visitor.collection.structures if s.name == 'Adapter')
    assert len(adapter.members) == 1
    assert adapter.members[0].name == "vtable"
    assert adapter.members[0].type_spec == "Any"
    TestLogger.success(f"Structure: {adapter.name}")
    TestLogger.info(f"{adapter.members[0].type_spec} {adapter.members[0].name}", indent=2)

    TestLogger.complete("Structure pointer member test passed")


def test_structure_with_array_member() -> None:
    """Test structure with array type member."""
    TestLogger.header("Stage 1: Structure with Array Member")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/guiddef.ctd'))

    # Guid structure has an array member
    guid = visitor.collection.structures[0]
    assert guid.name == "Guid"
    assert len(guid.members) == 4
    TestLogger.success(f"Structure: {guid.name} with {len(guid.members)} members")

    # data4 member should be Unt1[8]
    data4 = guid.members[3]
    assert data4.name == "data4"
    assert "[8]" in data4.type_spec
    TestLogger.success(f"Array member: {data4.type_spec} {data4.name}")

    for member in guid.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=2)

    TestLogger.complete("Structure array member test passed")
