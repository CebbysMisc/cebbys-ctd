#fmt: off
import sys
from pathlib import Path

# Prepend workspace source directories so local code is used (like pytest import behavior)
root = Path(__file__).resolve()
# Assume workspace root is one level above the package directory (two levels above this file)
repo_root = root.parent.parent
# Fallback: walk upward until a pyproject.toml is found
if not (repo_root / "pyproject.toml").exists():
    while repo_root != repo_root.parent and not (repo_root / "pyproject.toml").exists():
        repo_root = repo_root.parent

pkg_sources = [
    "cebbys-ctd-ghidra",
    "cebbys-ctd-antlr4",
    "cebbys-ctd-types",
    "cebbys-ctd-meta",
    "cebbys-ctd-resolver",
    "cebbys-ctd-loader",
    "cebbys-ctd-utility",
]

for pkg in pkg_sources:
    p = repo_root / pkg / "sources"
    if p.exists():
        sys.path.insert(0, str(p))

try:
    import importlib, inspect
    loader_mod = importlib.import_module('lv.cebbys.languages.ctd.loader')
    print('DEBUG: loader module file ->', inspect.getfile(loader_mod))
except Exception as _exc:
    print('DEBUG: loader import failed ->', _exc)

from lv.cebbys.languages.ctd.ghidra import (
    main,
)
from pathlib import (
    Path
)
#fmt: on

ROOT_PATH = Path(__file__).resolve().parent
CTD_ROOT_PATH = ROOT_PATH / "resources" / "ctd"

if __name__ == "__main__":
    print(f"Starting Ghidra with CTD root path: {CTD_ROOT_PATH}")
    main([CTD_ROOT_PATH])
