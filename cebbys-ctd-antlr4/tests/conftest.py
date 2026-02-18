"""Pytest configuration for antlr4 tests."""

import pathlib as Pathlib
import importlib.util as ImportUtil

# Load workspace conftest and import TestLogger
workspace_root = Pathlib.Path(__file__).parent.parent.parent
workspace_conftest_path = workspace_root / "conftest.py"

spec = ImportUtil.spec_from_file_location("workspace_conftest", workspace_conftest_path)
if spec and spec.loader:
    workspace_conftest = ImportUtil.module_from_spec(spec)
    spec.loader.exec_module(workspace_conftest)
    TestLogger = workspace_conftest.TestLogger
else:
    raise ImportError("Could not load workspace conftest.py")

__all__ = ['TestLogger']
