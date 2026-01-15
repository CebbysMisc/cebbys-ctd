"""Test that new syntax is parsed correctly."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser

def test_new_syntax_parsing() -> None:
    """Test that structure, function, and annotation syntax is parsed."""
    loader = Loader.CtdLoader([Pathlib.Path('resources/ctd')])
    
    # Parse d3d11.gtd directly to check meta
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.gtd')
    parse_tree = loader._parse_file(d3d11_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    print(f"Parsed {len(visitor.collection.typedefs)} typedefs")
    if visitor.collection.typedefs:
        for td in visitor.collection.typedefs:
            print(f"  - {td.name}: {td.type_spec}")
    print(f"Parsed {len(visitor.collection.enums)} enums")
    print(f"Parsed {len(visitor.collection.structures)} structures")
    print(f"Parsed {len(visitor.collection.functions)} functions")
    
    # Check typedef
    assert len(visitor.collection.typedefs) == 1
    hresult = visitor.collection.typedefs[0]
    assert hresult.name == "HResult"
    print(f"\n✓ Typedef: {hresult.name} = {hresult.type_spec}")
    
    # Check enum
    assert len(visitor.collection.enums) == 1
    driver_type = visitor.collection.enums[0]
    assert driver_type.name == "DriverType"
    assert len(driver_type.members) == 6
    print(f"✓ Enum: {driver_type.name} with {len(driver_type.members)} members")
    
    # Parse dxgi.gtd to check structure
    dxgi_path = Pathlib.Path('resources/ctd/dxgi.gtd')
    parse_tree = loader._parse_file(dxgi_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    print(f"\n✓ Parsed {len(visitor.collection.structures)} structures from dxgi")
    assert len(visitor.collection.structures) == 1
    adapter = visitor.collection.structures[0]
    assert adapter.name == "Adapter"
    assert len(adapter.members) == 1
    print(f"✓ Structure: {adapter.name} with {len(adapter.members)} members")
    for member in adapter.members:
        print(f"    {member.type_spec} {member.name}")
    
    # Check d3d11 function
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.gtd')
    parse_tree = loader._parse_file(d3d11_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    assert len(visitor.collection.functions) == 1
    func = visitor.collection.functions[0]
    assert func.name == "D3D11CreateDeviceAndSwapChain"
    assert func.annotation == "WinApi"
    assert len(func.parameters) == 2
    print(f"\n✓ Function: @{func.annotation} {func.return_type} {func.name}(...)")
    for param in func.parameters:
        print(f"    {param.type_spec} {param.name}")
    
    print("\n✅ All new syntax parsed successfully!")

if __name__ == '__main__':
    test_new_syntax_parsing()
