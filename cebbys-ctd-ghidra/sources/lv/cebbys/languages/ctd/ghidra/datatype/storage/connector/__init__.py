
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
    Declaration,
    Builtin,
    Pointer,
    Alias,
    Array,
)
from lv.cebbys.languages.ctd.utility import (
    get_logger,
)
from ghidra.program.model.listing import (  # type: ignore
    Program,
)
from ghidra.program.model.data import (  # type: ignore
    DataType,
    DataTypeManager,
)
from pyghidra import (
    transaction,
)
from pathlib import (
    Path,
)
from sqlite3 import (
    Connection,
    PARSE_DECLTYPES,
    Cursor,
)
from uuid import (
    UUID as Uuid,
)

logger = get_logger(__name__)


class DatatypeConnector:
    def __init__(self, database_path: Path) -> None:
        self._connection = Connection(str(database_path), detect_types=PARSE_DECLTYPES)
        self._cursor = self._connection.cursor()
        CtdTypeMapping.table(self._cursor)
        self._connection.commit()

    def synchronize(self, program: Program, declarations: list[Declaration]) -> bool:
        modified = [
            declaration
            for declaration in declarations
            if is_modified(self._cursor, declaration)
        ]
        if not modified:
            return False
        uuids = [get_type_uuid(declaration) for declaration in modified]
        if len(uuids) != len(set(uuids)):
            raise ValueError("Duplicate type UUIDs found in modified declarations")

        resolved = resolve(modified)

        existing = set(filter(self.is_existing, resolved))
        new = resolved - existing

        try:
            with transaction(program, "CTD datatype synchronization"):
                manager = program.getDataTypeManager()
                self.create_datatypes(manager, new)
                self.update_datatypes(manager, existing)
                self._connection.commit()
        except Exception as e:
            self._connection.rollback()
            logger.error(f"Error during synchronization: {e}", exc_info=True)
            return False
        return True

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
                type_uuid=type_uuid, type_path=declaration.typeref, ghidra_uuid=ghidra_uuid, sha256=declaration.sha256()
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
            CtdTypeMapping.insert(self._cursor, CtdTypeMapping(
                type_uuid=type_uuid, type_path=declaration.typeref, ghidra_uuid=mapping.ghidra_uuid, sha256=declaration.sha256()
            ))

    def close(self) -> None:
        self._connection.close()


def is_modified(cursor: Cursor, declaration: Declaration) -> bool:
    if isinstance(declaration, (Builtin, Pointer, Alias, Array)):
        return False

    mapping = CtdTypeMapping.select(
        cursor,
        CtdTypeMapping(type_uuid=get_type_uuid(declaration)),
        mode="one",
    )
    if mapping is None:
        return True

    sha256 = mapping.sha256
    return sha256 != declaration.sha256()


def resolve(declarations: list[Declaration]) -> set[tuple[Declaration, DataType]]:
    return {
        (declaration, DatatypeResolver.resolve(declaration))
        for declaration in declarations
    }


def get_type_uuid(declaration: Declaration) -> Uuid:
    if isinstance(declaration, Builtin):
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
