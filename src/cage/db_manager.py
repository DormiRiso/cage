import sqlite3

def connect_to_database(db_name="database/cage.db"):
    ''' Connect to the SQLite database specified by db_name. '''
    con = sqlite3.connect(db_name)
    return con

def init_db(db_name="database/cage.db"):
    ''' Initialize the database with the required tables. '''
    con = connect_to_database(db_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS crag(name TEXT PRIMARY KEY, lat REAL, lon REAL)")
    con.commit()
    con.close()

def get_coordinates_from_crag_name(crag_name, db_name="database/cage.db"):
    ''' Retrieve the latitude and longitude of a crag given its name. 
    Returns a tuple (lat, lon) or None if the crag is not found.
    '''
    con = connect_to_database(db_name)
    cur = con.cursor()
    res = cur.execute("SELECT lat, lon FROM crag WHERE name = ?", (crag_name,))
    coordinates = res.fetchone()
    con.close()
    return coordinates

def insert_new_crag(crag_name: str, lat: float, lon: float, db_name="database/cage.db"):
    ''' Insert a new crag into the database. Returns True if successful. '''
    con = connect_to_database(db_name)
    cur = con.cursor()
    cur.execute("INSERT INTO crag (name, lat, lon) VALUES (?, ?, ?)", (crag_name, lat, lon))
    con.commit()
    con.close()
    return True

