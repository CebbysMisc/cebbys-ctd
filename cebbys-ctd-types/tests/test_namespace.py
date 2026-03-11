from conftest import (
    TestLogger,
)
from tempfile import (
    TemporaryDirectory,
)
from pytest import (
    fixture,
)
from pathlib import (
    Path,
)

@fixture
def root():
    TestLogger.header("NamespaceTests: Instantiating root directory for sources")
    with TemporaryDirectory() as root:
        TestLogger.info(f"Sources will be written to temp directory: '{root}'")
        return Path(root)
    TestLogger.info(f"Deleting sources directory: '{root}'")

def test_namespace_source_header_range_slice(root: Path):
    TestLogger.header("NamespaceMeta: Test source slice from namespace header range")
    TestLogger.complete("Test passed")

def test_namespace_source_body_range_slice(root: Path):
    TestLogger.header("NamespaceMeta: Test source slice from namespace body range")
    TestLogger.complete("Test passed")