from lv.cebbys.languages.ctd.type.token.__api__ import (
    FileRangeProtocol,
    ReferableProtocol,
    NamedToken,
    FileCursor,
    FileRange,
)
from pathlib import (
    Path,
)
from typing import (
    Iterable,
)

class ModuleToken(NamedToken):
    def __init__(
        self, *,
        file: Path,
        root: Path
    ) -> None:
        super().__init__(
            file=file,
            content_range=FileRange(start=FileCursor.start(file), end=FileCursor.end(file)),
            name=file.relative_to(root).with_suffix('').as_posix()
        )
        self._root = root

    @property
    def root(self) -> Path:
        """The root path of the module.
        
        Root path is the base path where modules are looked up from.
        Every module path will be child of the root path.
        Module name is automatically derived from the root and module path.
        """
        return self._root

class DecoratorToken(NamedToken):
    def __init__(self, *, file: Path, content_range: FileRangeProtocol, name:str, arguments: Iterable[str]) -> None:
        super().__init__(file=file, content_range=content_range, name=name)
        self._arguments = tuple(arguments)

    @property
    def name(self) -> str:
        """The name of the decorator.

        Example - `@{name}`:
        * `@TypeId("uuid235162")` → `TypeId`
        * `@Injectable` → `Injectable`
        * `@Component` → `Component`
        """
        return super().name
    
    @property
    def arguments(self) -> tuple[str, ...]:
        """The arguments of the decorator.

        Example - `@{name}({arguments})`:
        * `@Storage("register", 0x0, 0x4)` → `["\"register\"", "0x0", "0x4"]`
        * `@TypeId("uuid235162")` → `["\"uuid235162\""]`
        """
        return self._arguments
    
class NamespaceToken(NamedToken):
    def __init__(self, *, file: Path, content_range: FileRangeProtocol, name: str) -> None:
        super().__init__(file=file, content_range=content_range, name=name)
    
class ReferableToken(NamedToken):
    def __init__(self, *, file: Path, content_range: FileRangeProtocol, path:str, name:str) -> None:
        super().__init__(file=file, content_range=content_range, name=name)
        self._path = path

    @property
    def path(self) -> str:
        """The path of the token.
        * `example::element::path::value`
        """
        return self._path
    
    @property
    def pathname(self) -> str:
        """The path and name of the token.
        
        Example:
        * path: `example::element::path`
        * name: `value`
        * pathname: `example::element::path::value`
        """
        return f"{self.path}::{self.name}"
    
    

class DeclarationToken(ReferableToken):
    def __init__(
        self, *,
        file: Path,
        content_range: FileRangeProtocol,
        path: str,
        name: str,
        decorators: Iterable[DecoratorToken] = [],
    ) -> None:
        super().__init__(file=file, content_range=content_range, path=path, name=name)
        self._decorators = tuple(decorators)

    @property
    def decorators(self) -> tuple[DecoratorToken, ...]:
        """The decorators applied to the declaration."""
        return self._decorators

class TypedefToken(DeclarationToken):
    def __init__(
        self, *,
        base_reference: ReferableProtocol,
        content_range: FileRangeProtocol,
        decorators: Iterable[DecoratorToken] = [],
        signed: bool|None,
        file: Path,
        name: str,
        path: str,
    ) -> None:
        super().__init__(file=file, content_range=content_range, path=path, name=name, decorators=decorators)
        self._base_ref = base_reference
        self._signed = signed

    @property
    def base_reference(self) -> ReferableProtocol:
        """The reference to the base type."""
        return self._base_ref
    
    @property
    def signed(self) -> bool|None:
        """Whether the type is signed or unsigned. `None` if not specified."""
        return self._signed

def get() -> TypedefToken:
    """Get the metadata of the decorator at the current cursor position."""
    ...

t = get()