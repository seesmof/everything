from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()


currentDir = path.dirname(path.abspath(__file__))
dataDir = path.join(currentDir, "..", "data")
moviesFile = path.join(dataDir, "movies.md")

movies = []
with open(moviesFile, "r", encoding="utf-8") as f:
    for line in f:
        # Format: MovieName (MovieYear)
        name, year = line.strip().split(" (")
        year = int(year[:-1])
        movies.append((name, year))
movies.sort(key=lambda movie: movie[0])
console.print(movies)
