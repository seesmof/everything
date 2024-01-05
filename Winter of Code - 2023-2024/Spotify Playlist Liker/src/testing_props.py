from os import path
from rich.console import Console
from rich.traceback import install
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler

from utils import *

install()
console = Console()
scope = "user-library-modify"
current_dir = path.dirname(path.abspath(__file__))
cache_file = path.join(current_dir, "..", "data", "cache.json")
