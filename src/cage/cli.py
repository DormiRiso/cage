import argparse
from cage._version import __version__

# Main entry point for the CLI
def main():
    parser = argparse.ArgumentParser(description="Cage CLI Tool")
    parser.add_argument('--version', action='version', version=f'Cage version {__version__}')
    parser.add_argument('--crag', type=str, required=True, help='Name of the crag to fetch weather data for')
    parser.add_argument('--days', type=int, default=7, help='Number of days of historical weather data to fetch')
    args = parser.parse_args()

    print(f'You are searching for the weather data of the crag: {args.crag}')

# If this script is run directly, call the main function
if __name__ == "__main__":
    main()
