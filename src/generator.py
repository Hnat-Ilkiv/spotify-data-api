from faker import Faker
from src.progress_bar import print_progress_bar
from src.file_size import file_size
import csv
import uuid
import random
import time

fake = Faker()

def generate_spotify_csv(filename='data/spotify_data.csv', users=100, playlists=100, songs=100):
    start_time = time.time()

    total_users_written = 0
    total_playlists_written = 0
    total_songs_written = 0
    total_rows_written = 0

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UserId', 'Username', 'PlaylistId', 'PlaylistName', 'SongId', 'SongTitle', 'Artist'])
        total_rows_written += 1

        # Initial call to print 0% progress
        print_progress_bar(0, users, prefix = '- Progress:', suffix = 'Complete', length = 50)

        for user_num in range(1, users + 1):
            user_id = str(uuid.uuid4())
            username = fake.user_name()
            total_users_written += 1
            for playlist_num in range(1, random.randint(2, playlists + 1)):
                playlist_id = str(uuid.uuid4())
                playlist_name = fake.word() + "_playlist"
                total_playlists_written += 1
                for song_num in range(1, random.randint(2, songs + 1)):
                    song_id = str(uuid.uuid4())
                    song_sentence = fake.sentence(nb_words=3)
                    song_title = song_sentence[:-1]
                    artist = fake.name()
                    total_songs_written += 1
                    writer.writerow([user_id, username, playlist_id, playlist_name, song_id, song_title, artist])
                    total_rows_written += 1
            # Update Progress Bar
            print_progress_bar(user_num, users, prefix = '- Progress:', suffix = 'Complete', length = 50)
        
        end_time = time.time()
        str_time = time.strftime("%H:%M:%S",time.gmtime(end_time - start_time))

        print(f"Result CSV file generate:")
        print(f"- Users written:     {total_users_written}")
        print(f"- Playlists written: {total_playlists_written}")
        print(f"- Songs written:     {total_songs_written}")
        print(f"- Rows written:      {total_rows_written}")
        print(f"- CSV file size:     {file_size(filename)}")
        print(f"- Generation time:   {str_time}")
        
    return total_rows_written
