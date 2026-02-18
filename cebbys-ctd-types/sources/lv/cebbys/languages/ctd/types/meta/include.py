__all__ = ['IncludeMeta']


class IncludeMeta:
    # TODO: Add code comments as TypedefMeta

    def __init__(self):
        self._path: str | None = None

    @property
    def path(self) -> str:
        if not self._path:
            raise BaseException("Path is not initialized")
        return self._path

    def set_path(self, path: str) -> None:
        self._path = path
