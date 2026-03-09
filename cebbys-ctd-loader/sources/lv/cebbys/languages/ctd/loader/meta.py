from lv.cebbys.languages.ctd.loader.antlr import (
    CtdAntlrCtx
)
from lv.cebbys.languages.ctd.types.meta import (
    ModuleMeta
)
from lv.cebbys.languages.ctd.meta.parser import (
    CtdMetaParser
)

class CtdMetaLoader:
    @staticmethod
    def load(ctxs: list[CtdAntlrCtx]):
        contexts: list[ModuleMeta] = []
        for ctx in ctxs:
            try:
                contexts.append(
                    CtdMetaParser.parse_module(ctx.root, ctx.path, ctx.name, ctx.ctx)
                )
            except Exception as e:
                raise BaseException(f"Failed to process module '{ctx.name}' from '{ctx.path}'") from e
        return contexts