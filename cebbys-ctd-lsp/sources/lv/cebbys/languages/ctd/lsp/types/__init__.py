from lsprotocol import (
    types as LspTypes
)
from typing import (
    Final
)

class Completion:
    class Options(LspTypes.CompletionOptions): ...
    class Params(LspTypes.CompletionParams): ...
    class Item(LspTypes.CompletionItem): ...
    class List(LspTypes.CompletionList): ...
    ID: Final = LspTypes.TEXT_DOCUMENT_COMPLETION

class OpenDocument:
    class Params(LspTypes.DidOpenTextDocumentParams): ...
    ID: Final = LspTypes.TEXT_DOCUMENT_DID_OPEN

class Initialize:
    class Params(LspTypes.InitializeParams): ...
    ID: Final = LspTypes.INITIALIZE