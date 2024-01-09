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
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://y2mate.com.co/en185z/youtube-to-mp3-converter")

inputBox = driver.find_element(By.ID, "txt-url")
inputBox.send_keys("https://music.youtube.com/watch?v=3mPu1ho7ThY")

searchButton = driver.find_element(By.ID, "btn-submit")
searchButton.click()

wait = WebDriverWait(driver, 60)
downloadButton = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(., 'Download') and @data-ftype=\"mp3\"]")
    )
)
downloadButton.click()

"""
neededUrl = downloadButton.get_attribute("href")

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[-1])
driver.get(neededUrl)
"""

newWait = WebDriverWait(driver, 60)
download = newWait.until(EC.element_to_be_clickable((By.ID, "A_downloadUrl")))
download.click()

console.log("Started waiting for file to download")
sleep(5)
