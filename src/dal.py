from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from src.models import User, Playlist, Song

# Абстрактні інтерфейси
class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str):
        pass


class IPlaylistRepository(ABC):
    @abstractmethod
    def add_playlist(self, playlist: Playlist):
        pass

    @abstractmethod
    def add_song_to_playlist(self, playlist: Playlist, song: Song):
        pass

    @abstractmethod
    def get_playlist_by_id(self, playlist_id: str):
        pass


class ISongRepository(ABC):
    @abstractmethod
    def add_song(self, song: Song):
        pass

    @abstractmethod
    def get_song_by_id(self, song_id: str):
        pass

    @abstractmethod
    def get_all_songs(self):
        pass


# Реалізація DAL через SQLAlchemy
class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: str):
        return self.session.query(User).filter_by(id=user_id).first()


class PlaylistRepository(IPlaylistRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_playlist(self, playlist: Playlist):
        self.session.add(playlist)
        self.session.commit()

    def add_song_to_playlist(self, playlist: Playlist, song: Song):
        playlist.songs.append(song)
        self.session.commit()

    def get_playlist_by_id(self, playlist_id: str):
        return self.session.query(Playlist).filter_by(id=playlist_id).first()


class SongRepository(ISongRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_song(self, song: Song):
        self.session.add(song)
        self.session.commit()

    def get_song_by_id(self, song_id: str):
        return self.session.query(Song).filter_by(id=song_id).first()

    def get_all_songs(self):
        return self.session.query(Song).all()

