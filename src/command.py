import argparse

from src.generator import generate_spotify_csv

def generate_csv_command(args):
    print(f"CSV file generation started.")
    if args.s and not (args.m or args.l):
        generate_spotify_csv(users=10, playlists=10, songs=10, verbose=args.verbose)
    elif args.m and not (args.s or args.l):
        generate_spotify_csv(users=100, playlists=100, songs=100, verbose=args.verbose)
    elif args.l and not (args.s or args.m):
        generate_spotify_csv(users=1000, playlists=1000, songs=1000, verbose=args.verbose)
    else:
        generate_spotify_csv(users=20, playlists=60, songs=240, verbose=args.verbose)
    print(f"CSV file generated successfully.")
