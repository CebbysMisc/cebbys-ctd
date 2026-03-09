# from lv.cebbys.languages.ctd.lsp.server import create_server

# __all__ = ["create_server"]

from pygls.lsp.server import (
    LanguageServer
)
from lv.cebbys.languages.ctd.lsp.types import (
    Completion,
)

SERVER = LanguageServer("ctd-language-server", "v1.0")

@SERVER.feature(
    Completion.ID,
    Completion.Options(trigger_characters=["."])
)
def completions(params: Completion.Params):
    pass
