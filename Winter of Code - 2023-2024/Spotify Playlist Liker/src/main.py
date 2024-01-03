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

console.print(f"{actionTaken} all tracks in {playlistUrl}")

# get all tracks
# for each perform the action

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load the auth data from file and see if its been saved earlier
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

with open(authDataPath, "w", encoding="utf-8") as f:
    json.dump(
        {
            "clientId": clientId,
            "clientSecret": clientSecret,
        },
        f,
        indent=4,
    )

scope = "user-library-modify"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope, client_id=clientId, client_secret=clientSecret
    )
)

# Retrieve the playlist data
playlist = sp.playlist(playlistUrl)

# Extract the track data
tracks = playlist["tracks"]["items"]

# Iterate over each track
for track in tracks:
    track_id = track["track"]["id"]

    # Check if the track is already liked or disliked
    is_liked = sp.current_user_saved_tracks_contains([track_id])[0]

    if actionTaken == "Like" and not is_liked:
        # Like the track
        sp.current_user_saved_tracks_add([track_id])
    elif actionTaken == "Dislike" and is_liked:
        # Remove the track from liked tracks
        sp.current_user_saved_tracks_delete([track_id])

# Display success message
console.print(
    f"[green]Successfully {actionTaken.lower()}d all tracks in given playlist[/green]"
)
