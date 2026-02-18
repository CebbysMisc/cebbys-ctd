from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    StructureMemberMeta,
    StructureMeta
)

class StructureMember:
    """Represents a structure member."""
    name: str
    type: Declaration
    meta: StructureMemberMeta


class Structure(Declaration):
    """Represents a structure declaration."""
    decorators: list[Decorator]
    base: Declaration | None
    members: list[StructureMember]
    meta: StructureMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base = None
