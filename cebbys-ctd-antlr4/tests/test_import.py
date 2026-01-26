"""Test that ANTLR4 generated types can be imported."""


def test_import_lexer() -> None:
    """Test that GtdLexer can be imported."""
    from lv.cebbys.languages.ctd.antlr4 import CtdLexer
    assert CtdLexer is not None


def test_import_parser() -> None:
    """Test that GtdParser can be imported."""
    from lv.cebbys.languages.ctd.antlr4 import CtdParser
    assert CtdParser is not None


def test_import_visitor() -> None:
    """Test that GtdVisitor can be imported."""
    from lv.cebbys.languages.ctd.antlr4 import CtdVisitor
    assert CtdVisitor is not None


def test_import_all() -> None:
    """Test that all exports are available."""
    import lv.cebbys.languages.ctd.antlr4 as Antlr4
    assert hasattr(Antlr4, 'CtdLexer')
    assert hasattr(Antlr4, 'CtdParser')
    assert hasattr(Antlr4, 'CtdVisitor')
