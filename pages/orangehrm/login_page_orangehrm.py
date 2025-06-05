import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from utils.config_reader import read_config as data


class LoginPageOrangehrm(BasePageOrangehrm):

    # Locators - Login Page (lp)
    _lp_username_textbox = (By.XPATH, "//input[@name='username']")
    _lp_password_textbox = (By.XPATH, "//input[@name='password']")
    _lp_login_button = (By.XPATH, "//button[text()=' Login ']")
    _lp_error_message = (By.XPATH, "//div[@class='orangehrm-login-error']//div[1]//p")


    # Functions
    @allure.step("Open OrangeHRM Website")
    def open_orangehrm_website(self):
        self.log.info("Open OrangeHRM Website")
        base_url = data("orangehrm", "base_url")
        self.open_url(base_url)


    @allure.step("Login to Orangehrm website")
    def login(self):
        self.log.info("Login to Orangehrm website")
        base_url = data("orangehrm", "base_url")
        self.open_url(base_url)

        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        self.login_with_username_and_password(username, password)


    @allure.step("Login using username and password")
    def login_with_username_and_password(self, username, password):
        self.log.info("Login using username and password")
        self.enter_text(self._lp_username_textbox, username)
        self.enter_text(self._lp_password_textbox, password)
        self.click_element(self._lp_login_button)


    @allure.step("Verify error message using invalid login: {expected_error_message}.")
    def show_login_error_message(self, expected_error_message):
        actual_error_message = self.wait.until(EC.visibility_of_element_located(self._lp_error_message)).text

        try:
            assert self.get_text(self._lp_error_message) == expected_error_message, \
                f"Error message mismatch: Expected = '{expected_error_message}', Actual = '{actual_error_message}'"
        except AssertionError:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Error message mismatch: Expected = '{expected_error_message}', Actual = '{actual_error_message}'.")
            raise


