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
    # Get the URL and action from the user
    url = getUrl()
    action = getAction()

    # Load the authentication data from a JSON file
    authData = loadJson(path=authFile)

    # Extract the client ID, client secret, and redirect URL from the authentication data
    client_id, client_secret, redirect_url = (
        checkAndPromptData(authData=authData, variable="clientId"),
        checkAndPromptData(authData=authData, variable="clientSecret"),
        checkAndPromptData(authData=authData, variable="redirectUri"),
    )

    # Save the extracted authentication data back to the JSON file
    saveJson(
        path=authFile,
        data={
            "clientId": client_id,
            "clientSecret": client_secret,
            "redirectUri": redirect_url,
        },
    )

    # Create a Spotify object with the extracted authentication details
    spotify = Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_url,
            cache_handler=CacheFileHandler(cache_path=cacheFile),
        )
    )

    # Get the playlist using the Spotify object and the provided URL
    playlist = spotify.playlist(url)

    # Perform the specified action on the tracks in the playlist
    performActionOnTracks(
        playlist=playlist, spotify=spotify, console=console, action=action
    )


if __name__ == "__main__":
    main()
