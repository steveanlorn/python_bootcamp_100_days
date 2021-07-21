import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotipy API docs: https://spotipy.readthedocs.io/en/2.18.0/#api-reference

# https://developer.spotify.com/documentation/general/guides/scopes/
SCOPE_PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"


class Spotify:
    def __init__(self, client_id: str, client_secret: str, scopes: list[str]):
        self.sp = spotipy.Spotify(
            # https://developer.spotify.com/documentation/general/guides/authorization-guide/
            auth_manager=SpotifyOAuth(
                scope=scopes,
                redirect_uri="http://127.0.0.1:5500/",
                client_id=client_id,
                client_secret=client_secret,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]

    # https://developer.spotify.com/documentation/web-api/reference/#category-search
    def search_song_URI(self, title: str, year: str = '') -> str:
        result = self.sp.search(q=f"track:{title} year:{year}", type="track", limit=1, market="ID")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            return uri
        except IndexError:
            pass

    # https://developer.spotify.com/documentation/web-api/reference/#endpoint-create-playlist
    def create_playlist(self, name: str) -> str:
        playlist = self.sp.user_playlist_create(user=self.user_id, name=name, public=False)
        return playlist["id"]

    # https://developer.spotify.com/documentation/web-api/reference/#endpoint-add-tracks-to-playlist
    def add_item_to_playlist(self, playlist_id: str, items: list[str]):
        self.sp.playlist_add_items(playlist_id, items)
