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


class Flag(Declaration):
    """Represents a flag declaration."""
    decorators: list[Decorator]
    base: Declaration | None
    members: list[FlagMember]
    meta: FlagMeta
