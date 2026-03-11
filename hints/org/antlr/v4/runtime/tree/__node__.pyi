import org.antlr.v4.runtime.tree.__tree__ as _TreeModule
import org.antlr.v4.runtime.__token__ as _TokenModule


class RuleNode(_TreeModule.ParseTree):
    ...


class TerminalNode(_TreeModule.ParseTree):
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/tree/TerminalNode.html"""
    def getSymbol(self) -> _TokenModule.Token: ...

class ErrorNode(TerminalNode):
    ...
