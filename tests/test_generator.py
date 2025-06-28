import os
from src.generator import generate_spotify_csv

def test_csv_generation_creates_file():
    test_file = 'data/test_spotify_data.csv'
    user_num = 10
    generate_spotify_csv(test_file, rows=user_num)
    assert os.path.exists(test_file)
    with open(test_file, 'r') as file:
        lines = file.readlines()
    assert len(lines) >= user_num
    os.remove(test_file)

