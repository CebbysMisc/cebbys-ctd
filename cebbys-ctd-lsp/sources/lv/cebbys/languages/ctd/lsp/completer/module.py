from lv.cebbys.languages.ctd.lsp.types import (
    Completion,
)
from pygls.lsp.server import (
    LanguageServer
)

class ModuleCodeCompleter:
    def get_suggestions(self, server: LanguageServer, params: Completion.Params):
        suggestions: list[str]
        if self.is_above_namespaces():
            pass
        elif self.is_outside_namespace():
            pass
        else:
            pass



    def is_above_namespaces(self):
        pass

    def is_outside_namespace(self):
        pass