"""Test that new syntax is parsed correctly."""
import pathlib as Pathlib
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser
from test_utils import TestLogger

def test_new_syntax_parsing() -> None:
    """Test that structure, function, and annotation syntax is parsed."""
    loader = Loader.CtdLoader([Pathlib.Path('resources/ctd')])
    
    TestLogger.header("Parsing D3D11 Definitions")
    
    # Parse d3d11.gtd directly to check meta
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.gtd')
    parse_tree = loader._parse_file(d3d11_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    TestLogger.info(f"Parsed {len(visitor.collection.typedefs)} typedefs")
    if visitor.collection.typedefs:
        for td in visitor.collection.typedefs:
            TestLogger.info(f"{td.name}: {td.type_spec}", indent=2)
    TestLogger.info(f"Parsed {len(visitor.collection.enums)} enums")
    TestLogger.info(f"Parsed {len(visitor.collection.structures)} structures")
    TestLogger.info(f"Parsed {len(visitor.collection.functions)} functions")
    
    # Check typedef
    assert len(visitor.collection.typedefs) == 1
    hresult = visitor.collection.typedefs[0]
    assert hresult.name == "HResult"
    TestLogger.section_break()
    TestLogger.success(f"Typedef: {hresult.name} = {hresult.type_spec}")
    
    # Check enum
    assert len(visitor.collection.enums) == 1
    driver_type = visitor.collection.enums[0]
    assert driver_type.name == "DriverType"
    assert len(driver_type.members) == 6
    TestLogger.success(f"Enum: {driver_type.name} with {len(driver_type.members)} members")
    
    # Parse dxgi.gtd to check structure
    TestLogger.header("Parsing DXGI Definitions")
    dxgi_path = Pathlib.Path('resources/ctd/dxgi.gtd')
    parse_tree = loader._parse_file(dxgi_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    TestLogger.success(f"Parsed {len(visitor.collection.structures)} structures from dxgi")
    assert len(visitor.collection.structures) == 1
    adapter = visitor.collection.structures[0]
    assert adapter.name == "Adapter"
    assert len(adapter.members) == 1
    TestLogger.success(f"Structure: {adapter.name} with {len(adapter.members)} members")
    for member in adapter.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=4)
    
    # Check d3d11 function
    TestLogger.header("Parsing D3D11 Functions")
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.gtd')
    parse_tree = loader._parse_file(d3d11_path)
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)
    
    assert len(visitor.collection.functions) == 1
    func = visitor.collection.functions[0]
    assert func.name == "D3D11CreateDeviceAndSwapChain"
    assert func.annotation == "WinApi"
    assert len(func.parameters) == 2
    TestLogger.success(f"Function: @{func.annotation} {func.return_type} {func.name}(...)")
    for param in func.parameters:
        TestLogger.info(f"{param.type_spec} {param.name}", indent=4)
    
    TestLogger.complete("All new syntax parsed successfully")
