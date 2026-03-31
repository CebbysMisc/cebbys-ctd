from lv.cebbys.languages.ctd.types.meta import (
    DecoratorMeta,
)
from typing import (
    runtime_checkable,
    Protocol,
    Any,
)


class Decorator:
    def __init__(self, meta: "DecoratorMeta") -> None:
        self._meta = meta
        arguments: list[Any] = []
        for argument in self.meta.arguments:
            value: Any = argument
            if is_bool(argument):
                value = argument == "true"  # Convert boolean literals to bool
            if is_float(argument):
                value = float(argument)  # Convert numeric literals to floats
            elif argument.isdigit():
                value = int(argument)  # Convert numeric literals to integers
            arguments.append(value)
        self._arguments = tuple(arguments)

    @property
    def name(self) -> str:
        return self.meta.name

    @property
    def arguments(self) -> tuple[Any, ...]:
        return self._arguments

    @property
    def meta(self) -> "DecoratorMeta":
        return self._meta


@runtime_checkable
class SupportsDecorators(Protocol):
    @property
    def decorators(self) -> tuple[Decorator, ...]: ...


def is_float(value: Any) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_bool(value: Any) -> bool:
    return value in {"true", "false"}
