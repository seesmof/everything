from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()


currentDir = path.dirname(path.abspath(__file__))
dataDir = path.join(currentDir, "..", "data")
moviesFile = path.join(dataDir, "movies.md")


def fetchMoviesFromFile(file: str) -> list[tuple[str, int]]:
    movies = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            name, year = line.strip().split(" (")
            year = int(year[:-1])
            movies.append((name, year))
    movies.sort(key=lambda movie: movie[0])
    return movies


movies = fetchMoviesFromFile(moviesFile)
console.print(movies)

movieLinks = []
for name, year in movies:
    url = f"https://letterboxd.com/film/{name}/"
console.print(movieLinks)
