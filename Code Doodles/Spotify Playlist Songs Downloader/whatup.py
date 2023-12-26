from rich.console import Console
from rich.traceback import install

install()
console = Console()

import YouTubeMusicAPI

songName = "Ridin' Blessed"
result = YouTubeMusicAPI.search(songName)

console.print(result["url"] if result else "[red]No results found[/]")
