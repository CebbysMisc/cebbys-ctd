from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    EnumMemberMeta,
    EnumMeta
)

class EnumMember:
    """Represents an enum member."""
    name: str
    value: int | None
    meta: EnumMemberMeta


class Enum(Declaration[EnumMeta]):
    """Represents an enum declaration."""
    decorators: list[Decorator]
    members: list[EnumMember]
    base: Declaration | None

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base = None
