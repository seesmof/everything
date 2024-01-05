from testing_props import *

url = "https://open.spotify.com/album/19sjeby9koY2PM85HL07lu?si=TiH6IQNTRBCohAqexEhCow"

spotify = Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="352617185d53483494fcc3615ee0e7ac",
        client_secret="768f0e9ecdee4e33a774e9c89c3b1840",
        redirect_uri="https://example.com/callback",
        cache_handler=CacheFileHandler(cache_path=cache_file),
    )
)

# For albums: A collection is an album method with album ID passed as argument
collection = spotify.album(album_id=getId(url))
# And tracks are gotten out like this
tracks = collection["tracks"]["items"]

for track in tracks:
    name, id = track["name"], track["id"]
    console.print(f"{name} - {id}")
