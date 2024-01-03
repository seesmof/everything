"""
Given a Spotify playlist URL, like or dislike all the tracks of it. For this we will need to get all of our tracks, then like or dislike them all individually.

in text: Spotify Playlist URL
in list: Action - Like | Dislike
out: Message - Success | Error
"""

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
