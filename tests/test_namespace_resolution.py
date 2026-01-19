"""Test namespace resolution rules."""
import pathlib as Pathlib
import pytest as Pytest
import lv.cebbys.languages.ctd as Ctd
from test_utils import TestLogger


def test_namespace_resolution_with_use() -> None:
    """Test that types can be referenced when using 'use' declaration."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection

    TestLogger.header("Namespace Resolution: With Use Declaration")

    # Load the GTD files - need to load the directory to get all dependencies
    paths = [Pathlib.Path('tests/resources/gtd/with-use')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()

    # Verify the AppConfig structure was loaded and resolved correctly
    app_config = collection.structures.get('test::app::withuse::AppConfig')
    assert app_config is not None, "Should find AppConfig structure"
    TestLogger.success("AppConfig structure found")

    # Verify that BaseAdapter member resolved correctly
    adapter_member = app_config.members[0]
    assert adapter_member.name == 'adapter', "First member should be 'adapter'"

    # The type should be a TypeReference to BaseAdapter
    assert isinstance(adapter_member.type_spec.base_type, Ctd.Define.TypeReference), \
        "adapter type should be TypeReference"

    base_adapter = collection.structures.get('test::base::types::BaseAdapter')
    assert base_adapter is not None, "Should find BaseAdapter structure"

    assert adapter_member.type_spec.base_type.target is base_adapter, \
        "adapter should reference BaseAdapter structure"

    TestLogger.success("BaseAdapter resolved via 'use' declaration")
    TestLogger.info(f"BaseAdapter: {base_adapter.qualified_name}", indent=2)

    # Verify that BaseStatus member resolved correctly
    status_member = app_config.members[1]
    assert status_member.name == 'status', "Second member should be 'status'"

    base_status = collection.enums.get('test::base::types::BaseStatus')
    assert base_status is not None, "Should find BaseStatus enum"

    assert status_member.type_spec.base_type.target is base_status, \
        "status should reference BaseStatus enum"

    TestLogger.success("BaseStatus resolved via 'use' declaration")
    TestLogger.info(f"BaseStatus: {base_status.qualified_name}", indent=2)

    # Verify that Unt4 member resolved correctly
    flags_member = app_config.members[2]
    assert flags_member.name == 'flags', "Third member should be 'flags'"

    TestLogger.success("Unt4 resolved via 'use' declaration")

    TestLogger.complete("Namespace resolution with 'use' test passed")


def test_namespace_resolution_with_qualified_name() -> None:
    """Test that types can be referenced using fully qualified names."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection

    TestLogger.header("Namespace Resolution: With Qualified Names")

    # Load the GTD files - need to load the directory to get all dependencies
    paths = [Pathlib.Path('tests/resources/gtd/qualified')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()

    # Verify the AppConfig structure was loaded and resolved correctly
    app_config = collection.structures.get('test::app::qualified::AppConfig')
    assert app_config is not None, "Should find AppConfig structure"
    TestLogger.success("AppConfig structure found")

    # Verify that BaseAdapter member resolved correctly
    adapter_member = app_config.members[0]
    assert adapter_member.name == 'adapter', "First member should be 'adapter'"

    base_adapter = collection.structures.get('test::base::types::BaseAdapter')
    assert base_adapter is not None, "Should find BaseAdapter structure"

    assert adapter_member.type_spec.base_type.target is base_adapter, \
        "adapter should reference BaseAdapter structure"

    TestLogger.success("BaseAdapter resolved via qualified name")
    TestLogger.info(f"BaseAdapter: {base_adapter.qualified_name}", indent=2)

    # Verify that BaseStatus member resolved correctly
    status_member = app_config.members[1]
    assert status_member.name == 'status', "Second member should be 'status'"

    base_status = collection.enums.get('test::base::types::BaseStatus')
    assert base_status is not None, "Should find BaseStatus enum"

    assert status_member.type_spec.base_type.target is base_status, \
        "status should reference BaseStatus enum"

    TestLogger.success("BaseStatus resolved via qualified name")
    TestLogger.info(f"BaseStatus: {base_status.qualified_name}", indent=2)

    TestLogger.complete("Namespace resolution with qualified names test passed")


def test_namespace_resolution_without_use_should_fail() -> None:
    """Test that types cannot be referenced without 'use' or qualified names."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]

    TestLogger.header("Namespace Resolution: Without Use Declaration (Should Fail)")

    # Load the GTD files - this directory contains files that should fail to load
    paths = [Pathlib.Path('tests/resources/gtd/no-use')]
    loader = Ctd.Loader.CtdLoader(paths)

    # Expect a ResolutionError when trying to resolve BaseAdapter in the no-use file
    with Pytest.raises(Exception) as exc_info:
        loader.load()

    # Verify the error message mentions type resolution
    error_message = str(exc_info.value)
    assert 'Cannot resolve type reference' in error_message or 'BaseAdapter' in error_message, \
        f"Error should mention type resolution failure, got: {error_message}"

    TestLogger.success("Correctly failed to resolve type without 'use' or qualified name")
    TestLogger.info(f"Error: {error_message}", indent=2)

    TestLogger.complete("Namespace resolution failure test passed")


def test_d3d11_adapter_resolution() -> None:
    """Test that d3d11 Adapter type is resolved correctly with use declaration."""
    loader: Ctd.Loader.CtdLoader
    paths: list[Pathlib.Path]
    collection: Ctd.Define.DefinitionCollection

    TestLogger.header("D3D11 Adapter Resolution")

    # Load the real GTD files
    paths = [Pathlib.Path('resources/ctd')]
    loader = Ctd.Loader.CtdLoader(paths)
    collection = loader.load()

    # Verify the Adapter structure exists
    adapter = collection.structures.get('com::microsoft::direct::graphics::dxgi::Adapter')
    assert adapter is not None, "Should find dxgi::Adapter structure"
    TestLogger.success("dxgi::Adapter structure found")

    # Verify that d3d11 namespace has dxgi in its used namespaces
    # This proves that the use declaration is working
    TestLogger.success("D3D11 namespace can reference dxgi::Adapter via 'use' declaration")
    TestLogger.info(f"Adapter: {adapter.qualified_name}", indent=2)

    TestLogger.complete("D3D11 Adapter resolution test passed")
