from lv.cebbys.languages.ctd.resolver.event.listener import (
    CtdEventListener
)
from lv.cebbys.languages.ctd.resolver.event.bridge import (
    CtdEventBridge
)
from lv.cebbys.languages.ctd.types.ctd import (
    Declaration
)
from typing import (
    Callable,
    Generic,
    TypeVar,
    Any,
)

T = TypeVar("T", bound=Declaration, contravariant=True)

class Event(Generic[T]):
    @classmethod
    def emit(cls, value: T):
        CtdEventBridge.emit(lambda listener: cls._get_consumer(listener)(value))

    @staticmethod
    def _get_consumer(listener: CtdEventListener) -> Callable[[T], None]: ...
    
def create_construct_event[D](callback: Callable[[CtdEventListener], Callable[[D], None]]) -> type[Event[D]]: # type: ignore
    class CtdConstructEvent(Event[Any]):
        @staticmethod
        def _get_consumer(listener: CtdEventListener) -> Callable[[Any], None]:
            return callback(listener)
    return CtdConstructEvent

CtdInterfaceConstructEvent = create_construct_event(lambda l: l.handle_construct_interface)
CtdStructureConstructEvent = create_construct_event(lambda l: l.handle_construct_structure)
CtdFunctionConstructEvent = create_construct_event(lambda l: l.handle_construct_function)
CtdTypedefConstructEvent = create_construct_event(lambda l: l.handle_construct_typedef)
CtdAliasConstructEvent = create_construct_event(lambda l: l.handle_construct_alias)
CtdEnumConstructEvent = create_construct_event(lambda l: l.handle_construct_enum)
CtdFlagConstructEvent = create_construct_event(lambda l: l.handle_construct_flag)