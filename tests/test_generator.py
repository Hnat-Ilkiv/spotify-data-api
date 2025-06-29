import os
from src.generator import generate_spotify_csv

def test_csv_generation_creates_file():
    test_file = 'data/test_spotify_data.csv'
    user_num = 10
    playlist_num = 10
    song_num = 10

    lines_written = generate_spotify_csv(test_file, users=user_num, playlists=playlist_num, songs=song_num)

    assert os.path.exists(test_file)

    with open(test_file, 'r') as file:
        lines = file.readlines()

    assert len(lines) >= user_num
    assert len(lines) == lines_written

    os.remove(test_file)
    assert not os.path.exists(test_file)

