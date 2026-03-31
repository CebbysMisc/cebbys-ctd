from lv.cebbys.languages.ctd.ghidra.datatype.storage.connector.sqlite.__utility__ import (
    CursorExecute,
)
from dataclasses import (
    dataclass,
)
from typing import (
    Optional,
)
from uuid import (
    UUID as Uuid,
)


@dataclass
class CtdTypeMapping(CursorExecute):
    type_uuid: Uuid = CursorExecute.primary_key()
    ghidra_uuid: Optional[int] = None
