import json
from os import path
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def delete_chapters_from_json_file(json_file_path: str) -> None:
    """Deletes 'Chapters' key from JSON file at json_file_path.

    Args:
        json_file_path (str): Path to JSON file.
    """
    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for Testament in data.values():
        for Book in Testament:
            Book.pop("Chapters", None)

    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    currentDir: str = path.dirname(path.abspath(__file__))
    delete_chapters_from_json_file(path.join(currentDir, "main.json"))
