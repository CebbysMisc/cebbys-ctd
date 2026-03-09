from lsprotocol import (
    types as LspTypes
)
from typing import (
    Final
)

class Completion:
    class Options(LspTypes.CompletionOptions): ...
    class Params(LspTypes.CompletionParams): ...
    ID: Final = LspTypes.TEXT_DOCUMENT_COMPLETION