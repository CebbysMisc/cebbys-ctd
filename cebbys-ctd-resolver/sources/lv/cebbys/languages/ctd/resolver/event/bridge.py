from lv.cebbys.languages.ctd.resolver.event.listener import (
    CtdEventListener
)
# from lv.cebbys.languages.ctd.types.ctd import (
#     Typedef,
#     Alias,
# )
from typing import (
    Callable
)
from uuid import (
    uuid4,
    UUID
)
# class DefaultListener(CtdEventListener):
#     def handle_construct_typedef(self, value: Typedef):
#         print(f"Emitted typedef construction '{value}'")
#     def handle_construct_alias(self, value: Alias):
#         print(f"Emitted alias construction '{value}'")


class CtdEventBridge:
    LISTENERS: dict[UUID, CtdEventListener] = {}
    FIELD: UUID = uuid4()

    @staticmethod
    def emit(consumer: Callable[[CtdEventListener], None]):
        for listener in CtdEventBridge.LISTENERS.values():
            consumer(listener)

    @staticmethod
    def register(listener: CtdEventListener):
        if listener in CtdEventBridge.LISTENERS.values() or CtdEventBridge._is_marked(listener):
            raise BaseException(f"Event listener already registered")
        CtdEventBridge._mark(listener)
        uuid = uuid4()
        CtdEventBridge.LISTENERS[uuid] = listener
        return uuid

    @staticmethod
    def _is_marked(listener: CtdEventListener):
        return getattr(listener, str(CtdEventBridge.FIELD), False)

    @staticmethod
    def _mark(listener: CtdEventListener):
        setattr(listener, str(CtdEventBridge.FIELD), True)

# CtdEventBridge.register(DefaultListener())
