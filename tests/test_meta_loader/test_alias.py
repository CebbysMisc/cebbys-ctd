"""Stage 1: Test alias meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_alias_parsing() -> None:
    """Test that alias declarations are parsed into AliasMeta."""
    TestLogger.header("Stage 1: Alias Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/guiddef.ctd'))

    # guiddef.ctd should have 2 aliases
    assert len(visitor.collection.aliases) == 2
    TestLogger.success(f"Parsed {len(visitor.collection.aliases)} aliases")

    # Check IID alias
    iid_alias = visitor.collection.aliases[0]
    assert iid_alias.name == "IID"
    assert iid_alias.type_spec == "InterfaceId"
    TestLogger.success(f"Alias: {iid_alias.name} = {iid_alias.type_spec}")

    # Check REFIID alias (pointer type)
    refiid_alias = visitor.collection.aliases[1]
    assert refiid_alias.name == "REFIID"
    assert refiid_alias.type_spec == "IID *"
    TestLogger.success(f"Alias: {refiid_alias.name} = {refiid_alias.type_spec}")

    TestLogger.complete("Alias meta loading test passed")


def test_alias_namespace() -> None:
    """Test that alias has correct namespace."""
    TestLogger.header("Stage 1: Alias Namespace")

    visitor = parse_ctd_file(Pathlib.Path('resources/ctd/microsoft/guiddef.ctd'))

    iid_alias = visitor.collection.aliases[0]
    assert iid_alias.namespace == "com::microsoft::windows::guid"
    TestLogger.success(f"Alias namespace: {iid_alias.namespace}")

    TestLogger.complete("Alias namespace test passed")
