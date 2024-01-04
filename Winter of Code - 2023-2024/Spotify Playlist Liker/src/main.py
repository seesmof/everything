"""
Given a Spotify playlist URL, like or dislike all the tracks of it. For this we will need to get all of our tracks, then like or dislike them all individually.

in text: Spotify Playlist URL
in list: Action - Like | Dislike
out: Message - Success | Error
"""

from os import path
from rich.console import Console
from rich.traceback import install
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler

from utils import (
    checkAndPromptData,
    getAction,
    getUrl,
    loadJson,
    performActionOnTracks,
    saveJson,
)

install()
console = Console()
currentDir = path.dirname(path.abspath(__file__))
authFile = path.join(currentDir, "..", "data", "auth.json")
cacheFile = path.join(currentDir, "..", "data", "cache.json")
scope = "user-library-modify"


def main() -> None:
    # ask for url
    url = getUrl()
    # ask for action
    action = getAction()
    # load data from auth.json and check if they exist
    authData = loadJson(path=authFile)
    # if not ask for all of those too
    client_id, client_secret, redirect_url = (
        checkAndPromptData(authData=authData, variable="clientId"),
        checkAndPromptData(authData=authData, variable="clientSecret"),
        checkAndPromptData(authData=authData, variable="redirectUri"),
    )
    saveJson(
        path=authFile,
        data={
            "clientId": client_id,
            "clientSecret": client_secret,
            "redirectUri": redirect_url,
        },
    )
    # create spotify object and get necessary variables
    spotify = Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_url,
            scope=scope,
            cache_path=CacheFileHandler(cache_path=cacheFile),
        )
    )
    playlist = spotify.playlist(url)
    # like or dislike all of the tracks
    performActionOnTracks(
        playlist=playlist, spotify=spotify, console=console, action=action
    )
