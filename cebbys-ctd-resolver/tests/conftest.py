"""Pytest configuration for resolver tests."""

import pathlib as Pathlib
import importlib.util as ImportUtil
import pytest as Pytest
import lv.cebbys.languages.ctd.utility.logging as CtdLogging


@Pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for test runs - enable TRACE level."""
    CtdLogging.configure_logging(
        level=CtdLogging.LogLevel.TRACE,
        colored=True
    )


# Load workspace conftest and import TestLogger
workspace_root = Pathlib.Path(__file__).parent.parent.parent
workspace_conftest_path = workspace_root / "conftest.py"

spec = ImportUtil.spec_from_file_location("workspace_conftest", workspace_conftest_path)
if spec and spec.loader:
    workspace_conftest = ImportUtil.module_from_spec(spec)
    spec.loader.exec_module(workspace_conftest)
    TestLogger = workspace_conftest.TestLogger
    get_resource_path = workspace_conftest.get_resource_path
    load_meta_collection = workspace_conftest.load_meta_collection
else:
    raise ImportError("Could not load workspace conftest.py")

__all__ = [
    'TestLogger',
    'configure_logging',
    'get_resource_path',
    'load_meta_collection',
]
