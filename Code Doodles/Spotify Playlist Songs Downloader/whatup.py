from time import sleep
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://y2mate.com.co/en185z/youtube-to-mp3-converter")

inputBox = driver.find_element(by="id", value="txt-url")
inputBox.send_keys("https://music.youtube.com/watch?v=3mPu1ho7ThY")

searchButton = driver.find_element(by="id", value="btn-submit")
searchButton.click()

sleep(4)

downloadButton = driver.find_element(
    by="xpath", value="//a[contains(., 'Download') and @data-ftype=\"mp3\"]"
)
neededUrl = downloadButton.get_attribute("href")

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[-1])
driver.get(neededUrl)

WebDriverWait(driver, 12).until(
    EC.presence_of_element_located(
        ("xpath", "//a[contains(., 'Download') and @id=\"A_downloadUrl\"")
    )
).click()
