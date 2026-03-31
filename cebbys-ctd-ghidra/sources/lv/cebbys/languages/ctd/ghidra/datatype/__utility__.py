from ghidra.program.model.data import (  # type: ignore
    CategoryPath,
)
from lv.cebbys.languages.ctd.types.ctd import (
    Namespace,
)


ROOT = CategoryPath("/")


def get_category_path(namespace: Namespace) -> CategoryPath:
    path = namespace.path.split("::")
    if path:
        return CategoryPath(ROOT, *path)
    else:
        return ROOT
