from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import (
    FlagMemberMeta,
    FlagMeta
)


class FlagMember:
    """Represents a flag member."""
    name: str
    offset: int | None
    meta: FlagMemberMeta


class Flag(Declaration[FlagMeta]):
    """Represents a flag declaration."""
    decorators: list[Decorator]
    members: list[FlagMember]
    base: Declaration | None

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []
        self.members = []
        self.base = None
