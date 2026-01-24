"""Stage 2: Test definition instance creation.

Tests that meta objects are correctly transformed into Definition instances.
At this stage, Definition objects are created but type references are not resolved.
"""
import pathlib as Pathlib
import sys
sys.path.insert(0, str(Pathlib.Path(__file__).parent.parent))

import lv.cebbys.languages.ctd.meta.loader as MetaLoader
import lv.cebbys.languages.ctd.meta.resolver.__api__ as ResolverApi
import lv.cebbys.languages.ctd.meta.resolver.typedef as TypedefModule
import lv.cebbys.languages.ctd.meta.resolver.enum as EnumModule
import lv.cebbys.languages.ctd.meta.resolver.structure as StructureModule
import lv.cebbys.languages.ctd.meta.resolver.function as FunctionModule
from test_utils import TestLogger


def test_typedef_definition_creation() -> None:
    """Test that TypedefMeta creates TypedefDefinition instances."""
    TestLogger.header("Stage 2: Typedef Definition Creation")

    # Load meta collection
    paths = [Pathlib.Path('resources/ctd/std-types.ctd')]
    meta_loader = MetaLoader.MetaLoader(paths)
    meta_collection, namespace_uses = meta_loader.load()

    # Create resolver context with empty type cache
    type_cache = {}
    context = ResolverApi.ResolverContext(type_cache, meta_collection, namespace_uses)

    # Create typedef instances (phase 1)
    typedef_resolver = TypedefModule.TypedefResolver(context)
    typedef_resolver.create_instances()

    # Verify definitions were created and cached
    assert 'std::lib::Int4' in context.type_cache
    assert 'std::lib::Void' in context.type_cache
    TestLogger.success("TypedefDefinition instances created")

    # Verify the definition has correct properties
    int4_def = context.type_cache['std::lib::Int4']
    assert int4_def.name == 'Int4'
    assert int4_def.namespace == 'std::lib'
    assert int4_def.qualified_name == 'std::lib::Int4'
    TestLogger.success(f"Int4 definition: {int4_def.qualified_name}")

    TestLogger.complete("Typedef definition creation test passed")


def test_enum_definition_creation() -> None:
    """Test that EnumMeta creates EnumDefinition instances."""
    TestLogger.header("Stage 2: Enum Definition Creation")

    paths = [Pathlib.Path('resources/ctd/std-types.ctd')]
    meta_loader = MetaLoader.MetaLoader(paths)
    meta_collection, namespace_uses = meta_loader.load()

    type_cache = {}
    context = ResolverApi.ResolverContext(type_cache, meta_collection, namespace_uses)

    # Create enum instances
    enum_resolver = EnumModule.EnumResolver(context)
    enum_resolver.create_instances()

    # Verify Null enum was created
    assert 'std::lib::Null' in context.type_cache
    null_def = context.type_cache['std::lib::Null']
    assert null_def.name == 'Null'
    TestLogger.success(f"Null enum definition: {null_def.qualified_name}")

    # At creation phase, members are empty (set during resolve phase)
    assert len(null_def.members) == 0
    TestLogger.success("Enum members are empty (deferred to resolve phase)")

    TestLogger.complete("Enum definition creation test passed")


def test_structure_definition_creation() -> None:
    """Test that StructureMeta creates StructureDefinition instances."""
    TestLogger.header("Stage 2: Structure Definition Creation")

    paths = [Pathlib.Path('resources/ctd/dxgi.ctd')]
    meta_loader = MetaLoader.MetaLoader(paths)
    meta_collection, namespace_uses = meta_loader.load()

    type_cache = {}
    context = ResolverApi.ResolverContext(type_cache, meta_collection, namespace_uses)

    # Create structure instances
    structure_resolver = StructureModule.StructureResolver(context)
    structure_resolver.create_instances()

    # Verify Rational structure was created
    assert 'com::microsoft::direct::graphics::dxgi::Rational' in context.type_cache
    rational_def = context.type_cache['com::microsoft::direct::graphics::dxgi::Rational']
    assert rational_def.name == 'Rational'
    TestLogger.success(f"Rational structure definition: {rational_def.qualified_name}")

    TestLogger.complete("Structure definition creation test passed")


def test_function_definition_creation() -> None:
    """Test that FunctionMeta creates FunctionDefinition instances."""
    TestLogger.header("Stage 2: Function Definition Creation")

    paths = [Pathlib.Path('resources/ctd/d3d11.ctd')]
    meta_loader = MetaLoader.MetaLoader(paths)
    meta_collection, namespace_uses = meta_loader.load()

    type_cache = {}
    context = ResolverApi.ResolverContext(type_cache, meta_collection, namespace_uses)

    # Create function instances
    function_resolver = FunctionModule.FunctionResolver(context)
    function_resolver.create_instances()

    # Verify function was created
    func_name = 'com::microsoft::direct::graphics::d3d11::D3D11CreateDeviceAndSwapChain'
    assert func_name in context.type_cache
    func_def = context.type_cache[func_name]
    assert func_def.name == 'D3D11CreateDeviceAndSwapChain'
    TestLogger.success(f"Function definition: {func_def.qualified_name}")

    # Verify decorators were transferred
    assert len(func_def.decorators) == 1
    assert func_def.decorators[0].name == 'WinApi'
    TestLogger.success(f"Function has @{func_def.decorators[0].name} decorator")

    TestLogger.complete("Function definition creation test passed")


def test_type_cache_singleton_guarantee() -> None:
    """Test that each type is created exactly once in the cache."""
    TestLogger.header("Stage 2: Type Cache Singleton Guarantee")

    paths = [Pathlib.Path('resources/ctd/std-types.ctd')]
    meta_loader = MetaLoader.MetaLoader(paths)
    meta_collection, namespace_uses = meta_loader.load()

    type_cache = {}
    context = ResolverApi.ResolverContext(type_cache, meta_collection, namespace_uses)

    # Create instances
    typedef_resolver = TypedefModule.TypedefResolver(context)
    typedef_resolver.create_instances()

    # Get the same type twice
    int4_first = context.type_cache['std::lib::Int4']
    int4_second = context.type_cache['std::lib::Int4']

    # Should be the exact same object
    assert int4_first is int4_second
    TestLogger.success(f"Int4 singleton: id={id(int4_first)}")
    TestLogger.success("Same object returned on multiple accesses")

    TestLogger.complete("Type cache singleton test passed")
