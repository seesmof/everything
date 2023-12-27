from time import sleep
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import json
from os import path

import YouTubeMusicAPI
from seleniumbase import SB

from rich.console import Console
from rich.traceback import install

install()
console = Console()

REDIRECT_URL = "https://example.com/callback"
SCOPES = "playlist-read-private"
TEST_PLAYLIST_URL = "https://open.spotify.com/playlist/3PSAwyWVPlYlhQLEpvCxJX"
CLIENT_ID = None
CLIENT_SECRET = None


def loadVariables():
    fileName = "spotifyData.json"
    currentDir = path.dirname(path.abspath(__file__))
    relativePath = path.join(currentDir, "..", "data", fileName)
    try:
        with open(relativePath, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"CLIENT_ID": None, "CLIENT_SECRET": None}


def setSpotifyData():
    data: dict = loadVariables()
    global CLIENT_ID, CLIENT_SECRET
    CLIENT_ID = data["CLIENT_ID"]
    CLIENT_SECRET = data["CLIENT_SECRET"]

    console.log(
        "[green]Loaded Spotify data[/]"
        if CLIENT_ID and CLIENT_SECRET
        else "[red]Failed to load Spotify data[/]"
    )


def parsePlaylist(url: str):
    spotifyClient = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URL,
            scope=SCOPES,
        )
    )

    playlistId = url.split("/")[-1]
    try:
        playlistData = spotifyClient.playlist(playlistId)
    except Exception as e:
        console.log(f"[red]Failed to parse playlist: \n{e}[/]")
        return None

    tracks = []
    for item in playlistData["tracks"]["items"]:
        track = item["track"]
        author, name = track["artists"][0]["name"], track["name"]
        tracks.append((author, name))

    console.log(
        f"[green]Parsed {len(tracks)} tracks[/]"
        if tracks
        else "[red]Failed to parse tracks[/]"
    )
    return sorted(tracks)


def getYoutubeLink(name: str, author: str):
    trackUrl = YouTubeMusicAPI.search(f"{author} - {name}")
    youtubeLink = trackUrl["url"] if trackUrl else None
    return youtubeLink


def lookForTracks(tracks: [(str, str)]):
    from seleniumbase import Driver

    s = Driver(uc=True)
    DOWNLOADER_URL = "https://yt1s.com/en572/youtube-to-mp3"

    for author, name in tracks:
        youtubeLink = getYoutubeLink(name, author)
        if not youtubeLink:
            console.log(f"[red]Failed to find track: {author} - {name}[/]")
            continue

        s.open(DOWNLOADER_URL)
        s.type("input#s_input", youtubeLink)
        s.click("button#btn-convert")
        s.wait_for_element("button#btn-action").click()
        s.highlight("a#asuccess")

    sleep(60)


"""
1. get spotify playlist url input from user
2. parse playlist and get a list of tracks
3. for each track, go to youtube and search for this track
    - if found, go to youtube music converter and download
    - else, output an error and continue
"""


def main():
    setSpotifyData()

    # spotifyPlaylistUrl = input("Enter Spotify Playlist URL: ")
    spotifyPlaylistUrl = TEST_PLAYLIST_URL

    listOfTracks = (
        parsePlaylist(spotifyPlaylistUrl)
        if spotifyPlaylistUrl
        else console.log("[red]Failed to parse playlist url[/]")
    )
    lookForTracks(listOfTracks) if listOfTracks else console.log(
        "[red]No tracks found[/]"
    )


if __name__ == "__main__":
    main()
