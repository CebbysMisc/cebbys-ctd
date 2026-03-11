
from lv.cebbys.languages.ctd.meta.parser import (
    CtdMetaParser
)
from lv.cebbys.languages.ctd.types.meta import (
    ModuleMeta,
)
from lv.cebbys.languages.ctd.lsp.types import (
    Completion,
)
from lv.cebbys.languages.ctd.antlr4 import (
    CtdGrammar,
    CtdParser,
)
from pygls.lsp.server import (
    LanguageServer
)
from logging import (
    basicConfig,
    error,
    INFO,
    info,
)
from pathlib import (
    Path
)
from typing import (
    Any
)

basicConfig(level=INFO, format="%(message)s")

class CompletionCtx:
    server: LanguageServer
    params: Completion.Params
    meta: ModuleMeta


class ModuleCodeCompleter:
    def get_suggestions(self, server: LanguageServer, params: Completion.Params):
        info(f"Getting code completions")
        suggestions: list[Completion.Item] = []
        incomplete: bool = True
        ctx = CompletionCtx()
        ctx.server = server
        ctx.params = params
        document = server.workspace.get_text_document(params.text_document.uri)
        filename: Any = document.filename
        antlr = CtdParser.moduleDeclaration(document.source)
        # try:
        #     ctx.meta = CtdMetaParser.parse_module(
        #         Path(server.workspace.root_path).resolve(), # type: ignore
        #         Path(document.path).resolve(),
        #         filename[:-4],
        #         antlr,
        #     )
        # except BaseException as e:
        #     error("Failure mapping antlr context to meta", exc_info=e, stack_info=True, stacklevel=3)
        # if self.is_outside_namespace(ctx):
        #     if self.is_above_namespaces(ctx):
        #         suggestions.append(Completion.Item(label="import "))
        #     suggestions.append(Completion.Item(label="namespace "))
        # else:   
        #     suggestions.append(Completion.Item(label="use "))
        #     suggestions.append(Completion.Item(label="interface "))
        #     suggestions.append(Completion.Item(label="structure "))
        #     suggestions.append(Completion.Item(label="function "))
        #     suggestions.append(Completion.Item(label="typedef "))
        #     suggestions.append(Completion.Item(label="alias "))
        #     suggestions.append(Completion.Item(label="enum "))
        #     suggestions.append(Completion.Item(label="flag "))

        return Completion.List(is_incomplete=incomplete, items=suggestions)

    def is_above_namespaces(self, ctx: CompletionCtx):
        line = ctx.params.position.line
        min: int = 0xFFFFFFFF
        for namespace in ctx.meta.namespaces:
            current: int = namespace.ctx.start.line # type: ignore
            if current < min:
                min = current
        info(f"Checking if cursor index: {line} is before first namespace line: {min}")
        return line < min

    def is_outside_namespace(self, ctx: CompletionCtx):
        return True
        # row = ctx.params.position.line
        # col = ctx.params.position.character
        # info(f"Checking if cursor {row}:{col} is inside namespaces")
        # return all([ns.range.is_outside(row, col) for ns in ctx.meta.namespaces])