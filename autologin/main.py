from .robot import Robot
from .webdrivers import firefox as firefox_driver_factory
from .webdrivers import chrome as chrome_driver_factory

from time import sleep
from datetime import datetime

import logging
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')

def get_driver_factory(webdriver):
    if webdriver == "firefox":
        return firefox_driver_factory.create
    elif webdriver == "chrome":
        return chrome_driver_factory.create
    else:
        raise ValueError("Unsupported webdriver: " + webdriver)

def main(webdriver, url, username, password, fullscreen=True, **robot_args):

    driver_factory = get_driver_factory(webdriver)

    while True:
        driver  = driver_factory(fullscreen=fullscreen)

        # Bring browser window to front
        driver.switch_to.window(driver.current_window_handle)

        with Robot(driver=driver, url=url, **robot_args) as robot:
            try:
                while True:
                    if robot.login(username, password):
                        while True:
                            if robot.login_required:
                                robot.login(username, password)
                            else:
                                sleep(1)
                    else:
                        logger.info("Login failed, retry in 30 seconds!")
                        sleep(30)
            except Exception as e:
                logger.warn(e)
