"""Tests for CtdMetaParser.parse_class method.

Validates the complete parsing pipeline:
1. CTD string → ANTLR4 context (via Antlr4.CtdParser)
2. ANTLR4 context → Meta object (via Parser.CtdMetaParser)
3. Meta object attribute validation
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
import lv.cebbys.languages.ctd.meta.parser as Parser
import lv.cebbys.languages.ctd.types.meta as Meta
from conftest import TestLogger


def _parse_class(ctd_string: str, namespace: str = "test") -> Meta.ClassMeta:
    """Helper function to parse CTD class string into ClassMeta.

    Performs steps 1-2 of the parsing pipeline:
    1. Parse CTD string into ANTLR4 context
    2. Map ANTLR4 context to Meta object

    Args:
        ctd_string: CTD class declaration
        namespace: Namespace for the class (default: "test")

    Returns:
        ClassMeta object
    """
    ctd_parser: Antlr4.CtdParser
    class_ctx: Antlr4.CtdGrammar.ClassDeclarationContext
    class_meta: Meta.ClassMeta

    # Step 1: Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    class_ctx = ctd_parser.classDeclaration(ctd_string)

    assert class_ctx is not None
    assert isinstance(class_ctx, Antlr4.CtdGrammar.ClassDeclarationContext)
    TestLogger.success("ANTLR4 context created")

    # Step 2: Map ANTLR4 context to Meta object
    class_meta = Parser.CtdMetaParser.parse_class(namespace, class_ctx)

    assert class_meta is not None
    assert isinstance(class_meta, Meta.ClassMeta)
    TestLogger.success("ClassMeta object created")

    return class_meta


def test_parse_empty_class() -> None:
    """Test parsing an empty class with no members or methods."""
    TestLogger.header("MetaParser: Empty Class")

    class_meta = _parse_class("class Empty {}")

    assert class_meta.name == "Empty"
    assert class_meta.namespace == "test"
    assert len(class_meta.bases) == 0
    assert len(class_meta.members) == 0
    assert len(class_meta.methods) == 0
    assert len(class_meta.decorators) == 0

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_members_only() -> None:
    """Test parsing a class with only properties (no methods)."""
    TestLogger.header("MetaParser: Class with Members Only")

    class_meta = _parse_class('''
        class Point {
            Int4 x
            Int4 y
        }
    ''')

    assert class_meta.name == "Point"
    assert class_meta.namespace == "test"
    assert len(class_meta.bases) == 0
    assert len(class_meta.members) == 2
    assert len(class_meta.methods) == 0

    assert class_meta.members[0].name == "x"
    assert str(class_meta.members[0].type_spec) == "Int4"
    assert class_meta.members[1].name == "y"
    assert str(class_meta.members[1].type_spec) == "Int4"

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_members_and_methods() -> None:
    """Test parsing a class with both members and methods."""
    TestLogger.header("MetaParser: Class with Members and Methods")

    class_meta = _parse_class('''
        class Shape {
            Unt4 color
            Int4 GetColor()
            void SetColor(Unt4 color)
        }
    ''')

    assert class_meta.name == "Shape"
    assert len(class_meta.members) == 1
    assert len(class_meta.methods) == 2

    assert class_meta.members[0].name == "color"
    assert str(class_meta.members[0].type_spec) == "Unt4"

    assert class_meta.methods[0].name == "GetColor"
    assert class_meta.methods[1].name == "SetColor"
    assert len(class_meta.methods[1].parameters) == 1
    assert class_meta.methods[1].parameters[0].name == "color"

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_single_base() -> None:
    """Test parsing a class that extends a single base type."""
    TestLogger.header("MetaParser: Class with Single Base")

    class_meta = _parse_class('''
        class Point3D : Point {
            Int4 z
            Int4 GetZ()
        }
    ''')

    assert class_meta.name == "Point3D"
    assert len(class_meta.bases) == 1
    assert str(class_meta.bases[0]) == "Point"
    assert len(class_meta.members) == 1
    assert len(class_meta.methods) == 1

    assert class_meta.members[0].name == "z"
    assert class_meta.methods[0].name == "GetZ"

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_multiple_bases() -> None:
    """Test parsing a class that extends multiple base types."""
    TestLogger.header("MetaParser: Class with Multiple Bases")

    class_meta = _parse_class('''
        class ComObject : IUnknown, BaseObject {
            Any* data
            Unt4 refCount
            Int4 QueryInterface(Unt4 interfaceId, Any* vtable)
            Unt4 AddRef()
            Unt4 Release()
        }
    ''')

    assert class_meta.name == "ComObject"
    assert len(class_meta.bases) == 2
    assert str(class_meta.bases[0]) == "IUnknown"
    assert str(class_meta.bases[1]) == "BaseObject"
    assert len(class_meta.members) == 2
    assert len(class_meta.methods) == 3

    assert class_meta.members[0].name == "data"
    assert class_meta.members[1].name == "refCount"
    assert class_meta.methods[0].name == "QueryInterface"
    assert class_meta.methods[1].name == "AddRef"
    assert class_meta.methods[2].name == "Release"

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_decorated_members() -> None:
    """Test parsing a class with decorated member properties."""
    TestLogger.header("MetaParser: Class with Decorated Members")

    class_meta = _parse_class('''
        class Node {
            @Nullable Node* next
            Int4 value
            Node* GetNext()
        }
    ''')

    assert class_meta.name == "Node"
    assert len(class_meta.members) == 2
    assert len(class_meta.methods) == 1

    nullable_member = class_meta.members[0]
    assert nullable_member.name == "next"
    assert len(nullable_member.decorators) == 1
    assert nullable_member.decorators[0].name == "Nullable"

    plain_member = class_meta.members[1]
    assert plain_member.name == "value"
    assert len(plain_member.decorators) == 0

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_decorated_methods() -> None:
    """Test parsing a class with decorated methods."""
    TestLogger.header("MetaParser: Class with Decorated Methods")

    class_meta = _parse_class('''
        class Service {
            Unt4 id
            @WinApi Int4 Start()
            @WinApi void Stop()
        }
    ''')

    assert class_meta.name == "Service"
    assert len(class_meta.members) == 1
    assert len(class_meta.methods) == 2

    assert class_meta.methods[0].name == "Start"
    assert len(class_meta.methods[0].decorators) == 1
    assert class_meta.methods[0].decorators[0].name == "WinApi"

    assert class_meta.methods[1].name == "Stop"
    assert len(class_meta.methods[1].decorators) == 1
    assert class_meta.methods[1].decorators[0].name == "WinApi"

    TestLogger.success("All attributes validated")
    TestLogger.complete()


def test_parse_class_with_class_decorator() -> None:
    """Test parsing a class with a class-level decorator."""
    TestLogger.header("MetaParser: Class with Class Decorator")

    class_meta = _parse_class('''
        @WinApi
        class MyClass {
            Int4 value
            Int4 GetValue()
        }
    ''')

    assert class_meta.name == "MyClass"
    assert len(class_meta.decorators) == 1
    assert class_meta.decorators[0].name == "WinApi"
    assert len(class_meta.members) == 1
    assert len(class_meta.methods) == 1

    TestLogger.success("All attributes validated")
    TestLogger.complete()
