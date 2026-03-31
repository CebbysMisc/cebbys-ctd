from lv.cebbys.languages.ctd.ghidra.datatype.storage.connector.ghidra import (
    GhidraConnector,
)
from lv.cebbys.languages.ctd.ghidra.datatype.storage.connector.sqlite import (
    CtdTypeMapping,
)
from lv.cebbys.languages.ctd.ghidra.datatype.resolver import (
    DatatypeResolver,
)
from lv.cebbys.languages.ctd.types.ctd import (
    SupportsDecorators,
    Declaration,
)
from ghidra.program.model.listing import (  # type: ignore
    Program,
)
from ghidra.program.model.data import (  # type: ignore
    DataType,
    DataTypeManager,
)
from sqlite3 import (
    Connection,
    PARSE_DECLTYPES,
)
from pyghidra import (
    transaction,
)
from pathlib import (
    Path,
)
from uuid import (
    UUID as Uuid,
)


class DatatypeConnector:
    def __init__(self, database_path: Path) -> None:
        self._connection = Connection(str(database_path), detect_types=PARSE_DECLTYPES)
        self._cursor = self._connection.cursor()
        CtdTypeMapping.table(self._cursor)
        self._connection.commit()

    def synchronize(self, program: Program, declarations: list[Declaration]) -> None:
        modified = [declaration for declaration in declarations if is_modified(declaration)]
        if not modified:
            return
        resolved = resolve(modified)

        existing = set(filter(self.is_existing, resolved))
        new = resolved - existing

        try:
            with transaction(program, "CTD datatype synchronization"):
                manager = program.getDataTypeManager()
                self.create_datatypes(manager, new)
                self.update_datatypes(manager, existing)
            self._connection.commit()
        except Exception:
            self._connection.rollback()
            raise

    def is_existing(self, entry: tuple[Declaration, DataType]) -> bool:
        declaration, _ = entry
        type_uuid = get_type_uuid(declaration)
        result = CtdTypeMapping.select(
            self._cursor,
            CtdTypeMapping(type_uuid=type_uuid),
            mode="one",
        )
        return result is not None and result.ghidra_uuid is not None

    def create_datatypes(
        self,
        manager: DataTypeManager,
        items: set[tuple[Declaration, DataType]],
    ) -> None:
        for declaration, datatype in items:
            ghidra_uuid = GhidraConnector.create(manager, datatype)
            type_uuid = get_type_uuid(declaration)
            CtdTypeMapping.insert(self._cursor, CtdTypeMapping(
                type_uuid=type_uuid, ghidra_uuid=ghidra_uuid
            ))

    def update_datatypes(
        self,
        manager: DataTypeManager,
        items: set[tuple[Declaration, DataType]],
    ) -> None:
        for declaration, datatype in items:
            type_uuid = get_type_uuid(declaration)
            mapping = CtdTypeMapping.select(
                self._cursor,
                CtdTypeMapping(type_uuid=type_uuid),
                mode="one",
            )
            if mapping is None or mapping.ghidra_uuid is None:
                raise ValueError(
                    f"Expected existing CtdTypeMapping for type_uuid {type_uuid}, but ghidra_uuid is missing"
                )
            GhidraConnector.update(manager, mapping.ghidra_uuid, datatype)

    def close(self) -> None:
        self._connection.close()


# TODO As of now keep the declarations always modified because caching in the sqlite connector is not implemented yet
def is_modified(declaration: Declaration) -> bool:
    if not isinstance(declaration, SupportsDecorators):
        return False
    
    
    return True


def resolve(declarations: list[Declaration]) -> set[tuple[Declaration, DataType]]:
    return {
        (declaration, DatatypeResolver.resolve(declaration))
        for declaration in declarations
    }


def get_type_uuid(declaration: Declaration) -> Uuid:
    if not isinstance(declaration, SupportsDecorators):
        raise ValueError(f"Declaration {declaration} does not support decorators")
    decorators = declaration.decorators
    if not decorators:
        raise ValueError(f"Declaration {declaration} does not have any decorators")

    for decorator in decorators:
        if decorator.name == "TypeId":
            arguments = decorator.arguments
            if not arguments:
                raise ValueError(f"Decorator @{decorator.name} does not have any arguments")
            argument = arguments[0]
            if not isinstance(argument, str):
                raise ValueError(
                    f"Decorator @{decorator.name} argument {argument} is not a uuid string"
                )
            return Uuid(argument)
    raise ValueError(f"Declaration {declaration} does not have a @TypeId decorator")
