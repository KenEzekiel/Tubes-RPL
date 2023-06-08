import sqlite3
import os
import sys


def connect_db():
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    current_dir = os.path.dirname(__file__)
    if "pytest" in sys.modules:
        filename = "test_db.sqlite3"
    else:
        filename = "db.sqlite3"
    db_file = os.path.join(current_dir, filename)
    created = os.path.exists(db_file)
    connection = sqlite3.connect(db_file, check_same_thread=False)
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    if not created:
        with open(os.path.join(current_dir, 'schema.sql'), 'r') as f:
            sql_script = f.read()
            print("Creating database...")
            cursor.executescript(sql_script)
    print("Database connected")
    return connection, cursor


def clear_db():
    tables = ["Hewan", "RiwayatHewan", "Makanan", "JenisMakanan"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")
    commit()


def commit():
    connection.commit()


connection, cursor = connect_db()
