import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class LoginPageSaucedemo(BasePage):

    # Locators
    _username_textbox = (By.XPATH, "//input[@id='user-name']")
    _password_textbox = (By.XPATH, "//input[@id='password']")
    _login_button = (By.XPATH, "//input[@id='login-button']")
    _swag_labs_logo = (By.XPATH, "//div[@class='app_logo']")
    _swag_labs_logo2 = (By.XPATH, "//div[@class='app_logo2']")
    _invalid_login_error_message = (By.XPATH, "//h3[@data-test='error']")


    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username, password):
        """Perform login action"""
        try:
            self.enter_text(self._username_textbox, username)
            self.enter_text(self._password_textbox, password)
            self.click_element(self._login_button)
        except Exception as e:
            self.screenshot_util.take_screenshot()
            self.log.error(f"User is unable to login. \nError -> {e}")
            pytest.fail(f"User is unable to login. \nError -> {e}")


    @allure.step("User is successfully logged in")
    def user_successfully_logged_in(self):
        try:
            swag_labs_logo = self.wait.until(EC.visibility_of_element_located(self._swag_labs_logo)).is_displayed()
            assert swag_labs_logo == True
        except TimeoutException:
            self.screenshot_util.take_screenshot()
            self.log.error(f"User is unable to login")
            pytest.fail(f"User is unable to login")


    @allure.step("Enter username and password")
    def enter_username_and_password(self, username, password):
        try:
            self.enter_text(self._username_textbox, username)
            self.enter_text(self._password_textbox, password)
        except Exception as e:
            self.screenshot_util.take_screenshot()
            self.log.error(f"User is unable to enter username and password. Error -> {e}")
            pytest.fail(f"User is unable to enter username and password. Error -> {e}")


    @allure.step("Click Login Button")
    def click_login_button(self):
        self.click_element(self._login_button)


    @allure.step("Verify invalid login error message is displayed")
    def verify_invalid_login_error_message(self, expected_error_message):
        error_message = self.wait.until(EC.visibility_of_element_located(self._invalid_login_error_message)).text
        self.log.info(f"Actual Error Message = {error_message}")
        try:
            assert error_message == expected_error_message
        except Exception:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Incorrect error message displayed: Expected = {expected_error_message}, Actual = {error_message}.")
            pytest.fail(f"Incorrect error message displayed: Expected = {expected_error_message}, Actual = {error_message}.")


