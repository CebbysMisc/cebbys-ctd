from threading import (
    Thread,
)
from logging import (
    basicConfig,
    INFO,
    info,
)
from pathlib import (
    Path,
)
from typing import (
    Callable,
    Iterable,
    overload,
    Any,
)
from time import (
    sleep,
)
from uuid import (
    uuid4,
)

basicConfig(level=INFO, format="%(message)s")

class CtdIndexer:
    class ModuleIndexerThread(Thread):
        def __init__(self, consumer: Callable[[list[str]], Any]) -> None:
            super().__init__(name="ctd-indexer-thread", target=self.index, daemon=True)
            self._consumer = consumer
            self._cached: set[str] = set()
            self._roots: set[Path] = set()

        @property
        def roots(self):
            return self._roots
        
        @roots.setter
        def roots(self, value: Iterable[Path]):
            self._roots = set(value)

        def index(self):
            while True:
                try:
                    modules: set[str] = set()
                    for root in self.roots:
                        try:
                            modules = modules | {
                                str(p.relative_to(root))[:-4].replace("\\", "/")
                                for p in root.glob("**/*.ctd")
                            }
                        except:
                            pass
                    if modules != self._cached:
                        info(f"Updating modules to {modules}")
                        self._cached = modules
                        self._consumer(list(modules))
                except:
                    pass
                finally:
                    sleep(1)

    process: Any
    thread: ModuleIndexerThread
    _ctds: tuple[str, ...] = ()

    @classmethod
    def start(cls):
        if hasattr(cls, "process"):
            raise BaseException(f"Module indexer has already started with process id: {cls.process}")
        cls.process = uuid4()
        info(f"[ModuleIndexer] Starting indexer process: {cls.process}")
        cls.thread = CtdIndexer.ModuleIndexerThread(CtdIndexer.ctds)
        cls.thread.start()

    @overload
    @classmethod
    def roots(cls) -> set[Path]: ...
    @overload
    @classmethod
    def roots(cls, roots: Iterable[Path]) -> None: ...
    @classmethod
    def roots(cls, roots: Iterable[Path]|None = None) -> set[Path]|None:
        if not hasattr(cls, "process"):
            raise BaseException(f"Indexing thread not started")
        if roots is None:
            return cls.thread.roots
        else:
            cls.thread.roots = roots

    @overload
    @classmethod
    def ctds(cls) -> tuple[str, ...]: ...
    @overload
    @classmethod
    def ctds(cls, modules:Iterable[str]) -> None: ...
    @classmethod
    def ctds(cls, modules:Iterable[str]|None = None) -> tuple[str, ...]|None:
        if modules is None:
            return cls._ctds
        else:
            info(f"[ModuleIndexer] Modules refreshed: {modules}")
            cls._ctds = tuple(modules)

    @classmethod
    def close(cls):
        if hasattr(cls, "process"):
            info(f"[ModuleIndexer] Closing indexer process: {cls.process}")
            cls.process = None
            cls.thread.join()