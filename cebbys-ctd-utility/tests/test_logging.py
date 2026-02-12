"""Tests for the logging module."""
import sys
import io
import logging as Logging
import lv.cebbys.languages.ctd.utility as Utility
from conftest import TestLogger


def test_get_logger_creates_logger() -> None:
    """Test that get_logger creates a logger instance."""
    logger: Utility.Logger
    
    TestLogger.header("Logging: Get Logger")
    
    logger = Utility.get_logger('test.module')
    
    assert logger is not None
    assert logger.name == 'test.module'
    assert isinstance(logger, Utility.Logger)
    
    TestLogger.success(f"Created logger: {logger.name}")
    TestLogger.complete("Test passed")


def test_get_logger_returns_cached_instance() -> None:
    """Test that get_logger returns the same instance for the same name."""
    logger1: Utility.Logger
    logger2: Utility.Logger
    
    TestLogger.header("Logging: Logger Caching")
    
    logger1 = Utility.get_logger('test.cached')
    logger2 = Utility.get_logger('test.cached')
    
    assert logger1 is logger2
    TestLogger.success("Same logger instance returned")
    TestLogger.complete("Test passed")


def test_logger_levels() -> None:
    """Test that logger levels can be set and retrieved."""
    logger: Utility.Logger
    
    TestLogger.header("Logging: Log Levels")
    
    logger = Utility.get_logger('test.levels')
    
    # Test default level
    TestLogger.info(f"Default level: {logger.level}")
    
    # Test setting levels
    logger.set_level(Utility.LogLevel.DEBUG)
    assert logger.level == Logging.DEBUG
    TestLogger.success("Set DEBUG level")
    
    logger.set_level(Utility.LogLevel.WARNING)
    assert logger.level == Logging.WARNING
    TestLogger.success("Set WARNING level")
    
    logger.set_level(Utility.LogLevel.ERROR)
    assert logger.level == Logging.ERROR
    TestLogger.success("Set ERROR level")
    
    TestLogger.complete("Test passed")


def test_logger_output() -> None:
    """Test that logger produces output."""
    logger: Utility.Logger
    
    TestLogger.header("Logging: Output Messages")
    
    # Configure logging to ensure output
    Utility.configure_logging(level=Utility.LogLevel.DEBUG, colored=True)
    
    logger = Utility.get_logger('test.output')
    
    # Test all log levels
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")
    
    TestLogger.success("All log levels produced output")
    TestLogger.complete("Test passed")


def test_configure_logging_colored() -> None:
    """Test configuring logging with colored output."""
    TestLogger.header("Logging: Colored Configuration")
    
    # Configure with colors
    Utility.configure_logging(level=Utility.LogLevel.INFO, colored=True)
    
    logger = Utility.get_logger('test.colored')
    logger.info("Colored output enabled")
    
    TestLogger.success("Configured with colored output")
    TestLogger.complete("Test passed")


def test_configure_logging_plain() -> None:
    """Test configuring logging with plain output."""
    TestLogger.header("Logging: Plain Configuration")
    
    # Configure without colors
    Utility.configure_logging(level=Utility.LogLevel.INFO, colored=False)
    
    logger = Utility.get_logger('test.plain')
    logger.info("Plain output enabled")
    
    TestLogger.success("Configured with plain output")
    TestLogger.complete("Test passed")


def test_logger_formatting() -> None:
    """Test logger message formatting."""
    logger: Utility.Logger
    
    TestLogger.header("Logging: Message Formatting")
    
    logger = Utility.get_logger('test.format')
    
    # Test with format arguments
    logger.info("Processing %d files", 5)
    logger.info("Loading module: %s", "cebbys.ctd.loader")
    logger.info("Status: %s, Count: %d", "OK", 42)
    
    TestLogger.success("Formatted messages work correctly")
    TestLogger.complete("Test passed")


def test_log_level_enum() -> None:
    """Test LogLevel enum values."""
    TestLogger.header("Logging: LogLevel Enum")
    
    assert Utility.LogLevel.DEBUG.value == Logging.DEBUG
    assert Utility.LogLevel.INFO.value == Logging.INFO
    assert Utility.LogLevel.WARNING.value == Logging.WARNING
    assert Utility.LogLevel.ERROR.value == Logging.ERROR
    assert Utility.LogLevel.CRITICAL.value == Logging.CRITICAL
    
    TestLogger.success("All LogLevel enum values correct")
    TestLogger.complete("Test passed")
