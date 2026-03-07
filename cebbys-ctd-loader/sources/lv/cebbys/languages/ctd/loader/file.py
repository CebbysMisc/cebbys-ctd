from pathlib import (
    Path
)
from typing import (
    Final
)


class CtdFileCtx:
    def __init__(self, root: Path, path: Path) -> None:
        self.root: Final[Path] = root
        self.path: Final[Path] = path
        self.name: Final[str] = str(self.path.relative_to(self.root)).removesuffix(".ctd")

class CtdFileCtxLoader:
    @staticmethod
    def load(roots: list[Path]):
        ctd_files:list[CtdFileCtx] = []
        for root in roots:
            if not root.is_dir():
                continue
            for path in root.rglob('*.ctd'):
                if not path.is_file():
                    continue
                ctd_files.append(CtdFileCtx(root, path))
        return ctd_files