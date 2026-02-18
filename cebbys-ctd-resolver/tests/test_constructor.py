"""Tests for declaration constructors."""

import lv.cebbys.languages.ctd.types.meta as Meta
import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.resolver.constructor as Constructor


def test_construct_typedef() -> None:
    """Test that TypedefMeta can be constructed."""
    meta: Meta.TypedefMeta
    typedef: Ctd.Typedef
    
    meta = Meta.TypedefMeta(
        name="Int4",
        type_spec="int",
        namespace="test"
    )
    
    typedef = Constructor.DeclarationConstructor.construct(meta)
    
    assert isinstance(typedef, Ctd.Typedef)
    assert typedef.name == "Int4"
    assert typedef.meta == meta


def test_construct_enum() -> None:
    """Test that EnumMeta can be constructed."""
    meta: Meta.EnumMeta
    member_meta1: Meta.EnumMemberMeta
    member_meta2: Meta.EnumMemberMeta
    enum: Ctd.Enum
    
    member_meta1 = Meta.EnumMemberMeta(name="Red", value=0)
    member_meta2 = Meta.EnumMemberMeta(name="Green", value=1)
    
    meta = Meta.EnumMeta(
        name="Color",
        namespace="test",
        members=[member_meta1, member_meta2]
    )
    
    enum = Constructor.DeclarationConstructor.construct(meta)
    
    assert isinstance(enum, Ctd.Enum)
    assert enum.name == "Color"
    assert len(enum.members) == 2
    assert enum.members[0].name == "Red"
    assert enum.members[0].value == 0
    assert enum.members[1].name == "Green"
    assert enum.members[1].value == 1


def test_construct_structure() -> None:
    """Test that StructureMeta can be constructed."""
    meta: Meta.StructureMeta
    member_meta1: Meta.StructureMemberMeta
    member_meta2: Meta.StructureMemberMeta
    structure: Ctd.Structure
    
    member_meta1 = Meta.StructureMemberMeta(name="x", type_spec="int")
    member_meta2 = Meta.StructureMemberMeta(name="y", type_spec="int")
    
    meta = Meta.StructureMeta(
        name="Point",
        namespace="test",
        members=[member_meta1, member_meta2]
    )
    
    structure = Constructor.DeclarationConstructor.construct(meta)
    
    assert isinstance(structure, Ctd.Structure)
    assert structure.name == "Point"
    assert len(structure.members) == 2
    assert structure.members[0].name == "x"
    assert structure.members[1].name == "y"


def test_construct_function() -> None:
    """Test that FunctionMeta can be constructed."""
    meta: Meta.FunctionMeta
    param_meta1: Meta.ParameterMeta
    param_meta2: Meta.ParameterMeta
    function: Ctd.Function
    
    param_meta1 = Meta.ParameterMeta(name="a", type_spec="int")
    param_meta2 = Meta.ParameterMeta(name="b", type_spec="int")
    
    meta = Meta.FunctionMeta(
        name="add",
        namespace="test",
        return_type="int",
        parameters=[param_meta1, param_meta2]
    )
    
    function = Constructor.DeclarationConstructor.construct(meta)
    
    assert isinstance(function, Ctd.Function)
    assert function.name == "add"
    assert len(function.parameters) == 2
    assert function.parameters[0].name == "a"
    assert function.parameters[1].name == "b"

