from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import AliasMeta


class Alias(Declaration):
    """Represents an alias declaration."""
    decorators: list[Decorator]
    base: Declaration
    meta: AliasMeta