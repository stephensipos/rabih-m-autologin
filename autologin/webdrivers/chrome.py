
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def create(fullscreen=True):
    caps = DesiredCapabilities.CHROME.copy()
    # Disable certificate warning
    caps['acceptInsecureCerts'] = True

    chrome_options = Options()
    if fullscreen:
        # Start in full screen
        chrome_options.add_argument("--kiosk")

    # Disable "Chrome is being controlled by automated test software" infobar
    chrome_options.experimental_options["excludeSwitches"] = ["enable-automation"]

    driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)

    return driver