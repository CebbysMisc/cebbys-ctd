"""Tests for CtdParser structure declaration parsing.

Validates that CtdParser correctly parses structure declarations into ANTLR4 contexts.
"""
import lv.cebbys.languages.ctd.antlr4 as Antlr4
from conftest import TestLogger


def _parse_structure(ctd_string: str) -> Antlr4.CtdGrammar.StructureDeclarationContext:
    """Helper function to parse structure declaration.
    
    Args:
        ctd_string: CTD structure declaration string
        
    Returns:
        StructureDeclarationContext from ANTLR4 parser
    """
    ctd_parser: Antlr4.CtdParser
    structure_ctx: Antlr4.CtdGrammar.StructureDeclarationContext
    
    # Parse CTD string into ANTLR4 context
    ctd_parser = Antlr4.CtdParser()
    structure_ctx = ctd_parser.structureDeclaration(ctd_string)
    
    assert structure_ctx is not None
    assert isinstance(structure_ctx, Antlr4.CtdGrammar.StructureDeclarationContext)
    
    return structure_ctx


def test_parse_simple_structure() -> None:
    """Test parsing a simple structure."""
    TestLogger.header("CtdParser: Simple Structure")

    ctx = _parse_structure("""
        structure Point {
            int x
            int y
        }
    """)
    
    # Verify structure keyword and name
    assert ctx.getText().startswith("structure")
    assert ctx.IDENTIFIER().getText() == "Point"
    
    # Verify members
    member_list = ctx.structureMemberList()
    assert member_list is not None
    
    members = member_list.structureMember()
    assert len(members) == 2
    
    # First member: int x
    assert members[0].typeSpec().typeReference().qualifiedName().getText() == "int"
    assert members[0].IDENTIFIER().getText() == "x"
    
    # Second member: int y
    assert members[1].typeSpec().typeReference().qualifiedName().getText() == "int"
    assert members[1].IDENTIFIER().getText() == "y"
    
    TestLogger.success("Simple structure parsed correctly")
    TestLogger.complete()


def test_parse_structure_with_pointer_member() -> None:
    """Test parsing structure with pointer member."""
    TestLogger.header("CtdParser: Structure with Pointer")

    ctx = _parse_structure("""
        structure Node {
            int value
            Node* next
        }
    """)
    
    # Verify structure name
    assert ctx.IDENTIFIER().getText() == "Node"
    
    # Verify members
    members = ctx.structureMemberList().structureMember()
    assert len(members) == 2
    
    # First member: int value
    assert members[0].typeSpec().typeReference().qualifiedName().getText() == "int"
    assert members[0].IDENTIFIER().getText() == "value"
    
    # Second member: Node* next (pointer to Node)
    assert members[1].typeSpec().typeReference().qualifiedName().getText() == "Node"
    extensions = members[1].typeSpec().typeReference().typeExtension()
    assert len(extensions) == 1
    assert extensions[0].pointerModifier() is not None
    assert members[1].IDENTIFIER().getText() == "next"
    
    TestLogger.success("Structure with pointer parsed correctly")
    TestLogger.complete()


def test_parse_structure_with_array_member() -> None:
    """Test parsing structure with array member."""
    TestLogger.header("CtdParser: Structure with Array")

    ctx = _parse_structure("""
        structure Guid {
            Unt4 data1
            Unt2 data2
            Unt2 data3
            Unt1[8] data4
        }
    """)
    
    # Verify structure name
    assert ctx.IDENTIFIER().getText() == "Guid"
    
    # Verify members
    members = ctx.structureMemberList().structureMember()
    assert len(members) == 4
    
    # Fourth member: Unt1[8] data4 (array of 8 Unt1)
    assert members[3].typeSpec().typeReference().qualifiedName().getText() == "Unt1"
    extensions = members[3].typeSpec().typeReference().typeExtension()
    assert len(extensions) == 1
    assert extensions[0].arrayModifier() is not None
    assert extensions[0].arrayModifier().getText() == "[8]"
    assert members[3].IDENTIFIER().getText() == "data4"
    
    TestLogger.success("Structure with array parsed correctly")
    TestLogger.complete()


def test_parse_structure_with_extension() -> None:
    """Test parsing structure with base type extension."""
    TestLogger.header("CtdParser: Structure with Extension")

    ctx = _parse_structure("""
        structure DerivedStruct : BaseStruct {
            int newField
        }
    """)
    
    # Verify structure name
    assert ctx.IDENTIFIER().getText() == "DerivedStruct"
    
    # Verify base type
    base_type = ctx.typeSpec()
    assert base_type is not None
    assert base_type.typeReference().qualifiedName().getText() == "BaseStruct"
    
    # Verify members
    members = ctx.structureMemberList().structureMember()
    assert len(members) == 1
    assert members[0].IDENTIFIER().getText() == "newField"
    
    TestLogger.success("Structure with extension parsed correctly")
    TestLogger.complete()


def test_parse_structure_with_complex_types() -> None:
    """Test parsing structure with complex type extensions."""
    TestLogger.header("CtdParser: Structure with Complex Types")

    ctx = _parse_structure("""
        structure ComplexData {
            int[3]* arrayPtr
            int*[4] ptrArray
            int[2]**[3] multiDim
        }
    """)
    
    # Verify structure name
    assert ctx.IDENTIFIER().getText() == "ComplexData"
    
    # Verify members with complex extensions
    members = ctx.structureMemberList().structureMember()
    assert len(members) == 3
    
    # First member: int[3]* arrayPtr
    exts0 = members[0].typeSpec().typeReference().typeExtension()
    assert len(exts0) == 2  # [3], *
    assert exts0[0].arrayModifier().getText() == "[3]"
    assert exts0[1].pointerModifier() is not None
    
    # Second member: int*[4] ptrArray
    exts1 = members[1].typeSpec().typeReference().typeExtension()
    assert len(exts1) == 2  # *, [4]
    assert exts1[0].pointerModifier() is not None
    assert exts1[1].arrayModifier().getText() == "[4]"
    
    # Third member: int[2]**[3] multiDim
    exts2 = members[2].typeSpec().typeReference().typeExtension()
    assert len(exts2) == 4  # [2], *, *, [3]
    assert exts2[0].arrayModifier().getText() == "[2]"
    assert exts2[1].pointerModifier() is not None
    assert exts2[2].pointerModifier() is not None
    assert exts2[3].arrayModifier().getText() == "[3]"
    
    TestLogger.success("Structure with complex types parsed correctly")
    TestLogger.complete()


def test_parse_empty_structure() -> None:
    """Test parsing empty structure."""
    TestLogger.header("CtdParser: Empty Structure")

    ctx = _parse_structure("structure Empty {}")
    
    # Verify structure name
    assert ctx.IDENTIFIER().getText() == "Empty"
    
    # Verify no members
    member_list = ctx.structureMemberList()
    assert member_list is None
    
    TestLogger.success("Empty structure parsed correctly")
    TestLogger.complete()
