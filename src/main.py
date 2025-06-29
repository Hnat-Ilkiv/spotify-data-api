import sys
from src.generator import generate_spotify_csv

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a command: -gen_csv")
    else:
        command = sys.argv[1]

        if command == '-gen_csv':
            print("CSV file generate begin.")
            generate_spotify_csv()
            print("CSV file generated successfully.")
        else:
            print(f"Unknown command: {command}")

