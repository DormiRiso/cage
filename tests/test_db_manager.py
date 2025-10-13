import os
import sqlite3
from cage import db_manager
import pytest

TEST_DB_PATH = "database/test_cage.db"

def setup_module(module):
    # Elimina il database di test se esiste già
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def teardown_module(module):
    # Pulisci il database di test dopo i test
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def test_connect_to_database():
    con = db_manager.connect_to_database(TEST_DB_PATH)
    assert isinstance(con, sqlite3.Connection)
    con.close()

def test_init_db():
    con = db_manager.connect_to_database(TEST_DB_PATH)
    db_manager.init_db(TEST_DB_PATH)  # Inizializza il DB
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='crag';")
    table = cur.fetchone()
    assert table is not None
    con.close()

def test_insert_and_get_crag():
    con = db_manager.connect_to_database(TEST_DB_PATH)
    db_manager.init_db(TEST_DB_PATH)  # Inizializza il DB
    db_manager.insert_new_crag("TestCrag", 45.0, 7.0, TEST_DB_PATH)
    coords = db_manager.get_coordinates_from_crag_name("TestCrag", TEST_DB_PATH)
    assert coords == (45.0, 7.0)
    con.close()

def test_get_coordinates_nonexistent_crag():
    con = db_manager.connect_to_database(TEST_DB_PATH)
    db_manager.init_db(TEST_DB_PATH)  # Inizializza il DB
    coords = db_manager.get_coordinates_from_crag_name("NonExistentCrag", TEST_DB_PATH)
    assert coords is None
    con.close()
