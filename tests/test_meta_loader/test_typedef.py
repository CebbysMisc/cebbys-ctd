"""Stage 1: Test typedef meta loading."""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

from conftest import parse_ctd_file
from test_utils import TestLogger


def test_typedef_parsing() -> None:
    """Test that typedef declarations are parsed into TypedefMeta."""
    TestLogger.header("Stage 1: Typedef Meta Loading")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/std-types.ctd'))

    # std-types.ctd should have 14 typedefs
    assert len(visitor.collection.typedefs) == 14
    TestLogger.success(f"Parsed {len(visitor.collection.typedefs)} typedefs")

    # Check specific typedefs
    typedef_names = [td.name for td in visitor.collection.typedefs]
    expected = ['Snt1', 'Snt2', 'Snt4', 'Snt8', 'Unt1', 'Unt2', 'Unt4', 'Unt8',
                'Int1', 'Int2', 'Int4', 'Int8', 'Void', 'Any']

    for name in expected:
        assert name in typedef_names, f"Should find typedef {name}"
        TestLogger.info(f"Found: {name}", indent=2)

    # Check typedef properties
    snt4 = next(td for td in visitor.collection.typedefs if td.name == 'Snt4')
    assert snt4.type_spec == "signed int"
    assert snt4.namespace == "std::lib"
    TestLogger.success(f"Snt4: type_spec='{snt4.type_spec}', namespace='{snt4.namespace}'")

    any_td = next(td for td in visitor.collection.typedefs if td.name == 'Any')
    assert any_td.type_spec == "Void *"
    TestLogger.success(f"Any: type_spec='{any_td.type_spec}'")

    TestLogger.complete("Typedef meta loading test passed")


def test_typedef_with_type_reference() -> None:
    """Test typedef that references another type."""
    TestLogger.header("Stage 1: Typedef with Type Reference")

    visitor = parse_ctd_file(Pathlib.Path('resources/test/ctd/functions.ctd'))

    # Find ResultCode typedef which references Int4
    resultcode = next(
        (td for td in visitor.collection.typedefs if td.name == 'ResultCode'),
        None
    )
    assert resultcode is not None
    assert resultcode.type_spec == "Int4"
    TestLogger.success(f"ResultCode: type_spec='{resultcode.type_spec}'")

    # Find ModuleHandle typedef which references Any
    modulehandle = next(
        (td for td in visitor.collection.typedefs if td.name == 'ModuleHandle'),
        None
    )
    assert modulehandle is not None
    assert modulehandle.type_spec == "Any"
    TestLogger.success(f"ModuleHandle: type_spec='{modulehandle.type_spec}'")

    TestLogger.complete("Typedef type reference test passed")
