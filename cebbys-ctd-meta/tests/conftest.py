"""Pytest configuration for meta tests."""

import pytest as Pytest
import lv.cebbys.languages.ctd.utility.logging as CtdLogging


@Pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for test runs - enable DEBUG level."""
    CtdLogging.configure_logging(
        level=CtdLogging.LogLevel.DEBUG,
        colored=True
    )
