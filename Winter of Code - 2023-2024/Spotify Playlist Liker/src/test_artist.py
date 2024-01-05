from testing_props import *

url = "https://open.spotify.com/artist/4DpKv8e5T2yDXy0CT7H5dG?si=8jHM8VPTRGSpVH6sBndu2Q"

spotify = Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="352617185d53483494fcc3615ee0e7ac",
        client_secret="768f0e9ecdee4e33a774e9c89c3b1840",
        redirect_uri="https://example.com/callback",
        cache_handler=CacheFileHandler(cache_path=cache_file),
    )
)


# For artist: A collection is an artist albums method with artist ID passed as argument
container = spotify.artist_albums(artist_id=getId(url))
tracks = []
for album in container["items"]:
    object = spotify.album(album_id=album["id"])
    currentTracks = object["tracks"]["items"]
    tracks.extend(currentTracks)

for track in tracks:
    name, id = track["name"], track["id"]
    console.print(f"{name} - {id}")

"""
[
    {
        'album_group': 'album',
        'album_type': 'album',
        'artists': [
            {
                'external_urls': {'spotify': 'https://open.spotify.com/artist/4DpKv8e5T2yDXy0CT7H5dG'},
                'href': 'https://api.spotify.com/v1/artists/4DpKv8e5T2yDXy0CT7H5dG',
                'id': '4DpKv8e5T2yDXy0CT7H5dG',
                'name': 'Extol Records',
                'type': 'artist',
                'uri': 'spotify:artist:4DpKv8e5T2yDXy0CT7H5dG'
            }
        ],
        'external_urls': {'spotify': 'https://open.spotify.com/album/19sjeby9koY2PM85HL07lu'},
        'href': 'https://api.spotify.com/v1/albums/19sjeby9koY2PM85HL07lu',
        'id': '19sjeby9koY2PM85HL07lu',
        'name': 'Heavenly Phonk',
        'release_date': '2023-12-15',
        'release_date_precision': 'day',
        'total_tracks': 11,
        'type': 'album',
        'uri': 'spotify:album:19sjeby9koY2PM85HL07lu'
    }
]
"""
