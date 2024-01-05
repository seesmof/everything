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


def getPlaylistTracks(playlist: object) -> list:
    return [track for track in playlist["tracks"]["items"]]


def getAlbumTracks(album: object) -> list:
    return [track for track in album["tracks"]["items"]]


def getArtistTracks(artist: object) -> list:
    return [track for track in artist["top_tracks"]["tracks"]]


def performActionOnTracks(
    collection: dict,
    collectionType: str,
    spotify: object,
    console: object,
    action: str,
):
    tracks = (
        getPlaylistTracks()
        if collectionType == "Playlist"
        else getAlbumTracks()
        if collectionType == "Album"
        else getArtistTracks()
    )

    try:
        with console.status("Processing all the tracks..."):
            for track in tracks:
                track_id = track["track"]["id"]
                spotify.current_user_saved_tracks_add(
                    [track_id]
                ) if action == "Like" else spotify.current_user_saved_tracks_delete(
                    [track_id]
                )
        console.print(
            f"[green]Successfully {action.lower()}d all tracks in {collection['name']}[/green]"
        )
    except Exception as e:
        console.print(f"[red]Failed to {action.lower()} all tracks: {e}[/red]")
