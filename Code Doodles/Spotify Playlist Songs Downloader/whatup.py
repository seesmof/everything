from rich.console import Console
from rich.traceback import install

install()
console = Console()

from seleniumbase import SB

with SB(uc=True, demo=True) as driver:
    driver.open("https://www.youtube.com/results?search_query=ridin+blessed")
    songName = "Ridin' Blessed"
    driver.click(f"a:contains({songName})")
    videoUrl = driver.get_attribute("href")
    driver.open(f"https://yt1s.com/en572/youtube-to-mp3")
    driver.type("#s_input", videoUrl)
    driver.click("#btn-convert")
    driver.wait(1)
    driver.click("#btn-action")
    driver.wait(5)
    driver.click("#btn-action")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.youtube.com/results?search_query=ridin+blessed")
songName = "Ridin' Blessed"

links = driver.find_elements(
    "xpath", "//a[@class='yt-simple-endpoint style-scope ytd-video-renderer']"
)
for link in links:
    if link.text == songName:
        link.click()
        videoUrl = link.get_attribute("href")
        break

driver.execute_script("window.open('https://yt1s.com/en572/youtube-to-mp3');")
driver.switch_to.window(driver.window_handles[-1])
inputField = driver.find_element("xpath", "//input[@id='s_input']")
inputField.send_keys(videoUrl)
convertButton = driver.find_element("xpath", "//button[@id='btn-convert']")
convertButton.click()
downloadButton = driver.find_element("xpath", "//button[@id='btn-action']")
finalButton = driver.find_element("xpath", "//a[@id='asuccess']")
finalButton.click()

driver.quit()
