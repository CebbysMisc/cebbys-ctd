import lv.cebbys.languages.ctd.types.ctd as Ctd
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
    @staticmethod
    def link(modules: dict[str, Ctd.Module]):
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
                        if " " in meta.type_spec:
                            parts = meta.type_spec.split(" ")
                            if len(parts) == 2:
                                if parts[0] == "signed":
                                    declaration.signed = True
                                    type_name = parts[1]
                                elif parts[0] == "unsigned":
                                    declaration.signed = False
                                    type_name = parts[1]
                                else:
                                    declaration.signed = None
                                    type_name = parts[0]
                            else:
                                raise BaseException("Not implemented") 
                            
                            declaration.base = find_type_in_paths(module, paths, type_name)
                            LOGGER.warning(f"{declaration}")
                        else:
                            declaration.base = find_type_in_paths(module, paths, meta.type_spec)
                            LOGGER.warning(f"{declaration}")

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
