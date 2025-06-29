import argparse
from src.command import generate_csv_command

def main():
    parser = argparse.ArgumentParser(description="Spotify Data CLI")

    subparsers = parser.add_subparsers(dest='command', required=True)

    gen_csv_parser = subparsers.add_parser('gen_csv', help='Generation Spotify CSV')
    gen_csv_parser.add_argument('-s', action='store_true', help='Generate small CSV file')
    gen_csv_parser.add_argument('-m', action='store_true', help='Generate medium CSV file')
    gen_csv_parser.add_argument('-l', action='store_true', help='Generate large CSV file')
    gen_csv_parser.add_argument('--verbose', action='store_true', help='Enable verbose output mode')
    gen_csv_parser.set_defaults(func=generate_csv_command)

    
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
