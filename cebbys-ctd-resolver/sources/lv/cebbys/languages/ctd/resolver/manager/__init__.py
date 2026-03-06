from lv.cebbys.languages.ctd.types.ctd import (
    Reference as ReferenceApi,
    Declaration,
    Builtin,
    Pointer,
    Alias,
    Array
)
from typing import (
    Any
)


class Reference(ReferenceApi):
    def __init__(self, storage: dict[str, Any], key:str) -> None:
        self.storage = storage
        self.key = key
    
    @property
    def value(self) -> Declaration:
        out = self.storage[self.key]
        if not isinstance(out, Alias):
            return out
        try:
            return out.base.value
        except:
            return out
        
    def __str__(self) -> str:
        return f"{self.value}"
        
    def __repr__(self) -> str:
        return f"{self.value}"


class CtdDeclarationStorage:
    storage: dict[str, Declaration] = {}
    open = False
    
    @staticmethod
    def start():
        CtdDeclarationStorage.open = True
        CtdDeclarationStorage.storage.clear()
        CtdDeclarationStorage.register(Builtin("char"))
        CtdDeclarationStorage.register(Builtin("short"))
        CtdDeclarationStorage.register(Builtin("int"))
        CtdDeclarationStorage.register(Builtin("long"))
        CtdDeclarationStorage.register(Builtin("float"))
        CtdDeclarationStorage.register(Builtin("double"))
        CtdDeclarationStorage.register(Builtin("void"))
    
    @staticmethod
    def stop():
        CtdDeclarationStorage.open = False

    @staticmethod
    def register(declaration: Any) -> Reference:    
        try:
            if not CtdDeclarationStorage.open:
                raise BaseException(f"Declaration registration storage is frozen")
            if not isinstance(declaration, Declaration):
                raise BaseException(f"Value is not of type {Declaration.__name__} but is {type(declaration).__name__}")
            if declaration.typeref in CtdDeclarationStorage.storage:
                raise BaseException(f"Declaration already registered with key '{declaration.typeref}'")
            
            CtdDeclarationStorage.storage[declaration.typeref] = declaration
            return reference(declaration.typeref)
        except BaseException as e:
            raise BaseException(f"Failed to register declaration '{declaration}'") from e

    @staticmethod
    def resolve(typeref:str|Declaration) -> Reference:
        if not isinstance(typeref, str):
            typeref = typeref.typeref

        if typeref in CtdDeclarationStorage.storage:
            return reference(typeref)
        elif typeref.endswith("*"):
            result = CtdDeclarationStorage.resolve(typeref[:-1])
            result = Pointer(result)
            return CtdDeclarationStorage.register(result)
        elif typeref.endswith("]"):
            start = typeref.rindex("[")
            size = int(typeref[start + 1:-1])
            result = CtdDeclarationStorage.resolve(typeref[:start])
            result = Array(result, size)
            return CtdDeclarationStorage.register(result)
        else:
            raise BaseException(f"No declaration found with typeref '{typeref}'")

    @staticmethod
    def tree() -> dict[str, Any]:
        storage = CtdDeclarationStorage.storage
        root = CtdDeclarationTree()
        for typeref, declaration in storage.items():
            if "::" not in typeref:
                root.declarations[typeref] = declaration
            else:
                *path, name = typeref.split("::")
                current = root
                for element in path:
                    if element not in current.modules:
                        current.modules[element] = CtdDeclarationTree()
                    current = current.modules[element]
                current.declarations[name] = declaration
        return root.nodes

class CtdDeclarationTree:
    def __init__(self) -> None:
        self.declarations: "dict[str, Declaration]" = {}
        self.modules: "dict[str, CtdDeclarationTree]" = {}

    @property
    def nodes(self) -> "dict[str, Any]":
        return { **{k: v.nodes for k, v in self.modules.items()}, **self.declarations }
    
    def __str__(self) -> str:
        elements: list[str] = []
        elements.extend([
            f"\t{name}: {"\n".join([f"\t{line}" for line in str(module).split("\n")])[1:]}"
            for name, module in self.modules.items()
        ])
        elements.extend([f"\t{d}" for d in self.declarations.keys()])
        return "{\n" + ",\n".join(elements) + "\n}"
    
    def __repr__(self) -> str:
        return self.__str__().replace("\n", " ").replace("\t", "")
        

def reference(typeref:str):
    return Reference(CtdDeclarationStorage.storage, typeref)