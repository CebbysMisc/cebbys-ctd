from lv.cebbys.languages.ctd.types.exception import (
    CtdInvalidParameterException,
    CtdException,
)
from pathlib import (
    Path,
)
from typing import (
    Iterable,
    Any,
)

class CtdModuleLoader:
    def __init__(self, roots: Iterable[Path]) -> None:
        try:
            self._roots = set([root.resolve() for root in roots])
            if len(self._roots) == 0:
                raise CtdInvalidParameterException("roots", f"value must contain at least one root path")
        except BaseException as e:
            raise CtdException(f"Failed to create {type(self).__name__}") from e
    
    def load(self, module_id: str):
        try:
            lookups = [root / f"{module_id}.ctd" for root in self._roots]
            matches = [lookup for lookup in lookups if lookup.is_file()]
            length = len(matches)
            if length == 0:
                raise CtdException(f"No modules found at: {lookups}")
            elif length > 1:
                raise CtdException(f"Multiple modules found matching at: {matches}")
            matching = matches[0]
        except BaseException as e:
            raise CtdException(f"Failed to load module '{module_id}'") from e
        

    def resolve(self, module_id: str, type_reference: str) -> Any: ...