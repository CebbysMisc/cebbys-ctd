from lv.cebbys.languages.ctd.resolver.linker.resolver.__api__ import *


class BasicTypespecResolver(TypespecResolverApi):
    """Default typespec resolver using cached hierarchical search.
    
    Uses Algorithm 3 (Cached Hierarchical Search) as it provides:
    - Best performance for repeated lookups (common in large codebases)
    - Minimal duplicate searches across namespaces
    - Simple, predictable behavior
    - Good balance of speed and memory usage
    
    Algorithm rationale:
    - Algorithm 1 (Iterative): Too slow for large projects (no caching)
    - Algorithm 2 (Recursive): Elegant but stack overhead, no inter-call caching
    - Algorithm 3 (Cached): ✓ Best overall - fast, efficient, scalable
    - Algorithm 4 (Breadth-first): Overkill for simple cases, harder to debug
    """
    
    def resolve(
        self, 
        module: Ctd.Module, 
        namespace: Ctd.Namespace, 
        typespec: Meta.TypespecMeta
    ) -> Ctd.Declaration:
        """Resolve typespec to declaration using cached hierarchical search.
        
        See TypespecResolverApi.resolve() for full documentation.
        """
        return self._resolve_cached_hierarchical(module, namespace, typespec)