# from lv.cebbys.languages.ctd.lsp.server import create_server

# __all__ = ["create_server"]

from lv.cebbys.languages.ctd.lsp.indexer.ctd import (
    CtdIndexer
)
from lv.cebbys.languages.ctd.lsp.context import (
    CtdLspContext
)
from lv.cebbys.languages.ctd.lsp.types import (
    Completion,
    Initialize,
)
from pygls.lsp.server import (
    LanguageServer
)
from pathlib import (
    Path
)
from logging import (
    basicConfig,
    INFO,
    info,
)
from lv.cebbys.languages.ctd.lsp.completer.module import (
    ModuleCodeCompleter,
)

CONTEXT = CtdLspContext()
SERVER = LanguageServer("ctd-language-server", "v1.0")

# @SERVER.feature(
#     Initialize.ID
# )
# def initialize(server: LanguageServer, params: Initialize.Params):
#     try:
#         root = Path(str(params.root_uri))
#         reload_module_list([root])
#     except BaseException as e:
#         raise BaseException("Failed to initialize cebbys-type-definition-server") from e

COMPLETER = ModuleCodeCompleter()


@SERVER.feature(
    Completion.ID,
    Completion.Options(trigger_characters=["."])
)
def completions(server: LanguageServer, params: Completion.Params):
    roots = CtdIndexer.roots()
    current = set([Path(str(server.workspace.root_path))])
    if roots != current:
        CtdIndexer.roots(current)

    # document = server.workspace.get_text_document(params.text_document.uri)
    # document.source
    # line = document.lines[params.position.line].strip()

    # if line.startswith("include"):
    #     prefix = line.removeprefix("include").strip()
    #     items = list(CtdIndexer.ctds())
    #     if len(prefix) > 0:
    #         items = [i for i in items if i.startswith(prefix)]
    #     return Completion.List(is_incomplete=True, items=[
    #         Completion.Item(label=f"\"{module}\"")
    #         for module in items
    #     ])

    return COMPLETER.get_suggestions(server, params)

def main():
    CtdIndexer.start()
    try:
        basicConfig(level=INFO, format="%(message)s")
        SERVER.start_io()
    finally:
        CtdIndexer.close()

if __name__ == "__main__":
    main()