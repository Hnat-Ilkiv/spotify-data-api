from faker import Faker
import csv
import uuid
import random

fake = Faker()

def generate_spotify_csv(filename='data/spotify_data.csv', rows=1000):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UserId', 'Username', 'PlaylistId', 'PlaylistName', 'SongId', 'SongTitle', 'Artist'])

        for user_num in range(1, rows + 1):
            user_id = str(uuid.uuid4())
            username = fake.user_name()
            for playlist_num in range(1, random.randint(2, 10)):
                playlist_id = str(uuid.uuid4())
                playlist_name = fake.word() + "_playlist"
                for song_num in range(1, random.randint(2, 30)):
                    song_id = str(uuid.uuid4())
                    song_title = fake.sentence(nb_words=3)
                    artist = fake.name()
                    writer.writerow([user_id, username, playlist_id, playlist_name, song_id, song_title, artist])

