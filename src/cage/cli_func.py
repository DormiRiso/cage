import re
from matplotlib import pyplot as plt
import numpy as np
from cage.cli import DB_PATH
import cage.db_manager as db_manager
from cage.my_types import Crag, Station
    
def view_crags(args):
    """View all crags in the database."""
    crags = db_manager.list_all_crags(DB_PATH)
    if not crags:
        print("No crags found in the database.")
        return
    for crag in crags:
        print(crag)

def view_stations(args):
    """View all weather stations in the database."""
    stations = db_manager.list_all_stations(DB_PATH)
    if not stations:
        print("No weather stations found in the database.")
        return
    for station in stations:
        print(station)

def add_crag(args):
    """Add a new crag to the database.
    Prompts the user for crag name, latitude, and longitude.
    """
    name = input("Enter crag name: ").strip()
    try:
        lat_str = input("Enter latitude: ").strip()
        lon_str = input("Enter longitude: ").strip()
        # Check if lat and lon are floats in the form xx.xxxx
        float_pattern = r"^-?\d{1,2}\.\d{4}$"
        if not re.match(float_pattern, lat_str) or not re.match(float_pattern, lon_str):
            print("Latitude and longitude must be in the format xx.xxxx (e.g., 12.3456).")
            return
        lat = float(lat_str)
        lon = float(lon_str)

    except ValueError:
        print("Invalid latitude or longitude. Please enter numeric values.")
        return

    if db_manager.insert_new_crag(name, lat, lon, DB_PATH):
        print(f"Crag '{name}' added successfully.")
    else:
        print(f"Failed to add crag '{name}'. It may already exist.")

def add_station(args):
    """Add a new weather station to the database.
    Prompts the user for station name, latitude, longitude, and ilmeteo URL name.
    """
    name = input("Enter station name: ").strip()
    try:
        lat_str = input("Enter latitude: ").strip()
        lon_str = input("Enter longitude: ").strip()
        ilmeteo_url_name = input("Enter ilmeteo URL name: ").strip()
        # Check if lat and lon are floats in the form xx.xxxx
        float_pattern = r"^-?\d{1,2}\.\d{4}$"
        if not re.match(float_pattern, lat_str) or not re.match(float_pattern, lon_str):
            print("Latitude and longitude must be in the format xx.xxxx (e.g., 12.3456).")
            return
        lat = float(lat_str)
        lon = float(lon_str)

    except ValueError:
        print("Invalid latitude or longitude. Please enter numeric values.")
        return

    if db_manager.insert_new_station(name, lat, lon, ilmeteo_url_name, DB_PATH):
        print(f"Station '{name}' added successfully.")
    else:
        print(f"Failed to add station '{name}'. It may already exist.")

def plot_crags_and_stations(args):
    """Plot crags and weather stations in a 3D space."""

    crag_list = db_manager.list_all_crags(DB_PATH)
    station_list = db_manager.list_all_stations(DB_PATH)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('3D Visualization of Crags and Weather Stations')
    ax.grid(True)
    ax.set_box_aspect([1,1,0.5])  # Aspect ratio is 1:1:0.5
    # Plot crags
    for crag in crag_list:
        x, y, z = crag.cartesian_coordinates()
        ax.scatter(x, y, z, color='red', s=50, label='Crag' if 'Crag' not in ax.get_legend_handles_labels()[1] else "")
    # Plot stations
    for station in station_list:
        x, y, z = station.cartesian_coordinates()
        ax.scatter(x, y, z, color='green', s=50, label='Station' if 'Station' not in ax.get_legend_handles_labels()[1] else "")
    plt.legend()
    plt.show()