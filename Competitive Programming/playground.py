from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


import requests

baseUrl = "https://biblia-api-pdf.herokuapp.com/api"
params = {
    "method": "bible",
    "version": "AMP",
    "book": "MAT",
    "cStart": "19",
    "cEnd": "19",
    "vStart": "26",
    "vEnd": "26",
}
response = requests.get(baseUrl, params=params)
console.print(response)
data = response.json()
verseContent = data["content"][0]["verses"]["v26"]
console.print(f"Matthew 19:26 AMP - {verseContent}")
