import os
from cage import db_manager

TEST_DB_PATH = "database/test_cage.db"

def setup_module(module):
    """Setup a fresh database for testing."""
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def teardown_module(module):
    """Teardown the database after testing."""
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def test_init_db():
    """Test database initialization."""
    assert db_manager.init_db(TEST_DB_PATH) == True
    with db_manager.get_db_connection(TEST_DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='crag'")
        assert cur.fetchone() is not None
    
def test_insert_new_crag():
    """Test inserting new crags."""
    db_manager.init_db(TEST_DB_PATH)
    assert db_manager.insert_new_crag("TestCrag", 45.0, 7.0, TEST_DB_PATH) == True
    assert db_manager.insert_new_crag("TestCrag", 45.0, 7.0, TEST_DB_PATH) == False
    assert db_manager.insert_new_crag("", 45.0, 7.0, TEST_DB_PATH) == False
    assert db_manager.insert_new_crag("AnotherCrag", None, 7.0, TEST_DB_PATH) == False
    assert db_manager.insert_new_crag("AnotherCrag", 45.0, None, TEST_DB_PATH) == False
    teardown_module(None)
    setup_module(None)

def test_get_coordinates_from_crag_name():
    """Test retrieving coordinates by crag name."""
    db_manager.init_db(TEST_DB_PATH)
    db_manager.insert_new_crag("TestCrag", 45.0, 7.0, TEST_DB_PATH)
    coords = db_manager.get_coordinates_from_crag_name("TestCrag", TEST_DB_PATH)
    assert coords == (45.0, 7.0)
    assert db_manager.get_coordinates_from_crag_name("NonExistentCrag", TEST_DB_PATH) is None
    assert db_manager.get_coordinates_from_crag_name("", TEST_DB_PATH) is None
    teardown_module(None)
    setup_module(None)

def test_list_all_crags():
    """Test listing all crags."""
    db_manager.init_db(TEST_DB_PATH)
    db_manager.insert_new_crag("Crag1", 45.0, 7.0, TEST_DB_PATH)
    db_manager.insert_new_crag("Crag2", 46.0, 8.0, TEST_DB_PATH)
    crags = db_manager.list_all_crags(TEST_DB_PATH)
    print(crags)
    assert len(crags) == 2
    names = {crag.name for crag in crags}
    assert "Crag1" in names
    assert "Crag2" in names
    teardown_module(None)
    setup_module(None)
