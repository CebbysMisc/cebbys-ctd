import lv.cebbys.languages.ctd.antlr4 as Antlr4
import typing as Typing
from lv.cebbys.languages.ctd.antlr4 import CtdParser

__all__ = ["CtdParser", "CtdContextParser"]

R = Typing.TypeVar("R", bound=Antlr4.ParserRuleContext)
O = Typing.TypeVar("O")


class ParserBase(Antlr4.CtdVisitor):
    def rules[T1](self, ctx: Antlr4.ParserRuleContext, look: type[T1]) -> list[T1]:
        return ctx.getTypedRuleContexts(look)  # type: ignore

    def rule[T1](self, ctx: Antlr4.ParserRuleContext, look: type[T1], index: int = 0) -> T1:
        out = self.optional_rule(ctx, look, index)
        if not out:
            raise BaseException(f"Ctx: {ctx} must have rule: {look} at index: {index}")
        return out

    def optional_rule[T1](self, ctx: Antlr4.ParserRuleContext, look: type[T1], index: int = 0) -> T1 | None:
        return ctx.getTypedRuleContext(look, index)  # type: ignore

    def tokens(self, ctx: Antlr4.ParserRuleContext, token: int) -> list[Antlr4.TerminalNode]:
        return ctx.getTokens(token)  # type: ignore

    def token(self, ctx: Antlr4.ParserRuleContext, token: int, index: int = 0) -> Antlr4.TerminalNode:
        out = self.optional_token(ctx, token, index)
        if not out:
            raise BaseException(f"Ctx: {ctx} must have token: {token} at index: {index}")
        return out

    def optional_token(self, ctx: Antlr4.ParserRuleContext, token: int, index: int = 0) -> Antlr4.TerminalNode | None:
        return ctx.getToken(token, index)  # type: ignore

    def text(self, ctx: Typing.Any) -> str:
        out = self.optional_text(ctx)
        if not out:
            raise BaseException(f"Ctx: {ctx} must have text property")
        return out

    def optional_text(self, ctx: Typing.Any) -> str | None:
        try:
            return ctx.getText()  # type: ignore
        except:
            return None

    def qualified_name(self, ctx: Antlr4.CtdParser.QualifiedNameContext):
        """Extract qualified name from context.

        Args:
            ctx: Qualified name context

        Returns:
            Qualified name as string (e.g., 'ns1::ns2::name')
        """
        return '::'.join([
            self.text(id_token)
            for id_token in self.tokens(ctx, Antlr4.CtdParser.IDENTIFIER)
        ])


class CtdContextParser(Typing.Generic[R, O]):
    @staticmethod
    def instance() -> 'CtdContextParser[R, O]': ...

    def parse(self, ctx: R) -> O: ...


class CtdDeclaractionContextParser(Typing.Generic[R, O]):
    @staticmethod
    def instance() -> 'CtdDeclaractionContextParser[R, O]': ...

    def parse(self, namespace: str, ctx: R) -> O: ...


class CtdContextParserBase(ParserBase, CtdContextParser[R, O]):
    ...


class CtdDeclaractionContextParserBase(ParserBase, CtdDeclaractionContextParser[R, O]):
    ...
