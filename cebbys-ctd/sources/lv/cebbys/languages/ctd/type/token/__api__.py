from dataclasses import (
    dataclass,
)
from pathlib import (
    Path,
)
from typing import (
    runtime_checkable,
    TYPE_CHECKING,
    Protocol,
    Self,
    Any,
)
from mmap import (
    ACCESS_READ,
    mmap,
)


if TYPE_CHECKING:
    from lv.cebbys.languages.ctd.antlr4 import (
        CtdGrammar,
    )
    from org.antlr.v4.runtime import (
        ParserRuleContext,
    )


@runtime_checkable
class FileCursorProtocol(Protocol):
    @property
    def line(self) -> int:
        """The line number of the cursor in document, starting from 0.
        
        Example:
        ```python
        def main() -> None:
            |...
        ```
        The cursor is at line 2, so the line number is 1.
        """
        ...
    
    @property
    def char(self) -> int:
        """The character position of the cursor in the line, starting from 0.
        
        Example:
        ```python
        def main() -> None:
            |...
        ```
        The cursor is at character position 4 on line 2, so the char number is 4."""
        ...


class FileCursor:
    def __init__(self, *, line: int, char: int) -> None:
        self._line = line
        self._char = char

    @property
    def line(self) -> int:
        return self._line

    @property
    def char(self) -> int:
        return self._char
    
    @staticmethod
    def start(path: Path) -> FileCursorProtocol:
        return FileCursor(line=0, char=0)
    
    @staticmethod
    def end(path: Path) -> FileCursorProtocol:
        with open(path, "rb") as file:
            i = 0
            with mmap(file.fileno(), 0, access=ACCESS_READ) as content:
                size = content.size()
                while True:
                    line = content.readline()
                    if content.tell() >= size:
                        return FileCursor(line=i, char=len(line))
                    i += 1


@runtime_checkable
class FileRangeProtocol(Protocol):
    """The range of contents within a file.
    
    Exaple:
    ```python
    def main() -> None:
        |...|
    ```
    The range starts at the character position 4 on line 2, and ends at the character position 7 on line 2.
    
    So the file range points to content `...` within this range
    """

    @property
    def start(self) -> FileCursorProtocol:
        """The (Inclusive) start position of the range."""
        ...
    
    @property
    def end(self) -> FileCursorProtocol:
        """The (Exclusive) end position of the range."""
        ...


class FileRange:
    def __init__(self, *, start: FileCursorProtocol, end: FileCursorProtocol) -> None:
        self._start = start
        self._end = end

    @property
    def start(self) -> FileCursorProtocol:
        return self._start

    @property
    def end(self) -> FileCursorProtocol:
        return self._end


@runtime_checkable
class ReferableProtocol(Protocol):
    @property
    def name(self) -> str:
        """The name of the referable element."""
        ...
    
    @property
    def path(self) -> str:
        """The path of the referable element.

        Example - `example::element::path::value`"""
        ...

    @property
    def pathname(self) -> str:
        """The path and name of the referable element.

        Example:
        * path: `example::element::path`
        * name: `value`
        * pathname: `example::element::path::value::name`
        """
        ...


class Reference:
    def __init__(self, path: str, name: str) -> None:
        self._path = path
        self._name = name

    @property
    def path(self) -> str:
        return self._path

    @property
    def name(self) -> str:
        return self._name

    @property
    def pathname(self) -> str:
        return f"{self.path}::{self.name}"


class Token:
    def __init__(self, *, file: Path, content_range: FileRangeProtocol) -> None:
        self._content_range = content_range
        self._file = file

    @property
    def file(self) -> Path:
        """The file path."""
        return self._file
    
    @property
    def content_range(self) -> FileRangeProtocol:
        """The content range within the file."""
        return self._content_range

    @property
    def source(self) -> str:
        """The source code."""
        data: bytes
        with open(self.file, "rb") as file:
            i = 0
            start: int = 0
            end: int = 0
            with mmap(file.fileno(), 0, access=ACCESS_READ) as content:
                while True:
                    if i == self.content_range.start.line:
                        start = content.tell() + self.content_range.start.char
                    if i == self.content_range.end.line:
                        end = content.tell() + self.content_range.end.char
                        data = content[start:end]
                        break
                    content.readline()
                    i += 1
        return data.decode("utf-8")


class NamedToken(Token):
    def __init__(self, *, file: Path, content_range: FileRangeProtocol, name:str) -> None:
        super().__init__(file=file, content_range=content_range)
        self._name = name

    @property
    def name(self) -> str:
        """The name of the token."""
        return self._name