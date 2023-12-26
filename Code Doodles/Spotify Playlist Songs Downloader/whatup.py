from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from rich.console import Console
from rich.traceback import install

install()
console = Console()


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install()), options=options
)
driver.get("https://www.youtube.com/results?search_query=AD%CE%9BM+EXODUS")
driver.maximize_window()

links = driver.find_elements(
    "xpath", "//yt-formatted-string[@class='style-scope ytd-video-renderer']"
)
for link in links:
    if "EXODUS" in link.text:
        link.click()
        break
