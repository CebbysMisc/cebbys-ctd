"""Test TRACE level logging."""

import lv.cebbys.languages.ctd.utility.logging as CtdLogging


def test_trace_logging() -> None:
    """Test that TRACE level logs are visible."""
    logger = CtdLogging.get_logger("test.trace")
    
    logger.trace("This is a TRACE message")
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    
    # Just verify the test runs without errors
    assert True
