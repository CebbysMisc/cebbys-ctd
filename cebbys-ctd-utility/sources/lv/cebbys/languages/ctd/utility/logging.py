"""CTD Logging Module

Provides a centralized logging system for CTD modules with:
- Colored console output
- Configurable log levels
- Structured formatting
- Multiple loggers support
"""
import sys
import logging as Logging
import typing as Typing
from enum import Enum

__all__ = ['Logger', 'LogLevel', 'get_logger', 'configure_logging']


# Register TRACE level with Python's logging module
TRACE_LEVEL = 5
Logging.addLevelName(TRACE_LEVEL, 'TRACE')


class LogLevel(Enum):
    """Log level enumeration."""
    TRACE = TRACE_LEVEL
    DEBUG = Logging.DEBUG
    INFO = Logging.INFO
    WARNING = Logging.WARNING
    ERROR = Logging.ERROR
    CRITICAL = Logging.CRITICAL


class ColorCode:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


class ColoredFormatter(Logging.Formatter):
    """Custom formatter that adds colors to log messages."""
    
    LEVEL_COLORS = {
        TRACE_LEVEL: ColorCode.BRIGHT_BLACK,
        Logging.DEBUG: ColorCode.BRIGHT_BLUE,
        Logging.INFO: ColorCode.BRIGHT_GREEN,
        Logging.WARNING: ColorCode.BRIGHT_YELLOW,
        Logging.ERROR: ColorCode.BRIGHT_RED,
        Logging.CRITICAL: ColorCode.RED + ColorCode.BOLD,
    }
    
    def format(self, record: Logging.LogRecord) -> str:
        """Format the log record with colors.
        
        Args:
            record: Log record to format
            
        Returns:
            Formatted log message with ANSI color codes
        """
        level_color: str
        name_color: str
        message: str
        
        # Get color for log level
        level_color = self.LEVEL_COLORS.get(record.levelno, ColorCode.WHITE)
        name_color = ColorCode.BRIGHT_BLUE
        
        # Format: [LEVEL] module_name: message
        message = (
            f"{level_color}[{record.levelname:8}]{ColorCode.RESET} "
            f"{name_color}{record.name}{ColorCode.RESET}: "
            f"{record.getMessage()}"
        )
        
        # Add exception info if present
        if record.exc_info:
            message += f"\n{self.formatException(record.exc_info)}"
        
        return message


class Logger:
    """Wrapper around Python's logging.Logger with convenience methods."""
    
    def __init__(self, logger: Logging.Logger):
        """Initialize logger wrapper.
        
        Args:
            logger: Underlying Python logger
        """
        self._logger: Typing.Final[Logging.Logger]
        self._logger = logger

    def trace(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log a trace message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.log(TRACE_LEVEL, message, *args, **kwargs)
        
    def debug(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log a debug message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.debug(message, *args, **kwargs)
    
    def info(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log an info message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.info(message, *args, **kwargs)
    
    def warning(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log a warning message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.warning(message, *args, **kwargs)
    
    def error(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log an error message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.error(message, *args, **kwargs)
    
    def critical(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log a critical message.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.critical(message, *args, **kwargs)
    
    def exception(self, message: str, *args: Typing.Any, **kwargs: Typing.Any) -> None:
        """Log an exception with traceback.
        
        Args:
            message: Message to log
            *args: Format arguments
            **kwargs: Additional logging arguments
        """
        self._logger.exception(message, *args, **kwargs)
    
    def set_level(self, level: LogLevel | int) -> None:
        """Set the logging level.
        
        Args:
            level: Log level (LogLevel enum or int)
        """
        level_value: int
        
        if isinstance(level, LogLevel):
            level_value = level.value
        else:
            level_value = level
        
        self._logger.setLevel(level_value)
    
    @property
    def name(self) -> str:
        """Get logger name."""
        return self._logger.name
    
    @property
    def level(self) -> int:
        """Get current log level."""
        return self._logger.level


# Global logger registry
_LOGGERS: dict[str, Logger] = {}
_configured: bool = False


def configure_logging(
    level: LogLevel = LogLevel.INFO,
    colored: bool = True,
    format_string: str | None = None
) -> None:
    """Configure the global logging system.
    
    Args:
        level: Default log level for all loggers
        colored: Whether to use colored output
        format_string: Custom format string (if not using colored formatter)
    """
    global _configured
    
    handler: Logging.StreamHandler[Typing.Any]
    formatter: Logging.Formatter
    
    # Configure root logger
    root_logger = Logging.getLogger()
    root_logger.setLevel(level.value)
    
    # Remove existing handlers
    root_logger.handlers.clear()
    
    # Create console handler
    handler = Logging.StreamHandler(sys.stdout)
    handler.setLevel(level.value)
    
    # Set formatter
    if colored:
        formatter = ColoredFormatter()
    else:
        fmt = format_string or '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = Logging.Formatter(fmt)
    
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    
    _configured = True


def get_logger(name: str, level: LogLevel | None = None) -> Logger:
    """Get or create a logger with the given name.
    
    Args:
        name: Logger name (typically module name)
        level: Optional log level override
        
    Returns:
        Logger instance
        
    Example:
        >>> logger = get_logger('cebbys.ctd.loader')
        >>> logger.info('Loading CTD files...')
    """
    global _configured, _LOGGERS
    
    logger: Logger
    py_logger: Logging.Logger
    
    # Configure logging if not already done
    if not _configured:
        configure_logging()
    
    # Return cached logger if exists
    if name in _LOGGERS:
        logger = _LOGGERS[name]
        if level is not None:
            logger.set_level(level)
        return logger
    
    # Create new logger
    py_logger = Logging.getLogger(name)
    logger = Logger(py_logger)
    
    if level is not None:
        logger.set_level(level)
    
    # Cache and return
    _LOGGERS[name] = logger
    return logger
