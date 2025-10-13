import sqlite3

def connect_to_database(db_name="database/cage.db"):
    '''Function to connect to the SQLite database
    Returns a connection object'''
    try:
        con = sqlite3.connect(db_name)
        return con
    except ValueError:
        print("Error connecting to the database")
        return None

def get_coordinates_from_crag_name(crag_name, db_name="database/cage.db"):
    '''Function to get the coordinates of a crag from its name
    Returns a tuple (latitude, longitude)'''
    con = connect_to_database(db_name)
    cur = con.cursor()
    res = cur.execute(f"SELECT lat, lon FROM crag WHERE name='{crag_name}';")
    coordinates = res.fetchone()
    con.close()
    return coordinates

def insert_new_crag(crag_name: str, lat: float, lon: float, db_name="database/cage.db"):
    '''Function to insert a new crag into the database
    Returns True if the insertion was successful'''
    con = connect_to_database(db_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS crag(name TEXT, lat REAL, lon REAL)")
    con.commit()
    cur.execute(f"""INSERT INTO crag (name, lat, lon) VALUES ('{crag_name}', {lat}, {lon})""")
    con.commit()
    con.close()
    return True

