
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def create(fullscreen=True):
    caps = DesiredCapabilities.FIREFOX.copy()
    # Disable certificate warning
    caps['acceptInsecureCerts'] = True

    driver = webdriver.Firefox(capabilities=caps)
    
    if fullscreen:
        # Set to full screen
        driver.fullscreen_window()

    return driver