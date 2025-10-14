class Crag:
    """Class representing a climbing crag."""

    def __init__ (self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return f"{self.name}: (lat={self.lat}, lon={self.lon})"