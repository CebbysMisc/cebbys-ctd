
class Reference[T]:
    @property
    def key(self) -> "str": ...
    
    @property
    def value(self) -> "T": ...

class Storage[T]:
    def __init__(self) -> None:
        self.content: "dict[str, T]" = {}
        
    def register(self, key: "str", value: "T"): ...

    def reference(self, key: "str") -> "Reference[T]": ...