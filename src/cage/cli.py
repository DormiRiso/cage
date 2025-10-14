import argparse
from cage._version import __version__
from cage import cli_func
from cage import db_manager

DB_PATH = "database/dev_cage.db"

def main():
    """Main function to handle CLI commands."""
    if not db_manager.init_db(DB_PATH):
        print("Failed to initialize the database.")
        return

    parser = argparse.ArgumentParser(description="Cage CLI Tool")
    parser.add_argument('--version', action='version', version=f'Cage version {__version__}')

    subparsers = parser.add_subparsers(title="main_command", required=True)

    crag_parser = subparsers.add_parser("crag", help="CRUD operations for crags")
    crag_subparsers = crag_parser.add_subparsers(title="crag_command", required=True)

    station_parser = subparsers.add_parser("station", help="CRUD operations for weather stations")
    station_subparsers = station_parser.add_subparsers(title="station_command", required=True)

    plot_parser = subparsers.add_parser("plot", help="Plot crags and weather stations in 3D")
    plot_parser.set_defaults(func=cli_func.plot_crags_and_stations)

    crag_view_parser = crag_subparsers.add_parser("view", help="View all crags")
    crag_view_parser.set_defaults(func=cli_func.view_crags)

    station_view_parser = station_subparsers.add_parser("view", help="View all weather stations")
    station_view_parser.set_defaults(func=cli_func.view_stations)

    crag_add_parser = crag_subparsers.add_parser("add", help="Add a new crag")
    crag_add_parser.set_defaults(func=cli_func.add_crag)

    station_add_parser = station_subparsers.add_parser("add", help="Add a new weather station")
    station_add_parser.set_defaults(func=cli_func.add_station)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    """Run the main function if this script is executed."""
    main()
