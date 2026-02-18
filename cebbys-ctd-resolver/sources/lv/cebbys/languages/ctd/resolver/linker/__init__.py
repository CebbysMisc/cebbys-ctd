import lv.cebbys.languages.ctd.types.ctd as Ctd
import lv.cebbys.languages.ctd.types.meta as Meta
from typing import (
    Final,
    Any
)


import lv.cebbys.languages.ctd.utility.logging as Logging
LOGGER = Logging.get_logger(__name__)


class ModuleLinkerCtx:
    def __init__(self, modules: dict[str, Ctd.Module]) -> None:
        self.modules: Final[dict[str, Ctd.Module]] = modules


class ModuleLinker:
    def __init__(self, modules: dict[str, Ctd.Module]) -> None:
        self.builtin_cache: dict[str, object] = {

        }
        self.type_cache: dict[str, Ctd.Declaration | None] = {

        }
        self.modules = modules

    def resolve(self, paths:list[str], typespec: Meta.TypespecMeta) -> Ctd.Declaration:
        if isinstance(typespec, Meta.PointerTypespecMeta):
            out = Ctd.Pointer(self.resolve(paths, typespec.base))
        
        elif isinstance(typespec, Meta.ArrayTypespecMeta):
            
            out = Ctd.Pointer()

        raise BaseException(f"Typespec {typespec} not found in paths {paths}")
    
    def resolve(self, path: str, typespec: Meta.TypespecMeta) -> Ctd.Declaration | None:
        # key = f"{path}::{typespec}"
        # if key in self.type_cache:
        #     return self.type_cache[key]

        out = None

        # if isinstance(typespec, Meta.PointerTypespecMeta):
        #     base = self.resolve(path, typespec.base)
        #     if base is not None:
        #         out = Ctd.Pointer(base)
        #         self.type_cache[key] = out
        # elif isinstance(typespec, Meta.ArrayTypespecMeta):
        #     base = self.resolve(path, typespec.base)
        #     if base is not None:
        #         out = Ctd.Array(base, typespec.size)
        #         self.type_cache[key] = out
        # elif isinstance(typespec, Meta.TypedTypespecMeta):
        #     if typespec.qualified_name in self.builtin_cache:
        #         return 

        #     pass

            
        
        return out

    @staticmethod
    def link(modules: dict[str, Ctd.Module]):
        instance = ModuleLinker(modules)

        for _, module in modules.items():
            module.includes = [ modules[i.path] for i in module.meta.includes ]

            for namespace in module.namespaces:
                paths = [
                    namespace.path,
                    *namespace.meta.uses
                ]
                LOGGER.debug(f"Use paths: {paths}")
                for declaration in namespace.declarations:
                    if isinstance(declaration, Ctd.Typedef):
                        meta = declaration.meta
                        type_spec = meta.type_spec
                        
                        # Unwrap to get base type (handle arrays and pointers)
                        while isinstance(type_spec, (Meta.ArrayTypespecMeta, Meta.PointerTypespecMeta)):
                            type_spec = type_spec.base
                        
                        # Now we have TypedTypespecMeta
                        if isinstance(type_spec, Meta.TypedTypespecMeta):
                            declaration.signed = type_spec.signed
                            type_name = type_spec.qualified_name
                            declaration.base = find_type_in_paths(module, paths, type_name)
                            LOGGER.warning(f"{declaration}")
                        else:
                            raise TypeError(f"Expected TypedTypespecMeta but got {type(type_spec)}")

                    elif isinstance(declaration, Ctd.Alias):
                        alias_meta = declaration.meta
                        # TODO implement alias parsing

                        LOGGER.warning(f"{alias_meta.name} = {alias_meta.type_spec}")

                    # TODO implement the rest of Ctd.* parsing

builtin_cache: dict[str, Ctd.Builtin] = {
    "char": Ctd.Builtin("char"),
    "short": Ctd.Builtin("short"),
    "int": Ctd.Builtin("int"),
    "long": Ctd.Builtin("long"),
    "float": Ctd.Builtin("float"),
    "double": Ctd.Builtin("double"),
    "void": Ctd.Builtin("void"),
}
type_cache: dict[str, Ctd.Declaration|None] = {}

def find_type_in_paths(module: Ctd.Module, paths: list[str], name:str) -> Ctd.Declaration:
    type_ref : Ctd.Declaration | None = None
    if name in builtin_cache:
        return builtin_cache[name]
    for path in paths:
        type_ref = get_type(module, path, name)
        if type_ref:
            return type_ref
    if not type_ref:
        raise BaseException(f"Type '{name}' not found in module '{module.name}' and paths {paths}")

def get_type(module: Ctd.Module, path: str, name: str):
    global type_cache
    key = f"{module.name}:{path}:{name}"
    if key not in type_cache:
        modules = [
            module,
            *module.includes
        ]
        for module in modules:
            for namespace in module.namespaces:
                if path != namespace.path:
                    continue
                for declaration in namespace.declarations:
                    if name != declaration.name:
                        continue
                    else:
                        type_cache[key] = declaration
                        return declaration
        type_cache[key] = None
        return None
    return type_cache[key]
                    
def get_module(modules: dict[str, Ctd.Module], *, by_name:str|None = None):
    if by_name:
        return modules[by_name]
    raise BaseException("Not implemented")
