import lv.cebbys.languages.ctd.antlr4 as Antlr4
import typing as Typing
from lv.cebbys.languages.ctd.antlr4 import CtdParser

__all__ = ["CtdParser", "CtdContextParser"]

T = Typing.TypeVar("T", bound=Antlr4.ParserRuleContext)
O = Typing.TypeVar("O")


class CtdContextParser(Antlr4.CtdVisitor, Typing.Generic[T, O]):
    @staticmethod
    def instance() -> 'CtdContextParser[T, O]': ...

    def parse(self, ctx: T) -> O: ...


class CtdDeclaractionContextParser(Antlr4.CtdVisitor, Typing.Generic[T, O]):
    @staticmethod
    def instance() -> 'CtdDeclaractionContextParser[T, O]': ...

    def parse(self, namespace: str, ctx: T) -> O: ...

    def _parseGetText(self, callable: Typing.Callable[[], Typing.Any]) -> str:
        ctx: SupportsGetText = callable()
        return ctx.getText()

    def _parseTypeSpec(self, callable: Typing.Callable[[], Typing.Any]) -> str:
        """Extract type specification as string.

        Args:
            ctx: Type spec context

        Returns:
            Type specification string
        """
        ctx: Antlr4.CtdParser.TypeSpecContext = callable()
        parts: list[str]
        array_ctx: Antlr4.CtdParser.ArrayModifierContext | None
        pointer_ctx: Antlr4.CtdParser.PointerModifierContext | None

        parts = []

        # Handle sign modifier
        if ctx.signModifier():
            parts.append(self._parseGetText(ctx.signModifier))  # type: ignore

        # Handle primitive type
        if ctx.primitiveType():
            parts.append(self._parseGetText(ctx.primitiveType))  # type: ignore

        # Handle type reference
        if ctx.typeReference():
            parts.append(self._parseGetText(ctx.typeReference().qualifiedName))  # type: ignore

        # Handle array modifier - check in typeSpec first, then in typeReference
        array_ctx = ctx.arrayModifier()  # type: ignore
        if array_ctx is None and ctx.typeReference():
            array_ctx = ctx.typeReference().arrayModifier()  # type: ignore

        if array_ctx:
            parts.append(array_ctx.getText())  # type: ignore

        # Handle pointer modifier - check in typeSpec first, then in typeReference
        pointer_ctx = ctx.pointerModifier()  # type: ignore
        if pointer_ctx is None and ctx.typeReference():
            pointer_ctx = ctx.typeReference().pointerModifier()  # type: ignore

        if pointer_ctx:
            parts.append(pointer_ctx.getText())  # type: ignore

        return ' '.join(parts)


class SupportsGetText:
    def getText(self) -> str: ...
