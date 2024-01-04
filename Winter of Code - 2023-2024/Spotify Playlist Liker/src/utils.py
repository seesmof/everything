import json
import inquirer


def get_collection_type() -> str:
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


def get_url(collection_type: str) -> str:
    question = [
        inquirer.Text(
            "url",
            message=f"Enter a Spotify {collection_type.title()} URL",
            validate=lambda _, x: x != ""
            and x.startswith(f"https://open.spotify.com/{collection_type.lower()}/"),
        )
    ]
    answer = inquirer.prompt(question)
    return answer["url"]


def get_action() -> str:
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


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def check_and_prompt_data(auth_data: dict, variable: str) -> str:
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


def get_playlist_tracks(playlist_object: object) -> list:
    return [track for track in playlist_object["tracks"]["items"]]


def get_album_tracks(album_object: object) -> list:
    return [track for track in album_object["tracks"]["items"]]


def get_artist_tracks(artist_object: object) -> list:
    return [track for track in artist_object["top_tracks"]["tracks"]]


def perfrom_action_on_tracks(
    collection: dict,
    collection_type: str,
    spotify: object,
    console: object,
    action: str,
):
    tracks = (
        get_playlist_tracks()
        if collection_type == "Playlist"
        else get_album_tracks()
        if collection_type == "Album"
        else get_artist_tracks()
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
