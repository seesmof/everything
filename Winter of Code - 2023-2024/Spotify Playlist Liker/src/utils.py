import json
import inquirer


def getUrl() -> str:
    question = [
        inquirer.Text(
            "url",
            message="Enter a Spotify Playlist URL",
            validate=lambda _, x: x != ""
            and x.startswith("https://open.spotify.com/playlist/"),
        )
    ]
    answer = inquirer.prompt(question)
    return answer["url"]


def getAction() -> str:
    question = [
        inquirer.List(
            "action",
            message="Choose an action to take",
            choices=["Like", "Dislike"],
            default="Like",
        )
    ]
    answer = inquirer.prompt(question)
    return answer["action"]


def loadJson(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def saveJson(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def checkAndPromptData(authData: dict, variable: str) -> str:
    if authData[variable] != "":
        return authData[variable]
    else:
        name = variable.replace("_", " ").title()
        question = [
            inquirer.Text(
                variable,
                message=f"Enter your {name}",
            )
        ]
        answer = inquirer.prompt(question)
        return answer[variable]


def performActionOnTracks(
    playlist: dict, spotify: object, console: object, action: str
):
    tracks = playlist["tracks"]["items"]
    try:
        with console.status("Processing all the tracks..."):
            for track in tracks:
                trackId = track["track"]["id"]
                spotify.current_user_saved_tracks_add(
                    [trackId]
                ) if action == "Like" else spotify.current_user_saved_tracks_delete(
                    [trackId]
                )
        console.print(
            f"[green]Successfully {action.lower()}d all tracks in {playlist['name']}[/green]"
        )
    except Exception as e:
        console.print(f"[red]Failed to {action.lower()} all tracks: {e}[/red]")
