from lv.cebbys.languages.ctd.utility.logging import (
    get_logger,
)
from ghidra.program.model.data import (  # type: ignore
    DataTypeConflictHandler,
    DataTypeManager,
    DataTypePath,
    DataType,
)


logger = get_logger(__name__)


class GhidraConnector:
    @staticmethod
    def update(manager: DataTypeManager, ghidra_uuid: int, declaration: DataType) -> None:
        existing = GhidraConnector.get(manager, ghidra_uuid)
        if not existing:
            raise ValueError(f"Cannot update datatype, no datatype with uuid {ghidra_uuid} found")
        manager.replaceDataType(existing, declaration, False)

    @staticmethod
    def create(manager: DataTypeManager, declaration: DataType) -> int:
        existing = GhidraConnector.get(manager, declaration.getDataTypePath())
        if existing:
            manager.replaceDataType(existing, declaration, True)
        added = manager.addDataType(declaration, replace_handler())
        return manager.getID(added)

    @staticmethod
    def get(manager: DataTypeManager, id: int | DataTypePath) -> DataType | None:
        return manager.getDataType(id)  # type: ignore


def replace_handler() -> DataTypeConflictHandler:
    return DataTypeConflictHandler.REPLACE_HANDLER  # type: ignore
