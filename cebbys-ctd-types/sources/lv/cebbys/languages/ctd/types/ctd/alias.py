from lv.cebbys.languages.ctd.types.ctd.declaration import Declaration
from lv.cebbys.languages.ctd.types.ctd.decorator import Decorator
from lv.cebbys.languages.ctd.types.meta import AliasMeta

class Alias(Declaration[AliasMeta]):
    """Represents an alias declaration."""
    decorators: list[Decorator]
    base: Declaration
    meta: AliasMeta

    def __init__(self) -> None:
        super().__init__()
        self.decorators = []