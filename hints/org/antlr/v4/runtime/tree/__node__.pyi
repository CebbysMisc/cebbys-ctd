import org.antlr.v4.runtime.tree.__tree__ as _Tree


class RuleNode(_Tree.ParseTree):
    ...


class TerminalNode(_Tree.ParseTree):
    ...


class ErrorNode(TerminalNode):
    ...
