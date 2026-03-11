# from lv.cebbys.languages.ctd.types.exception import (
#     CtdException
# )
# from typing import (
#     Callable
# )

# class Reference[T]:
#     def __init__(self, registry: "Registry[T]", key: "str") -> None:
#         self._registry = registry
#         self._key = key

#     @property
#     def key(self):
#         return self._key

#     @property
#     def value(self):
#         return self._registry.item(self)

# class Registry[T]:
#     def __init__(self) -> None:
#         self._data: dict[str, T] = {}

#     def register(self, key: str, value: T) -> Reference[T]:
#         try:
#             if key in self._data:
#                 raise CtdException(f"Item '{key}' already exists with value '{value}'")
#             self._data[key] = value
#         except BaseException as e:
#             raise CtdException(f"Failed to register item '{key}' with value '{value}'") from e

#         return Reference(self, key)

#     def item(self, reference: Reference[T]) -> T:
#         return self._data[reference.key]