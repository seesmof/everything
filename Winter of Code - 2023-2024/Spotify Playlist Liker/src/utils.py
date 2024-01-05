import json
import inquirer


def getCollectionType() -> str:
    question = [
        inquirer.List(
            "collection_type",
            message="Choose a collection type",
            choices=["Playlist", "Album", "Artist"],
            default="Playlist",
        )
    ]
    answer = inquirer.prompt(question)
    return answer["collection_type"]


def getUrl(collectionType: str) -> str:
    question = [
        inquirer.Text(
            "url",
            message=f"Enter a Spotify {collectionType.title()} URL",
            validate=lambda _, x: x != ""
            and x.startswith(f"https://open.spotify.com/{collectionType.lower()}/"),
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


def checkAndPromptAuthData(auth_data: dict, variable: str) -> str:
    if auth_data[variable] != "":
        return auth_data[variable]
    else:
        name = (
            variable.replace("_", " ").title().replace("Url", "URL").replace("Id", "ID")
        )
        question = [
            inquirer.Text(
                variable,
                message=f"Enter your {name}",
            )
        ]
        answer = inquirer.prompt(question)
        return answer[variable]


def getId(url: str) -> str:
    res = url.split("/")[-1]
    return res.split("?")[0]


def performActionOnTracks(
    tracks: list,
    collectionType: str,
    spotify: object,
    console: object,
    action: str,
):
    try:
        with console.status("Processing all the tracks..."):
            for track in tracks:
                trackId = track["id"]
                spotify.current_user_saved_tracks_add(
                    [trackId]
                ) if action == "Like" else spotify.current_user_saved_tracks_delete(
                    [trackId]
                )
        console.print(
            f"[green]Successfully {action.lower()}d all tracks in a given {collectionType.lower()}[/green]"
        )
    except Exception as e:
        console.print(f"[red]Failed to {action.lower()} all tracks: {e}[/red]")
