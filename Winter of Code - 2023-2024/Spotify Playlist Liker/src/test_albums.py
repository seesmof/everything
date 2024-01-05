from os import path
from rich.console import Console
from rich.traceback import install
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler

from utils import (
    checkAndPromptAuthData,
    getAction,
    getCollectionType,
    getUrl,
    loadJson,
    performActionOnTracks,
    saveJson,
)

install()
console = Console()
scope = "user-library-modify"
current_dir = path.dirname(path.abspath(__file__))
cache_file = path.join(current_dir, "..", "data", "cache.json")

url = "https://open.spotify.com/album/19sjeby9koY2PM85HL07lu?si=TiH6IQNTRBCohAqexEhCow"


def getAlbumId(url: str) -> str:
    # get the part after last and remove whatever may be after a ?
    res = url.split("/")[-1]
    return res.split("?")[0]


spotify = Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id="352617185d53483494fcc3615ee0e7ac",
        client_secret="768f0e9ecdee4e33a774e9c89c3b1840",
        redirect_uri="https://example.com/callback",
        cache_handler=CacheFileHandler(cache_path=cache_file),
    )
)


collection = spotify.album(album_id=getAlbumId(url))
tracks = collection["tracks"]["items"]
for track in tracks:
    name, id = track["name"], track["id"]
    console.print(f"{name} - {id}")
