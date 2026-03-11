
import org.antlr.v4.runtime.__token__ as _TokenModule
import org.antlr.v4.runtime.tree as _TreeModule
import typing as _Typing


class RuleContext:
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/RuleContext.html"""

    def accept[T](self, visitor: _TreeModule.ParseTreeVisitor[T]) -> T: ...

    def getText(self) -> str: ...


_T = _Typing.TypeVar("_T", bound=_TreeModule.ParseTree)


class ParserRuleContext(RuleContext):
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/ParserRuleContext"""

    @property
    def start(self) -> _TokenModule.Token: ...

    @property
    def end(self) -> _TokenModule.Token: ...

    def getToken(self, type: int, index: int) -> _TreeModule.TerminalNode: ...

    def getTokens(self, type: int, index: int) -> list[_TreeModule.TerminalNode]: ...

    def getTypedRuleContexts(self, ctx_type: type[_T]) -> list[_T]: ...

    def getTypedRuleContext(self, ctx_type: type[_T], index: int) -> _T: ...

    @_Typing.overload
    def getChild(self, index: int, ctx_type: type[_T]) -> _T: ...

    @_Typing.overload
    def getChild(self, index: int) -> _TreeModule.ParseTree: ...
