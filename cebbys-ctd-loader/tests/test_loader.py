"""Test for Typedef declaration resolution to builtin types."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.types.ctd as Ctd

from lv.cebbys.languages.ctd.types.exception import (
    CtdInvalidParameterException,
    CtdException,
)
from lv.cebbys.languages.ctd.loader.module import (
    CtdModuleLoader
)
from conftest import (
    TestLogger
)
from pathlib import (
    Path
)

ROOT = Path(__name__).resolve().parent / "tests"

def test_exception_when_module_loader_created_without_roots() -> None:
    """Module loader shall fail if no ctd roots are provided to it."""
    TestLogger.header("CtdModuleLoader: Empty root list cause construction exception")
    try:
        CtdModuleLoader([])
        assert True, "Exception must have been thrown but was not"
    except BaseException as e:
        assert isinstance(e, CtdException),\
            f"Module constructor shall throw {CtdException.__name__} on empty root list, but threw {type(e).__name__}"
        cause = e.cause
        assert isinstance(cause, CtdInvalidParameterException),\
            f"Cause for module construction exception must be {CtdInvalidParameterException.__name__} but is {type(cause).__name__}"
        assert cause.parameter == "roots",\
            f"Failing parameter expected to be 'roots' but was '{cause.parameter}'"
        TestLogger.success(f"Valid exception was thrown in case of empty roots list")
    TestLogger.complete("Test passed")


def test_exception_when_module_does_not_exist_in_roots() -> None:
    """Module loader shall fail if ctd module does not exist in roots."""
    TestLogger.header("CtdModuleLoader: Not existant module cause exception")
    try:
        loader = CtdModuleLoader([ROOT / "resources/cases/0001-module-loader-duplicate-ctd-roots"])
        loader.load("not-exist")
        assert True, "Exception must have been thrown but was not"
    except BaseException as e:
        assert isinstance(e, CtdException),\
            f"Module constructor shall throw {CtdException.__name__} on empty root list, but threw {type(e).__name__}"
        cause = e.cause
        assert isinstance(cause, CtdException),\
            f"Cause for module construction exception must be {CtdException.__name__} but is {type(cause).__name__}"
        assert cause.message.startswith("No modules found at: "),\
            f"Unexpected error message '{cause.message}'"
        TestLogger.success(f"Valid exception was thrown in case of empty roots list")
    TestLogger.complete("Test passed")


def test_exception_when_duplicate_modules_exist_in_roots() -> None:
    """Module loader shall fail if duplicate ctds exist in roots."""
    TestLogger.header("CtdModuleLoader: Duplicated modules cause exception")
    try:
        loader = CtdModuleLoader([
            ROOT / "resources/cases/0001-module-loader-duplicate-ctd-roots/root-a",
            ROOT / "resources/cases/0001-module-loader-duplicate-ctd-roots/root-b"
        ])
        loader.load("test")
        assert True, "Exception must have been thrown but was not"
    except BaseException as e:
        assert isinstance(e, CtdException),\
            f"Module constructor shall throw {CtdException.__name__} on empty root list, but threw {type(e).__name__}"
        cause = e.cause
        assert isinstance(cause, CtdException),\
            f"Cause for module construction exception must be {CtdException.__name__} but is {type(cause).__name__}"
        assert cause.message.startswith("Multiple modules found matching at: "),\
            f"Unexpected error message '{cause.message}'"
        TestLogger.success(f"Valid exception was thrown in case of empty roots list")
    TestLogger.complete("Test passed")

