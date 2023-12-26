import json
from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

REDIRECT_URL = "http://localhost:8888/"
SCOPES = "playlist-read-private"
CLIENT_ID = None
CLIENT_SECRET = None


def loadSpotifyData():
    fileName = "spotifyData.json"
    currentDir = path.dirname(path.abspath(__file__))
    relativePath = path.join(currentDir, "..", "data", fileName)
    with open(relativePath, "r", encoding="utf-8") as f:
        return json.load(f)


def setSpotifyData():
    data = loadSpotifyData()
    global CLIENT_ID, CLIENT_SECRET
    CLIENT_ID = data["CLIENT_ID"]
    CLIENT_SECRET = data["CLIENT_SECRET"]
    console.log("Spotify data loaded")


setSpotifyData()

"""
1. get spotify playlist url input from user
2. parse playlist and get a list of tracks
3. for each track, go to youtube and search for this track
    - if found, go to youtube music converter and download
    - else, output an error and continue
"""

# spotifyPlaylistUrl = input("Enter Spotify Playlist URL: ")
