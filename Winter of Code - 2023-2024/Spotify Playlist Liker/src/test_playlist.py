from testing_props import *

url = "https://open.spotify.com/playlist/2dLiXPJqBygejaBL5n1rDQ?si=585e84ad7aa54624"

spotify = Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="352617185d53483494fcc3615ee0e7ac",
        client_secret="768f0e9ecdee4e33a774e9c89c3b1840",
        redirect_uri="https://example.com/callback",
        cache_handler=CacheFileHandler(cache_path=cache_file),
    )
)


collection = spotify.playlist_items(url)
