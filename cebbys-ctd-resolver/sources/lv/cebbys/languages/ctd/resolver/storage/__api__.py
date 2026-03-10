
class Reference[T]:
    @property
    def key(self) -> "str": ...
    
    @property
    def value(self) -> "T": ...

class LazyLoader[T]:
    def load(self, key: str) -> "T": ...

class Storage[T]:
    def __init__(self, loader: "LazyLoader[T]") -> None:
        self._content: "dict[str, T]" = {}
        self._loader = loader
        
    def register(self, key: "str", value: "T"): ...

    def reference(self, key: "str") -> "Reference[T]": ...