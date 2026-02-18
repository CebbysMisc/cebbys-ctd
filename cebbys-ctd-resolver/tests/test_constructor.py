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
    """Test that EnumMeta can be constructed (without populating members)."""
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
    
    # Phase 1: Only validate instance creation, not property population
    assert isinstance(enum, Ctd.Enum)
    assert enum.name == "Color"
    assert enum.meta == meta
    assert isinstance(enum.members, list)
    # Members list is initialized but empty (populated in resolution phase)


def test_construct_structure() -> None:
    """Test that StructureMeta can be constructed (without populating members)."""
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
    
    # Phase 1: Only validate instance creation, not property population
    assert isinstance(structure, Ctd.Structure)
    assert structure.name == "Point"
    assert structure.meta == meta
    assert isinstance(structure.members, list)
    # Members list is initialized but empty (populated in resolution phase)


def test_construct_function() -> None:
    """Test that FunctionMeta can be constructed (without populating parameters)."""
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
    
    # Phase 1: Only validate instance creation, not property population
    assert isinstance(function, Ctd.Function)
    assert function.name == "add"
    assert function.meta == meta
    assert isinstance(function.parameters, list)
    # Parameters list is initialized but empty (populated in resolution phase)

