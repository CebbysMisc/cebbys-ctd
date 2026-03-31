from lv.cebbys.languages.ctd.utility.logging import (
    get_logger,
)
from lv.cebbys.languages.ctd.loader import (
    CtdLoader,
)
from threading import (
    Thread,
    Event,
)
from importlib import (
    reload,
)
from pathlib import (
    Path,
)
from typing import (
    Any
)
from types import (
    ModuleType,
)
from time import (
    sleep,
)


logger = get_logger(__name__)


class Synchronizer(Thread):
    def __init__(self, roots: list[Path]) -> None:
        super().__init__(target=self.__thread__, daemon=True)
        self._stop_event = Event()
        self._roots = roots

    def __thread__(self) -> None:
        sleep(10)
        from pyghidra import (
            started,
        )
        while not self._stop_event.is_set():
            if not started():
                logger.info("Ghidra is not started, waiting...")
                sleep(5)
                continue
            try:
                import lv.cebbys.languages.ctd.ghidra.process.synchronize.thread as SynchronizeThread
                import lv.cebbys.languages.ctd.ghidra as GhidraModule
                deep_reload(SynchronizeThread)
                deep_reload(GhidraModule)
                SynchronizeThread.tick(self._roots)
            except BaseException as e:
                logger.error(f"Error in synchronization thread: {e}", exc_info=True)

    def stop(self) -> None:
        self._stop_event.set()


def deep_reload(module: ModuleType, visited: set[Any] | None = None):
    if visited is None:
        visited = set()
    if module in visited:
        return
    visited.add(module)

    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, ModuleType):
            if obj.__name__.startswith(module.__name__):
                deep_reload(obj, visited)
    try:
        reload(module)
    except Exception as e:
        logger.error(f"Reload failed for {module.__name__}: {e}", exc_info=True)
