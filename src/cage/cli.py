import argparse
from cage._version import __version__
import cage.db_manager as db_manager

def view_crags(args):
    """View all crags in the database."""
    crags = db_manager.list_all_crags()
    if not crags:
        print("No crags found in the database.")
        return
    for crag in crags:
        print(crag)

def add_crag(args):
    """Add a new crag to the database."""
    name = input("Enter crag name: ").strip()
    try:
        lat = float(input("Enter latitude: ").strip())
        lon = float(input("Enter longitude: ").strip())
    except ValueError:
        print("Invalid latitude or longitude. Please enter numeric values.")
        return

    if db_manager.insert_new_crag(name, lat, lon):
        print(f"Crag '{name}' added successfully.")
    else:
        print(f"Failed to add crag '{name}'. It may already exist.")

def main():
    """Main function to handle CLI commands."""
    if not db_manager.init_db():
        print("Failed to initialize the database.")
        return

    parser = argparse.ArgumentParser(description="Cage CLI Tool")
    parser.add_argument('--version', action='version', version=f'Cage version {__version__}')

    subparsers = parser.add_subparsers(title="main_command", required=True)

    crag_parser = subparsers.add_parser("crag", help="CRUD operations for crags")
    crag_subparsers = crag_parser.add_subparsers(title="crag_command", required=True)

    view_parser = crag_subparsers.add_parser("view", help="View all crags")
    view_parser.set_defaults(func=view_crags)

    add_parser = crag_subparsers.add_parser("add", help="Add a new crag")
    add_parser.set_defaults(func=add_crag)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    """Run the main function if this script is executed."""
    main()
