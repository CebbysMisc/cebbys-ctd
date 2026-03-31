from lv.cebbys.languages.ctd.types.meta import (
    DecoratorMeta,
)
from lv.cebbys.languages.ctd.types.ctd import (
    Decorator,
)


class DecoratorConstructor:
    @staticmethod
    def construct(meta: "DecoratorMeta") -> "Decorator":
        return Decorator(meta)
