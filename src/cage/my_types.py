from math import cos, sin, radians

class Crag:
    """Class representing a climbing crag."""

    def __init__ (self, name, lat, lon):
        """Initialize a Crag object."""
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        """String representation of the Crag object."""
        return f"Crag: {self.name} -> (lat={self.lat}, lon={self.lon})"

    def cartesian_coordinates(self):
        """Convert latitude and longitude to Cartesian coordinates.
        Returns a tuple (x, y, z).
        """
        r = 6371  # Earth's radius in kilometers
        lat_rad = radians(self.lat)
        lon_rad = radians(self.lon)
        x = r * cos(lat_rad) * cos(lon_rad)
        y = r * cos(lat_rad) * sin(lon_rad)
        z = r * sin(lat_rad)
        return (x, y, z)

class Station:
    """Class representing a weather station."""

    def __init__ (self, name, lat, lon, ilmeteo_url_name):
        """Initialize a Station object."""
        self.name = name
        self.lat = lat
        self.lon = lon
        self._ilmeteo_url_name = ilmeteo_url_name

    def __repr__(self):
        """String representation of the Station object."""
        return f"Weather station: {self.name} -> (lat={self.lat}, lon={self.lon})"

    def cartesian_coordinates(self):
        """Convert latitude and longitude to Cartesian coordinates.
        Returns a tuple (x, y, z).
        """
        r = 6371  # Earth's radius in kilometers
        lat_rad = radians(self.lat)
        lon_rad = radians(self.lon)
        x = r * cos(lat_rad) * cos(lon_rad)
        y = r * cos(lat_rad) * sin(lon_rad)
        z = r * sin(lat_rad)
        return (x, y, z)
