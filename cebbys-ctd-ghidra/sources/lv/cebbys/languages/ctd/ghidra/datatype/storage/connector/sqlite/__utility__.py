import dataclasses
import types
from sqlite3 import (
    Cursor,
    register_adapter,
    register_converter,
)
from typing import (
    get_type_hints,
    get_origin,
    get_args,
    overload,
    Literal,
    Self,
    Any,
    Union,
)
from dataclasses import (
    field,
)
from uuid import UUID as Uuid

register_adapter(Uuid, lambda u: u.bytes)
register_converter("UUID", lambda b: Uuid(bytes=b))

PY_TO_SQL: dict[type, str] = {
    int: "INTEGER",
    float: "REAL",
    bytes: "BLOB",
    str: "TEXT",
    Uuid: "UUID",
}


class CursorExecute:
    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        dataclasses.dataclass(cls)

    @classmethod
    def table(cls, cursor: Cursor) -> None:
        """Create the table if it does not already exist."""
        hints = get_type_hints(cls)
        pk_fields = set(cls.get_primary_key_fields())
        column_defs: list[Any] = []
        for field_name, hint in hints.items():
            sql_type = cls.resolve_sql_type(hint)
            pk_suffix = " PRIMARY KEY" if field_name in pk_fields else ""
            column_defs.append(f"{field_name} {sql_type}{pk_suffix}")
        columns = ", ".join(column_defs)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {cls.get_table_name()} ({columns})")

    @classmethod
    def insert(cls, cursor: Cursor, instance: Self) -> None:
        table = cls.get_table_name()
        fields = cls.get_fields()
        hints = get_type_hints(cls)

        for pk in cls.get_primary_key_fields():
            if getattr(instance, pk) is None:
                raise ValueError(f"{cls.__name__}.{pk} is a primary key and must not be None")

        for field_name, hint in hints.items():
            if not cls._is_optional(hint) and getattr(instance, field_name) is None:
                raise ValueError(
                    f"{cls.__name__}.{field_name} is not optional and must not be None")

        # Build query: INSERT INTO Table (col1, col2) VALUES (?, ?)
        placeholders = ", ".join(["?"] * len(fields))
        columns = ", ".join(fields)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        values = tuple(getattr(instance, f) for f in fields)
        cursor.execute(query, values)

    @overload
    @classmethod
    def select(  # type: ignore[override]
        cls,
        cursor: Cursor,
        instance: Self | None = None,
        *,
        mode: Literal["one"],
    ) -> Self | None: ...

    @overload
    @classmethod
    def select(  # type: ignore[override]
        cls,
        cursor: Cursor,
        instance: Self | None = None,
        *,
        mode: Literal["all"] = "all",
    ) -> list[Self]: ...

    @classmethod
    def select(cls, cursor: Cursor, instance: Self | None = None, *, mode: Literal["one", "all"] = "all") -> Any:
        table = cls.get_table_name()
        fields = cls.get_fields()
        columns = ", ".join(fields)

        query = f"SELECT {columns} FROM {table}"
        values: tuple[Any, ...] = ()

        if instance is not None:
            instance_filters = {f: getattr(instance, f)
                                for f in fields if getattr(instance, f) is not None}
            if instance_filters:
                conditions = " AND ".join([f"{k} = ?" for k in instance_filters.keys()])
                query += f" WHERE {conditions}"
                values = tuple(instance_filters.values())

        cursor.execute(query, values)

        if mode == "one":
            row = cursor.fetchone()
            return cls(**dict(zip(fields, row))) if row else None
        else:
            rows = cursor.fetchall()
            return [cls(**dict(zip(fields, r))) for r in rows]

    @staticmethod
    def _is_optional(hint: Any) -> bool:
        """Return True if the hint allows None (e.g. Optional[X] or X | None)."""
        origin = get_origin(hint)
        if origin is Union or origin is types.UnionType:
            return type(None) in get_args(hint)
        return False

    @classmethod
    def resolve_sql_type(cls, hint: Any) -> str:
        """Map a Python type annotation to a SQLite column type."""
        origin = get_origin(hint)
        # Handle Optional[X]  (Union[X, None])
        if origin is Union or origin is types.UnionType:
            inner = [a for a in get_args(hint) if a is not type(None)]
            if inner:
                return cls.resolve_sql_type(inner[0])
        return PY_TO_SQL.get(hint, "TEXT")

    @classmethod
    def get_primary_key_fields(cls) -> list[str]:
        """Return field names marked as primary keys."""
        if not dataclasses.is_dataclass(cls):
            return []
        return [
            f.name
            for f in dataclasses.fields(cls)
            if f.metadata.get("primary_key") is True
        ]

    @staticmethod
    def primary_key(default: Any = None) -> Any:
        """Return a dataclass field descriptor marked as a primary key."""
        return field(default=default, metadata={"primary_key": True})

    @classmethod
    def get_table_name(cls):
        return cls.__name__

    @classmethod
    def get_fields(cls):
        # Returns a list of field names based on type hints
        return list(get_type_hints(cls).keys())
