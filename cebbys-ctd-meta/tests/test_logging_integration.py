"""Test logging integration in meta parsers."""

import io as Io
import logging as Logging
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.utility.logging as CtdLogging


def test_module_parser_debug_logging() -> None:
    """Test that module parser emits debug logs."""
    # Configure logging to capture debug messages
    log_stream = Io.StringIO()
    handler = Logging.StreamHandler(log_stream)
    handler.setLevel(Logging.DEBUG)
    formatter = Logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Get the logger and configure it
    logger = Logging.getLogger('lv.cebbys.languages.ctd.meta.parser.module')
    logger.setLevel(Logging.DEBUG)
    logger.addHandler(handler)
    
    # Parse a simple CTD module
    ctd_source = """
    namespace test {
        typedef int Int4
    }
    """
    
    input_stream = Antlr4.InputStream(ctd_source)
    lexer = Antlr4.CtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = Antlr4.CtdGrammar(token_stream)
    module_ctx = parser.moduleDeclaration()
    
    # Parse to meta using CtdMetaParser
    module_meta = Parser.CtdMetaParser.parse_module(module_ctx)
    
    # Verify the log output contains expected debug messages
    log_output = log_stream.getvalue()
    
    assert "Parsing module declaration" in log_output, "Should log start of parsing"
    assert "Found 0 import(s) and 1 namespace(s)" in log_output, "Should log counts"
    assert "Module parsing complete: 0 include(s), 1 namespace(s)" in log_output, "Should log completion"
    
    # Verify the module was parsed correctly
    assert len(module_meta.namespaces) == 1
    assert len(module_meta.includes) == 0
    
    # Clean up
    logger.removeHandler(handler)


def test_module_parser_with_imports() -> None:
    """Test that module parser logs imports correctly."""
    # Configure logging to capture debug messages
    log_stream = Io.StringIO()
    handler = Logging.StreamHandler(log_stream)
    handler.setLevel(Logging.DEBUG)
    formatter = Logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Get the logger and configure it
    logger = Logging.getLogger('lv.cebbys.languages.ctd.meta.parser.module')
    logger.setLevel(Logging.DEBUG)
    logger.addHandler(handler)
    
    # Parse a CTD module with imports
    ctd_source = """
    import "base"
    import "utils"
    
    namespace test {
        typedef int Int4
    }
    
    namespace other {
        typedef void Void
    }
    """
    
    input_stream = Antlr4.InputStream(ctd_source)
    lexer = Antlr4.CtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = Antlr4.CtdGrammar(token_stream)
    module_ctx = parser.moduleDeclaration()
    
    # Parse to meta using CtdMetaParser
    module_meta = Parser.CtdMetaParser.parse_module(module_ctx)
    
    # Verify the log output contains expected debug messages
    log_output = log_stream.getvalue()
    
    assert "Parsing module declaration" in log_output
    assert "Found 2 import(s) and 2 namespace(s)" in log_output
    assert "Module parsing complete: 2 include(s), 2 namespace(s)" in log_output
    
    # Verify the module was parsed correctly
    assert len(module_meta.namespaces) == 2
    assert len(module_meta.includes) == 2
    
    # Clean up
    logger.removeHandler(handler)
