"""
autologin/robot.py

"""

import os
from time import sleep
from datetime import datetime
import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

logger = logging.getLogger(__name__)

class Robot:
    def __init__(self, driver, url, short_wait=5, medium_wait=30, long_wait=60, auto_close_browser=True):
            
        self.driver = driver
        self.url = url
        
        self.options = {}
        self.options["short_wait"] = short_wait
        self.options["medium_wait"] = medium_wait
        self.options["long_wait"] = long_wait
        self.options["auto_close_browser"] = auto_close_browser
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.options["auto_close_browser"]:
            self.driver.quit()
     
    def get_username_field(self):
        wait = WebDriverWait(self.driver, self.options["short_wait"])
        return wait.until(EC.presence_of_element_located((By.ID, "txtUserID")))
        
    def get_password_field(self):
        wait = WebDriverWait(self.driver, self.options["short_wait"])
        return wait.until(EC.presence_of_element_located((By.ID, "txtPassWord")))
    
    def get_login_button(self):
        wait = WebDriverWait(self.driver, self.options["short_wait"])
        return wait.until(EC.presence_of_element_located((By.ID, "login")))
    
    def get_login_error_message(self):
        try:
            wait = WebDriverWait(self.driver, self.options["short_wait"])
            return wait.until(EC.presence_of_element_located((By.ID, "login")))
        except:
            return None

    def get_cont_button(self):
        try:
            wait = WebDriverWait(self.driver, self.options["short_wait"])
            return wait.until(EC.presence_of_element_located((By.ID, "cont")))
        except:
            return None

    def click(self, element):
        """Clicks on an element, if fails, tries again using javascript"""
        try:
            wait = WebDriverWait(element, self.options["short_wait"])
            wait.until(EC.element_to_be_clickable((By.XPATH, ".")))
            element.click()
        except:
        #except ElementClickInterceptedException:
            sleep(1)
            self.driver.execute_script("arguments[0].click();", element)
        
        
    def navigate(self, url):
        logger.info("Opening URL: %s", url)
        self.driver.get("about:blank")
        self.driver.get(url)

    @property
    def login_required(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body_class = body.get_attribute("class")

        return body_class == "loginPageLoaded"

    def login(self, username: str, password: str):
        self.navigate(url=self.url + "/login/login.html")

        self.get_username_field().send_keys(username)
        self.get_password_field().send_keys(password)

        self.click(self.get_login_button())
        sleep(1)
        login_error_message = self.get_login_error_message()
        
        if login_error_message is not None:
            logger.warn(login_error_message.text)

            cont_button = self.get_cont_button()
            if cont_button is not None and cont_button.is_displayed:
                try:
                    self.click(cont_button)
                except Exception as e:
                    logger.warn(e)
                    
                return True

        return login_error_message is None
            
