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


class Enum(Declaration):
    """Represents an enum declaration."""
    decorators: list[Decorator]
    base: Declaration | None
    members: list[EnumMember]
    meta: EnumMeta
