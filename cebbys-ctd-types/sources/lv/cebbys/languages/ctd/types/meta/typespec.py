import typing as Typing

from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar,
)


class TypespecMeta:
    def __repr__(self):
        return f"{type(self).__name__}[\"{self.__str__()}\"]"


class PointerTypespecMeta(TypespecMeta):
    base: Typing.Final[TypespecMeta]

    def __init__(self, base: TypespecMeta) -> None:
        super().__init__()
        self.base = base

    def __str__(self) -> str:
        return f"{self.base}*"


class ArrayTypespecMeta(TypespecMeta):
    base: Typing.Final[TypespecMeta]
    size: Typing.Final[int]

    def __init__(self, base: TypespecMeta, size: int) -> None:
        super().__init__()
        self.base = base
        self.size = size

    def __str__(self) -> str:
        return f"{self.base}[{self.size}]"


class TypedTypespecMeta(TypespecMeta):
    qualified_name: Typing.Final[str]
    signed: Typing.Final[bool | None]

    def __init__(self, qualified_name: str, signed: bool | None = None) -> None:
        super().__init__()
        self.qualified_name = qualified_name
        self.signed = signed

    def __str__(self) -> str:
        if self.signed == None:
            return self.qualified_name
        if self.signed == True:
            return f"signed {self.qualified_name}"
        return f"unsigned {self.qualified_name}"
