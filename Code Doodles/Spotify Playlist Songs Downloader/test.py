from time import sleep
from rich.console import Console
from rich.traceback import install
import YouTubeMusicAPI

install()
console = Console()


def scrapeForUrl(url: str) -> str:
    from seleniumbase import SB

    with SB(uc=True) as s:
        s.open("https://yt1s.com/en572/youtube-to-mp3")
        s.type("input#s_input", url)
        s.click("button#btn-convert")
        s.wait_for_element("button#btn-action")
        s.click("button#btn-action")
        s.wait_for_element("a#asuccess")
        link = s.wait_for_element("a#asuccess").get_attribute("href")
        return link


TEST_URL = "https://music.youtube.com/watch?v=3mPu1ho7ThY"
console.print(scrapeForUrl(TEST_URL))
