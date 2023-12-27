from time import sleep
from rich.console import Console
from rich.traceback import install
import YouTubeMusicAPI

install()
console = Console()


def scrapeForUrl(url: str) -> str:
    from seleniumbase import Driver

    s = Driver(uc=True)
    s.open("https://yt1s.com/en572/youtube-to-mp3")
    s.type("input#s_input", url)
    s.click("button#btn-convert")
    s.find_element("button#btn-action").click()
    s.highlight("a#asuccess", timeout=30)


TEST_URL = "https://music.youtube.com/watch?v=3mPu1ho7ThY"
scrapeForUrl(TEST_URL)
