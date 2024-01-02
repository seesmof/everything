from letterboxdpy import movie
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


king = movie.Movie("Cast Away", 2000)
console.print(king.url)
