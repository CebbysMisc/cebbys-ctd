from lv.cebbys.languages.ctd.ghidra.datatype.storage.connector.sqlite.__utility__ import (
    CursorExecute,
)
from dataclasses import (
    dataclass,
    field,
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
    type_path: Optional[str] = None
    ghidra_uuid: Optional[int] = None
    sha256: Optional[str] = None
