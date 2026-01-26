import org.antlr.v4.runtime.__token__ as _TokenModule
import org.antlr.v4.runtime.__rule__ as _RuleModule
import org.antlr.v4.runtime.atn as _AtnModule
import typing as _Typing


class Recognizer[S, I]:
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/Recognizer.html"""
    _interp: I
    EOF: int


class Parser(Recognizer[_TokenModule.Token, _AtnModule.ParserATNSimulator]):
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/Parser.html"""

    def enterRule(
        self,
        ctx: _RuleModule.ParserRuleContext,
        state: int,
        rule_index: int
    ) -> None: ...
