from lv.cebbys.languages.ctd.resolver.storage import (
    Storage
)

from typing import (
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.types.ctd import (
        Module
    )

class ModuleStorage(Storage["Module"]):
    pass