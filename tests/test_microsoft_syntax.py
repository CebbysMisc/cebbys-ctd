"""Test Microsoft CTD syntax elements: alias, interface, array modifiers."""
import pathlib as Pathlib
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.antlr4.GtdLexer as GtdLexer
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser
from test_utils import TestLogger


def test_alias_parsing() -> None:
    """Test that alias declarations are parsed correctly."""
    TestLogger.header("Parsing Alias Declarations")

    # Parse guiddef.ctd which contains alias declarations
    guiddef_path = Pathlib.Path('resources/ctd/microsoft/guiddef.ctd')
    content = guiddef_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    # Check aliases
    TestLogger.info(f"Parsed {len(visitor.collection.aliases)} aliases")
    assert len(visitor.collection.aliases) == 2

    # Check first alias (IID)
    iid_alias = visitor.collection.aliases[0]
    assert iid_alias.name == "IID"
    assert iid_alias.type_spec == "InterfaceId"
    TestLogger.success(f"Alias: {iid_alias.name} = {iid_alias.type_spec}")

    # Check second alias (REFIID)
    refiid_alias = visitor.collection.aliases[1]
    assert refiid_alias.name == "REFIID"
    assert refiid_alias.type_spec == "IID *"
    TestLogger.success(f"Alias: {refiid_alias.name} = {refiid_alias.type_spec}")

    TestLogger.complete("Alias parsing test passed")


def test_array_modifier_parsing() -> None:
    """Test that array modifiers in type specs are parsed correctly."""
    TestLogger.header("Parsing Array Modifiers")

    # Parse guiddef.ctd which contains array modifiers
    guiddef_path = Pathlib.Path('resources/ctd/microsoft/guiddef.ctd')
    content = guiddef_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    # Check structure with array member
    TestLogger.info(f"Parsed {len(visitor.collection.structures)} structures")
    assert len(visitor.collection.structures) == 1

    guid_struct = visitor.collection.structures[0]
    assert guid_struct.name == "Guid"
    assert len(guid_struct.members) == 4
    TestLogger.success(f"Structure: {guid_struct.name} with {len(guid_struct.members)} members")

    # Check array member (data4 should be Unt1[8])
    data4_member = guid_struct.members[3]
    assert data4_member.name == "data4"
    assert "[8]" in data4_member.type_spec, f"Expected array modifier [8], got {data4_member.type_spec}"
    TestLogger.success(f"Array member: {data4_member.type_spec} {data4_member.name}")

    for member in guid_struct.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=4)

    TestLogger.complete("Array modifier parsing test passed")


def test_interface_parsing() -> None:
    """Test that interface declarations are parsed correctly."""
    TestLogger.header("Parsing Interface Declarations")

    # Parse unknown.ctd which contains interface declaration
    unknown_path = Pathlib.Path('resources/ctd/microsoft/unknown.ctd')
    content = unknown_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    # Check interfaces
    TestLogger.info(f"Parsed {len(visitor.collection.interfaces)} interfaces")
    assert len(visitor.collection.interfaces) == 1

    iunknown = visitor.collection.interfaces[0]
    assert iunknown.name == "IUnknown"
    assert len(iunknown.methods) == 3
    TestLogger.success(f"Interface: {iunknown.name} with {len(iunknown.methods)} methods")

    # Check methods
    query_interface = iunknown.methods[0]
    assert query_interface.name == "QueryInterface"
    assert len(query_interface.parameters) == 2
    assert len(query_interface.decorators) == 2
    TestLogger.info(f"Method: {query_interface.name}(...) with {len(query_interface.parameters)} params", indent=2)
    for decorator in query_interface.decorators:
        TestLogger.info(f"Decorator: @{decorator.name}", indent=4)

    add_ref = iunknown.methods[1]
    assert add_ref.name == "AddRef"
    assert len(add_ref.parameters) == 0
    TestLogger.info(f"Method: {add_ref.name}() with {len(add_ref.parameters)} params", indent=2)

    release = iunknown.methods[2]
    assert release.name == "Release"
    assert len(release.parameters) == 0
    TestLogger.info(f"Method: {release.name}() with {len(release.parameters)} params", indent=2)

    TestLogger.complete("Interface parsing test passed")
