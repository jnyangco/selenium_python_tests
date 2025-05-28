import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from utils.config_reader import read_config as data


class LoginPageOrangehrm(BasePage):

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


    @allure.step("Verify error message using invalid login.")
    def show_login_error_message(self, expected_error_message):
        actual_error_message = self.wait.until(EC.visibility_of_element_located(self._lp_error_message)).text
        assert actual_error_message == expected_error_message, pytest.fail(f"Incorrect error message. Expected = {expected_error_message}, Actual = {actual_error_message}")


