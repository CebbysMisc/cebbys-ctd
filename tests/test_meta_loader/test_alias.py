"""Stage 1: Test alias meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_alias_parsing() -> None:
    """Test that alias declarations are parsed into AliasMeta."""
    TestLogger.header("Stage 1: Alias Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/aliases.ctd'))

    # aliases.ctd should have 3 aliases
    assert len(visitor.collection.aliases) == 3
    TestLogger.success(f"Parsed {len(visitor.collection.aliases)} aliases")

    # Check InterfaceId alias
    interface_id_alias = visitor.collection.aliases[0]
    assert interface_id_alias.name == "InterfaceId"
    assert interface_id_alias.type_spec == "Guid"
    TestLogger.success(f"Alias: {interface_id_alias.name} = {interface_id_alias.type_spec}")

    # Check IID alias
    iid_alias = visitor.collection.aliases[1]
    assert iid_alias.name == "IID"
    assert iid_alias.type_spec == "InterfaceId"
    TestLogger.success(f"Alias: {iid_alias.name} = {iid_alias.type_spec}")

    # Check REFIID alias (pointer type)
    refiid_alias = visitor.collection.aliases[2]
    assert refiid_alias.name == "REFIID"
    assert refiid_alias.type_spec == "IID *"
    TestLogger.success(f"Alias: {refiid_alias.name} = {refiid_alias.type_spec}")

    TestLogger.complete("Alias meta loading test passed")


def test_alias_namespace() -> None:
    """Test that alias has correct namespace."""
    TestLogger.header("Stage 1: Alias Namespace")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/aliases.ctd'))

    interface_id_alias = visitor.collection.aliases[0]
    assert interface_id_alias.namespace == "test::aliases"
    TestLogger.success(f"Alias namespace: {interface_id_alias.namespace}")

    TestLogger.complete("Alias namespace test passed")
