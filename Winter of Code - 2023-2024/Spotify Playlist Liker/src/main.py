"""
Given a Spotify playlist URL, like or dislike all the tracks of it. For this we will need to get all of our tracks, then like or dislike them all individually.

in text: Spotify Playlist URL
in list: Action - Like | Dislike
out: Message - Success | Error
"""

import json
from os import path
import inquirer
from rich.markdown import Markdown as md
from rich.console import Console
from rich.traceback import install

install()
console = Console()

urlQuestion = [
    inquirer.Text(
        "playlistUrl",
        message="Enter a Spotify Playlist URL",
        validate=lambda _, x: x != ""
        and x.startswith("https://open.spotify.com/playlist/"),
    )
]
urlAnswer = inquirer.prompt(urlQuestion)
playlistUrl = urlAnswer["playlistUrl"]

actionQuestion = [
    inquirer.List(
        "action",
        message="Choose an action",
        choices=["Like", "Dislike"],
        default="Like",
    )
]
actionAnswer = inquirer.prompt(actionQuestion)
actionTaken = actionAnswer["action"]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

currentDir = path.dirname(path.abspath(__file__))
authDataPath = path.join(currentDir, "..", "data", "auth.json")
with open(authDataPath, "r", encoding="utf-8") as f:
    authData = json.load(f)

if authData["clientId"] != "":
    clientId = authData["clientId"]
else:
    clientIdQuestion = [
        inquirer.Text(
            "clientId", message="Enter your Client ID", validate=lambda _, x: x != ""
        )
    ]
    clientIdAnswer = inquirer.prompt(clientIdQuestion)
    clientId = clientIdAnswer["clientId"]

if authData["clientSecret"] != "":
    clientSecret = authData["clientSecret"]
else:
    clientSecretQuestion = [
        inquirer.Text(
            "clientSecret",
            message="Enter your Client Secret",
            validate=lambda _, x: x != "",
        )
    ]
    clientSecretAnswer = inquirer.prompt(clientSecretQuestion)
    clientSecret = clientSecretAnswer["clientSecret"]

if authData["redirectUri"] != "":
    redirectUri = authData["redirectUri"]
else:
    redirectUriQuestion = [
        inquirer.Text(
            "redirectUri",
            message="Enter your Redirect URI",
            validate=lambda _, x: x != "",
        )
    ]
    redirectUriAnswer = inquirer.prompt(redirectUriQuestion)
    redirectUri = redirectUriAnswer["redirectUri"]

with open(authDataPath, "w", encoding="utf-8") as f:
    json.dump(
        {
            "clientId": clientId,
            "clientSecret": clientSecret,
            "redirectUri": redirectUri,
        },
        f,
        indent=4,
    )

scope = "user-library-modify"
spotifyApiObject = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=clientId,
        client_secret=clientSecret,
        redirect_uri=redirectUri,
    )
)

from rich.progress import track as spinner

try:
    playlist = spotifyApiObject.playlist(playlistUrl)
    tracks = playlist["tracks"]["items"]
    for index, track in spinner(
        enumerate(tracks), description="Processing all the tracks"
    ):
        trackId = track["track"]["id"]
        spotifyApiObject.current_user_saved_tracks_add(
            [trackId]
        ) if actionTaken == "Like" else spotifyApiObject.current_user_saved_tracks_delete(
            [trackId]
        )
    console.print(
        f"[green]Successfully {actionTaken.lower()}d all tracks in given playlist[/green]"
    )
except Exception as e:
    console.print(f"[red]Failed to {actionTaken.lower()} all tracks: {e}[/red]")
