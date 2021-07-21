import songs
import datetime
import spotify
import os

date = datetime.date(2002, 10, 20)

song_list = songs.get_top_100(date)

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

if len(song_list) > 0:
    spt = spotify.Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, [spotify.SCOPE_PLAYLIST_MODIFY_PRIVATE])

    song_uris = []
    not_found_songs = []
    for song in song_list:
        title = song.get('title')
        print(f"Searching song: {title}")
        song_uri = spt.search_song_URI(title, date.strftime('%Y'))
        if song_uri is None:
            not_found_songs.append(title)
            continue
        song_uris.append(song_uri)

    play_list_id = spt.create_playlist(f"{date.strftime('%Y-%m-%d')} Billboard 100")
    spt.add_item_to_playlist(play_list_id, song_uris)

    if len(not_found_songs) > 0:
        print("-------------\n\n")
        print(f"Can not found {len(not_found_songs)} songs: ")
        for song in not_found_songs:
            print(song)
    print("-------------\n\n")
    print(f"Inserted {len(song_uris)}")
