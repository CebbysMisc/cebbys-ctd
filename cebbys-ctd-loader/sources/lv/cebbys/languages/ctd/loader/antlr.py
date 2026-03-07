from lv.cebbys.languages.ctd.loader.file import (
    CtdFileCtx
)
from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar,
    CtdParser
)
from pathlib import (
    Path
)
from typing import (
    Final
)


ModuleDeclarationContext = CtdGrammar.ModuleDeclarationContext

class CtdAntlrCtx:
    def __init__(self, file: CtdFileCtx, module: ModuleDeclarationContext) -> None:
        self.root: Final[Path] = file.root
        self.path: Final[Path] = file.path
        self.name: Final[str] = file.name
        self.ctx: Final[ModuleDeclarationContext] = module

class CtdAntlrCtxLoader:
    @staticmethod
    def load(files: list[CtdFileCtx]):
        contexts: list[CtdAntlrCtx] = []
        for file in files:
            try:
                content = file.path.read_text(encoding='utf-8')
                module = CtdParser.moduleDeclaration(content)
                contexts.append(CtdAntlrCtx(file, module))
            except Exception as e:
                raise BaseException(f"Failed to process module '{file.name}' from '{file.path}'") from e
        return contexts