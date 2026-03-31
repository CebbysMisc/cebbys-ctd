
class Token:
    """https://www.antlr.org/api/Java/org/antlr/v4/runtime/Token.html"""
    @property
    def line(self) -> int: ...
    @property
    def column(self) -> int: ...
