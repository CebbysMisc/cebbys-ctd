"""Test that new syntax is parsed correctly."""
import pathlib as Pathlib
import antlr4 as Antlr4
import lv.cebbys.languages.ctd.loader as Loader
import lv.cebbys.languages.ctd.visitor as Visitor
import lv.cebbys.languages.ctd.meta as Meta
import lv.cebbys.languages.ctd.antlr4.GtdLexer as GtdLexer
import lv.cebbys.languages.ctd.antlr4.GtdParser as GtdParser
from test_utils import TestLogger


def test_new_syntax_parsing() -> None:
    """Test that structure, function, and annotation syntax is parsed."""
    loader = Loader.CtdLoader([Pathlib.Path('resources/ctd')])

    TestLogger.header("Parsing D3D11 Definitions")

    # Parse d3d11.ctd directly to check meta
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.ctd')
    content = d3d11_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    TestLogger.info(f"Parsed {len(visitor.collection.typedefs)} typedefs")
    if visitor.collection.typedefs:
        for td in visitor.collection.typedefs:
            TestLogger.info(f"{td.name}: {td.type_spec}", indent=2)
    TestLogger.info(f"Parsed {len(visitor.collection.enums)} enums")
    TestLogger.info(f"Parsed {len(visitor.collection.flags)} flags")
    TestLogger.info(f"Parsed {len(visitor.collection.structures)} structures")
    TestLogger.info(f"Parsed {len(visitor.collection.functions)} functions")

    # Check typedefs
    assert len(visitor.collection.typedefs) == 2
    resultcode = visitor.collection.typedefs[0]
    assert resultcode.name == "ResultCode"
    modulehandle = visitor.collection.typedefs[1]
    assert modulehandle.name == "ModuleHandle"
    TestLogger.section_break()
    TestLogger.success(f"Typedef: {resultcode.name} = {resultcode.type_spec}")
    TestLogger.success(f"Typedef: {modulehandle.name} = {modulehandle.type_spec}")

    # Check enums
    assert len(visitor.collection.enums) == 2
    driver_type = visitor.collection.enums[0]
    assert driver_type.name == "DriverType"
    assert len(driver_type.members) == 6
    TestLogger.success(f"Enum: {driver_type.name} with {len(driver_type.members)} members")

    feature_level = visitor.collection.enums[1]
    assert feature_level.name == "FeatureLevel"
    assert len(feature_level.members) == 10
    TestLogger.success(
        f"Enum: {feature_level.name} with {len(feature_level.members)} members (hex values)")

    # Check flag
    assert len(visitor.collection.flags) == 1
    create_device_flag = visitor.collection.flags[0]
    assert create_device_flag.name == "CreateDeviceFlag"
    assert len(create_device_flag.members) == 9
    TestLogger.success(
        f"Flag: {create_device_flag.name} with {len(create_device_flag.members)} members")

    # Parse dxgi.ctd to check structure
    TestLogger.header("Parsing DXGI Definitions")
    dxgi_path = Pathlib.Path('resources/ctd/dxgi.ctd')
    content = dxgi_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()

    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    TestLogger.success(f"Parsed {len(visitor.collection.structures)} structures from dxgi")
    assert len(visitor.collection.structures) == 5

    TestLogger.info(f"Parsed {len(visitor.collection.flags)} flags from dxgi")
    TestLogger.info(f"Parsed {len(visitor.collection.enums)} enums from dxgi")

    # Check first structure (Rational)
    rational = visitor.collection.structures[0]
    assert rational.name == "Rational"
    assert len(rational.members) == 2
    TestLogger.success(f"Structure: {rational.name} with {len(rational.members)} members")
    for member in rational.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=4)

    # Check SwapChainDesc structure
    swap_chain_desc = visitor.collection.structures[3]
    assert swap_chain_desc.name == "SwapChainDesc"
    assert len(swap_chain_desc.members) == 8
    TestLogger.success(
        f"Structure: {swap_chain_desc.name} with {len(swap_chain_desc.members)} members")

    # Check Adapter structure
    adapter = visitor.collection.structures[4]
    assert adapter.name == "Adapter"
    assert len(adapter.members) == 1
    TestLogger.success(f"Structure: {adapter.name} with {len(adapter.members)} members")
    for member in adapter.members:
        TestLogger.info(f"{member.type_spec} {member.name}", indent=4)

    # Check d3d11 function
    TestLogger.header("Parsing D3D11 Functions")
    d3d11_path = Pathlib.Path('resources/ctd/d3d11.ctd')
    content = d3d11_path.read_text(encoding='utf-8')
    input_stream = Antlr4.InputStream(content)
    lexer = GtdLexer.GtdLexer(input_stream)
    token_stream = Antlr4.CommonTokenStream(lexer)
    parser = GtdParser.GtdParser(token_stream)
    parse_tree = parser.compilationUnit()
    visitor = Visitor.MetaVisitor()
    visitor.visitCompilationUnit(parse_tree)

    assert len(visitor.collection.functions) == 1
    func = visitor.collection.functions[0]
    assert func.name == "D3D11CreateDeviceAndSwapChain"
    assert len(func.parameters) == 8
    decorators = func.decorators
    assert len(decorators) == 1
    decorator = decorators[0]
    assert decorator.name == "WinApi"
    TestLogger.success(f"Function: {decorator} {func.return_type} {func.name}(...)")
    for param in func.parameters:
        param_decorators_str = " ".join(str(d) for d in param.decorators)
        annot_str = f"{param_decorators_str} " if param_decorators_str else ""
        TestLogger.info(f"{annot_str}{param.type_spec} {param.name}", indent=4)

    TestLogger.complete("All new syntax parsed successfully")
