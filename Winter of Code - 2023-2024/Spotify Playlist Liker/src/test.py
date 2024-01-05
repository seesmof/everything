from os import path
from rich.console import Console
from rich.traceback import install
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler

from utils import *

scope = "user-library-modify"
currentDir = path.dirname(path.abspath(__file__))
cacheFile = path.join(currentDir, "..", "data", "cache.json")

url = "https://open.spotify.com/album/19sjeby9koY2PM85HL07lu?si=yDPrbdWDQgiM8H3jY4TDow"

spotify = Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="352617185d53483494fcc3615ee0e7ac",
        client_secret="ee221bd7a5be46539ffc2b53403e1376",
        redirect_uri="http://localhost:8000",
        cache_handler=CacheFileHandler(cache_path=cacheFile),
    )
)

container = spotify.album(album_id=getId(url))
tracks = container["tracks"]["items"]
for track in tracks:
    print(track["name"])
