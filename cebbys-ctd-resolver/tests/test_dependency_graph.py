"""Tests for dependency graph builder."""

import lv.cebbys.languages.ctd.resolver as Resolver
import lv.cebbys.languages.ctd.types.meta as Meta


def test_dependency_graph_initialization() -> None:
    """Test that DependencyGraph can be initialized."""
    graph: Resolver.DependencyGraph
    
    graph = Resolver.DependencyGraph()
    
    assert graph is not None
    # Verify internal structures exist (they're private but we can check)
    assert hasattr(graph, '_module_imports')
    assert hasattr(graph, '_namespace_hierarchy')
    assert hasattr(graph, '_type_registry')
    assert hasattr(graph, '_namespace_uses')
    assert hasattr(graph, '_type_references')


def test_dependency_graph_builder_with_empty_modules() -> None:
    """Test that DependencyGraphBuilder can handle empty module dict."""
    modules: dict[str, Meta.ModuleMeta]
    graph: Resolver.DependencyGraph
    
    modules = {}
    graph = Resolver.DependencyGraphBuilder.build(modules)
    
    assert graph is not None


def test_dependency_graph_builder_with_single_module() -> None:
    """Test that DependencyGraphBuilder can handle a single module."""
    modules: dict[str, Meta.ModuleMeta]
    module: Meta.ModuleMeta
    graph: Resolver.DependencyGraph
    
    # Create a simple module with one namespace
    module = Meta.ModuleMeta()
    modules = {"test.ctd": module}
    
    graph = Resolver.DependencyGraphBuilder.build(modules)
    
    assert graph is not None
