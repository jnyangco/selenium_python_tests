import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver
# from base.selenium_driver import SeleniumDriver
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus
from utils.config_reader import read_config as data


class OrangeHrmPage:

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        # self.base_url = "https://opensource-demo.orangehrmlive.com/"
        self.wait = WebDriverWait(driver, 10)

    # ELEMENTS
    # Login Page (lp)
    _lp_username_textbox = (By.XPATH, "//input[@name='username']")
    _lp_password_textbox = (By.XPATH, "//input[@name='password']")
    _lp_login_button = (By.XPATH, "//button[text()=' Login ']")



    # FUNCTIONS
    @allure.step("Open OrangeHRM Website")
    def open_orangehrm_website(self):
        self.log.info("Open OrangeHRM Website")
        base_url = data("orangehrm", "base_url")
        self.driver.get(base_url)


    @allure.step("Login using username and password")
    def login_with_username_and_password(self, username, password):
        self.log.info("Login using username and password")
        self.log.info(f"Enter username '{username}'")
        username_textbox = self.wait.until(EC.element_to_be_clickable(self._lp_username_textbox))
        username_textbox.send_keys(username)

        self.log.info(f"Enter password '{password}'")
        password_textbox = self.wait.until(EC.element_to_be_clickable(self._lp_password_textbox))
        password_textbox.send_keys(password)

        self.log.info("Click Login button")
        login_button = self.wait.until(EC.element_to_be_clickable(self._lp_login_button))
        login_button.click()











