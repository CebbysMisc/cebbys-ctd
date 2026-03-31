"""
Tests for CursorExecute utility class.

Covers:
- insert: writing rows into an in-memory SQLite database
- select (mode="one"): single-row retrieval without filters
- select (mode="all"): multi-row retrieval without filters
- select with instance-attribute filters (non-None fields become WHERE conditions)
- select with explicit **filters kwarg
- select where explicit **filters override instance-attribute values
- select returning None when no row matches
"""

import importlib.util
import sqlite3
import unittest
from pathlib import Path
from typing import Optional
from uuid import UUID as Uuid

# Load __utility__ directly to avoid triggering the Ghidra/pyghidra __init__.py
_util_path = (
    Path(__file__).parent.parent
    / "sources/lv/cebbys/languages/ctd/ghidra/datatype/storage/connector/sqlite/__utility__.py"
)
_spec = importlib.util.spec_from_file_location("__utility__", _util_path)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
CursorExecute = _mod.CursorExecute


# ---------------------------------------------------------------------------
# Sample model
# ---------------------------------------------------------------------------

class Widget(CursorExecute):
    id: Optional[int] = CursorExecute.primary_key()
    typeUuid: Optional[str] = None
    name: Optional[str] = None


def _create_table(conn: sqlite3.Connection) -> None:
    Widget.table(conn.cursor())
    conn.commit()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestCursorExecuteInsert(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        _create_table(self.conn)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_insert_single_row(self):
        Widget.insert(self.cursor, Widget(id=1, typeUuid="uuid-a", name="Alpha"))
        self.conn.commit()

        self.cursor.execute("SELECT id, typeUuid, name FROM Widget")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], (1, "uuid-a", "Alpha"))

    def test_insert_multiple_rows(self):
        Widget.insert(self.cursor, Widget(id=1, typeUuid="uuid-a", name="Alpha"))
        Widget.insert(self.cursor, Widget(id=2, typeUuid="uuid-b", name="Beta"))
        self.conn.commit()

        self.cursor.execute("SELECT COUNT(*) FROM Widget")
        self.assertEqual(self.cursor.fetchone()[0], 2)

    def test_insert_raises_on_none_primary_key(self):
        with self.assertRaises(ValueError) as ctx:
            Widget.insert(self.cursor, Widget(id=None, typeUuid="uuid-x", name="X"))
        self.assertIn("id", str(ctx.exception))
        self.assertIn("primary key", str(ctx.exception))

    def test_insert_raises_on_none_required_field(self):
        class Strict(CursorExecute):
            id: int = CursorExecute.primary_key(default=0)
            code: str = "default"
            label: Optional[str] = None

        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        Strict.table(cursor)
        conn.commit()

        with self.assertRaises(ValueError) as ctx:
            Strict.insert(cursor, Strict(id=1, code=None, label="ok"))  # type: ignore[arg-type]
        self.assertIn("code", str(ctx.exception))
        self.assertIn("not optional", str(ctx.exception))
        conn.close()


class TestCursorExecuteSelectOne(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        _create_table(self.conn)
        self.cursor = self.conn.cursor()
        Widget.insert(self.cursor, Widget(id=1, typeUuid="uuid-a", name="Alpha"))
        Widget.insert(self.cursor, Widget(id=2, typeUuid="uuid-b", name="Beta"))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_select_one_no_filter_returns_first_row(self):
        result = Widget.select(self.cursor, mode="one")
        self.assertIsInstance(result, Widget)

    def test_select_one_with_instance_filter(self):
        result = Widget.select(self.cursor, Widget(typeUuid="uuid-b"), mode="one")
        self.assertIsNotNone(result)
        self.assertEqual(result.typeUuid, "uuid-b")
        self.assertEqual(result.name, "Beta")

    def test_select_one_no_match_returns_none(self):
        result = Widget.select(self.cursor, Widget(typeUuid="does-not-exist"), mode="one")
        self.assertIsNone(result)

    def test_select_one_by_id(self):
        result = Widget.select(self.cursor, Widget(id=1), mode="one")
        self.assertIsNotNone(result)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, "Alpha")


class TestCursorExecuteSelectAll(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        _create_table(self.conn)
        self.cursor = self.conn.cursor()
        Widget.insert(self.cursor, Widget(id=1, typeUuid="uuid-shared", name="Alpha"))
        Widget.insert(self.cursor, Widget(id=2, typeUuid="uuid-shared", name="Beta"))
        Widget.insert(self.cursor, Widget(id=3, typeUuid="uuid-unique", name="Gamma"))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_select_all_no_filter_returns_all(self):
        results = Widget.select(self.cursor)
        self.assertEqual(len(results), 3)

    def test_select_all_instance_filter_typeUuid(self):
        results = Widget.select(self.cursor, Widget(typeUuid="uuid-shared"))
        self.assertEqual(len(results), 2)
        self.assertTrue(all(w.typeUuid == "uuid-shared" for w in results))

    def test_select_all_instance_filter_unique(self):
        results = Widget.select(self.cursor, Widget(typeUuid="uuid-unique"))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Gamma")

    def test_select_all_instance_filter_by_name(self):
        results = Widget.select(self.cursor, Widget(name="Beta"))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 2)

    def test_select_all_instance_multi_field_filter(self):
        results = Widget.select(self.cursor, Widget(typeUuid="uuid-shared", name="Alpha"))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Alpha")

    def test_select_all_no_match_returns_empty_list(self):
        results = Widget.select(self.cursor, Widget(typeUuid="not-there"))
        self.assertEqual(results, [])


class TestCursorExecuteHelpers(unittest.TestCase):
    def test_get_table_name(self):
        self.assertEqual(Widget.get_table_name(), "Widget")

    def test_get_fields(self):
        self.assertEqual(Widget.get_fields(), ["id", "typeUuid", "name"])

    def test_subclass_is_dataclass(self):
        import dataclasses
        self.assertTrue(dataclasses.is_dataclass(Widget))

    def test_get_primary_key_fields(self):
        self.assertEqual(Widget.get_primary_key_fields(), ["id"])

    def test_primary_key_returns_field_descriptor(self):
        import dataclasses
        f = CursorExecute.primary_key()
        self.assertIsInstance(f, dataclasses.Field)
        self.assertIsNone(f.default)
        self.assertTrue(f.metadata.get("primary_key"))

    def test_get_primary_key_fields_no_pk(self):
        class NoPk(CursorExecute):
            name: Optional[str] = None
        self.assertEqual(NoPk.get_primary_key_fields(), [])


class TestCursorExecuteTable(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_table_creates_table(self):
        Widget.table(self.cursor)
        self.conn.commit()
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='Widget'"
        )
        self.assertIsNotNone(self.cursor.fetchone())

    def test_table_idempotent(self):
        # Calling table() twice must not raise
        Widget.table(self.cursor)
        Widget.table(self.cursor)
        self.conn.commit()

    def test_table_correct_columns(self):
        Widget.table(self.cursor)
        self.conn.commit()
        self.cursor.execute("PRAGMA table_info(Widget)")
        cols = {row[1]: row[2] for row in self.cursor.fetchall()}
        self.assertEqual(cols, {"id": "INTEGER", "typeUuid": "TEXT", "name": "TEXT"})

    def test_table_primary_key_constraint(self):
        Widget.table(self.cursor)
        self.conn.commit()
        self.cursor.execute("PRAGMA table_info(Widget)")
        # pk column in PRAGMA table_info is non-zero for primary key columns
        pk_cols = [row[1] for row in self.cursor.fetchall() if row[5] != 0]
        self.assertEqual(pk_cols, ["id"])

    def test_table_allows_insert(self):
        Widget.table(self.cursor)
        Widget.insert(self.cursor, Widget(id=1, typeUuid="u1", name="Test"))
        self.conn.commit()
        self.cursor.execute("SELECT COUNT(*) FROM Widget")
        self.assertEqual(self.cursor.fetchone()[0], 1)


class Record(CursorExecute):
    rowId: Optional[int] = None
    uid: Optional[Uuid] = None
    label: Optional[str] = None


class TestCursorExecuteUuid(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        Record.table(self.cursor)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_table_uuid_column_type(self):
        self.cursor.execute("PRAGMA table_info(Record)")
        cols = {row[1]: row[2] for row in self.cursor.fetchall()}
        self.assertEqual(cols["uid"], "UUID")

    def test_insert_and_select_uuid_round_trip(self):
        uid = Uuid("12345678-1234-5678-1234-567812345678")
        Record.insert(self.cursor, Record(rowId=1, uid=uid, label="hello"))
        self.conn.commit()

        result = Record.select(self.cursor, Record(uid=uid), mode="one")
        self.assertIsNotNone(result)
        self.assertEqual(result.uid, uid)
        self.assertEqual(result.label, "hello")

    def test_select_by_uuid_filter(self):
        uid_a = Uuid("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
        uid_b = Uuid("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
        Record.insert(self.cursor, Record(rowId=1, uid=uid_a, label="A"))
        Record.insert(self.cursor, Record(rowId=2, uid=uid_b, label="B"))
        self.conn.commit()

        results = Record.select(self.cursor, Record(uid=uid_a))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].label, "A")


if __name__ == "__main__":
    unittest.main()
