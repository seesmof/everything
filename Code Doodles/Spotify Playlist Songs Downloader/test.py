from time import sleep
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from seleniumbase import SB

with SB(uc=True, demo=True) as driver:
    driver.get("https://y2mate.com.co/en185z/youtube-to-mp3-converter")
    driver.type("#txt-url", "https://music.youtube.com/watch?v=3mPu1ho7ThY")
    driver.find_element("#btn-submit").click()
