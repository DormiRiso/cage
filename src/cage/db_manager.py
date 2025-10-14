import sqlite3
from contextlib import contextmanager
from cage.my_types import Crag

def connect_to_database(db_name="database/cage.db"):
    """Connect to the SQLite database specified by db_name.
    Returns the connection object or None if connection fails.
    """
    if db_name is None:
        raise ValueError("Database name cannot be None")
    try:
        con = sqlite3.connect(db_name)
        return con
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

@contextmanager
def get_db_connection(db_name="database/cage.db"):
    """Context manager for database connections."""
    con = connect_to_database(db_name)
    if con is None:
        raise sqlite3.Error("Failed to connect to database")
    try:
        yield con
    finally:
        con.close()

def init_db(db_name="database/cage.db"):
    """Initialize the database with the required tables.
    Returns True if successful, False otherwise.
    """
    try:
        with get_db_connection(db_name) as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS crag(name TEXT PRIMARY KEY, lat REAL, lon REAL)")
            con.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        return False

def get_coordinates_from_crag_name(crag_name, db_name="database/cage.db"):
    """Retrieve the latitude and longitude of a crag given its name.
    Returns a tuple (lat, lon) or None if the crag is not found.
    """
    if not crag_name:
        return None

    try:
        with get_db_connection(db_name) as con:
            cur = con.cursor()
            res = cur.execute("SELECT lat, lon FROM crag WHERE name = ?", (crag_name,))
            coordinates = res.fetchone()
            return coordinates
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return None

def insert_new_crag(crag_name: str, lat: float, lon: float, db_name="database/cage.db"):
    """Insert a new crag into the database.
    Returns True if insertion is successful, False otherwise.
    """
    if not crag_name or lat is None or lon is None:
        return False

    try:
        with get_db_connection(db_name) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO crag (name, lat, lon) VALUES (?, ?, ?)", (crag_name, lat, lon))
            con.commit()
            return True
    except sqlite3.IntegrityError:
        # Crag already exists (PRIMARY KEY constraint)
        print(f"Crag '{crag_name}' already exists")
        return False
    except sqlite3.Error as e:
        print(f"Database insert error: {e}")
        return False
   
def list_all_crags(db_name="database/cage.db"):
    """Retrieve a list of all crags in the database.
    Returns a list of Crag objects.
    """
    try:
        with get_db_connection(db_name) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM crag")
            rows = cur.fetchall()
            crags = [Crag(name=row[0], lat=row[1], lon=row[2]) for row in rows]
            return crags
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return []
