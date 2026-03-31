"""Tests for Declaration.source property and universal decorator construction.

Validates:
1. meta.ctx is populated by parsers for all declaration types
2. Declaration.source returns the exact original CTD text
3. Decorators are constructed for all declaration types (not just Typedef)
4. When decorators are present, source starts at the first decorator
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
from lv.cebbys.languages.ctd.resolver.constructor.declaration import DeclarationConstructor


class FakeNamespace:
    """Minimal namespace stub for declaration construction in tests."""
    path = "test"


_NS = FakeNamespace()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _construct_typedef(ctd: str) -> Ctd.Typedef:
    ctx = Antlr4.CtdParser().typedefDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_typedef("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_alias(ctd: str) -> Ctd.Alias:
    ctx = Antlr4.CtdParser().aliasDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_alias("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_enum(ctd: str) -> Ctd.Enum:
    ctx = Antlr4.CtdParser().enumDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_enum("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_flag(ctd: str) -> Ctd.Flag:
    ctx = Antlr4.CtdParser().flagDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_flag("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_structure(ctd: str) -> Ctd.Structure:
    ctx = Antlr4.CtdParser().structureDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_structure("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_interface(ctd: str) -> Ctd.Interface:
    ctx = Antlr4.CtdParser().interfaceDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_interface("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


def _construct_function(ctd: str) -> Ctd.Function:
    ctx = Antlr4.CtdParser().functionDeclaration(ctd)
    meta = Parser.CtdMetaParser.parse_function("test", ctx)
    return DeclarationConstructor.construct(_NS, meta)


# ---------------------------------------------------------------------------
# Tests: ctx is stored on meta
# ---------------------------------------------------------------------------

def test_meta_ctx_stored_typedef():
    ctx = Antlr4.CtdParser().typedefDeclaration("typedef int MyInt")
    meta = Parser.CtdMetaParser.parse_typedef("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_alias():
    ctx = Antlr4.CtdParser().aliasDeclaration("alias MyInt AliasInt")
    meta = Parser.CtdMetaParser.parse_alias("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_enum():
    ctx = Antlr4.CtdParser().enumDeclaration("enum Color : int { RED GREEN }")
    meta = Parser.CtdMetaParser.parse_enum("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_flag():
    ctx = Antlr4.CtdParser().flagDeclaration("flag Options : int { OPT_A OPT_B }")
    meta = Parser.CtdMetaParser.parse_flag("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_structure():
    ctx = Antlr4.CtdParser().structureDeclaration("structure Point { int x int y }")
    meta = Parser.CtdMetaParser.parse_structure("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_interface():
    ctx = Antlr4.CtdParser().interfaceDeclaration("interface IFoo { int bar() }")
    meta = Parser.CtdMetaParser.parse_interface("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


def test_meta_ctx_stored_function():
    ctx = Antlr4.CtdParser().functionDeclaration("int add(int a int b)")
    meta = Parser.CtdMetaParser.parse_function("test", ctx)
    assert meta.ctx is not None
    assert meta.ctx is ctx


# ---------------------------------------------------------------------------
# Tests: source property (no decorators)
# ---------------------------------------------------------------------------

def test_source_typedef():
    ctd = "typedef int MyInt"
    decl = _construct_typedef(ctd)
    assert decl.source == ctd


def test_source_alias():
    ctd = "alias MyInt AliasInt"
    decl = _construct_alias(ctd)
    assert decl.source == ctd


def test_source_enum():
    ctd = "enum Color : int { RED GREEN BLUE }"
    decl = _construct_enum(ctd)
    assert decl.source == ctd


def test_source_flag():
    ctd = "flag Options : int { OPT_A OPT_B }"
    decl = _construct_flag(ctd)
    assert decl.source == ctd


def test_source_structure():
    ctd = "structure Point { int x int y }"
    decl = _construct_structure(ctd)
    assert decl.source == ctd


def test_source_interface():
    ctd = "interface IFoo { int bar() }"
    decl = _construct_interface(ctd)
    assert decl.source == ctd


def test_source_function():
    ctd = "int add(int a int b)"
    decl = _construct_function(ctd)
    assert decl.source == ctd


# ---------------------------------------------------------------------------
# Tests: source property includes decorator text
# ---------------------------------------------------------------------------

def test_source_typedef_with_decorator():
    ctd = "@WinApi typedef int WinInt"
    decl = _construct_typedef(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@WinApi")


def test_source_alias_with_decorator():
    ctd = "@Deprecated alias MyInt OldInt"
    decl = _construct_alias(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@Deprecated")


def test_source_enum_with_decorator():
    ctd = "@WinApi enum Color : int { RED GREEN }"
    decl = _construct_enum(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@WinApi")


def test_source_structure_with_decorator():
    ctd = "@WinApi structure Point { int x int y }"
    decl = _construct_structure(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@WinApi")


def test_source_function_with_decorator():
    ctd = "@WinApi int add(int a int b)"
    decl = _construct_function(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@WinApi")


# ---------------------------------------------------------------------------
# Tests: decorators constructed for all types (not just Typedef)
# ---------------------------------------------------------------------------

def test_decorators_typedef():
    decl = _construct_typedef("@WinApi typedef int WinInt")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_alias():
    decl = _construct_alias("@Deprecated alias MyInt OldInt")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "Deprecated"


def test_decorators_enum():
    decl = _construct_enum("@WinApi enum Color : int { RED }")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_flag():
    decl = _construct_flag("@WinApi flag Options : int { OPT_A }")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_structure():
    decl = _construct_structure("@WinApi structure Point { int x }")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_interface():
    decl = _construct_interface("@WinApi interface IFoo { int bar() }")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_function():
    decl = _construct_function("@WinApi int add(int a)")
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "WinApi"


def test_decorators_with_arguments():
    decl = _construct_typedef('@Storage("reg", "ecx") typedef int RegInt')
    assert len(decl.decorators) == 1
    assert decl.decorators[0].name == "Storage"
    assert len(decl.decorators[0].arguments) == 2


def test_no_decorators_empty_tuple():
    decl = _construct_typedef("typedef int MyInt")
    assert decl.decorators == ()
    assert isinstance(decl.decorators, tuple)


def test_decorators_are_immutable_tuple():
    decl = _construct_typedef("@WinApi typedef int WinInt")
    assert isinstance(decl.decorators, tuple)


def test_multiple_decorators():
    decl = _construct_typedef("@WinApi @Nullable typedef int MyInt")
    assert len(decl.decorators) == 2
    assert decl.decorators[0].name == "WinApi"
    assert decl.decorators[1].name == "Nullable"


def test_source_with_multiple_decorators_starts_at_first():
    ctd = "@WinApi @Nullable typedef int MyInt"
    decl = _construct_typedef(ctd)
    assert decl.source == ctd
    assert decl.source.startswith("@WinApi")
