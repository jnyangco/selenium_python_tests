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
            self.wait.until(EC.visibility_of_element_located(self._username_textbox)).send_keys(username)
            self.wait.until(EC.visibility_of_element_located(self._password_textbox)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self._login_button)).click()
        except TimeoutException:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Failed to login with {username} and {password}.")
            pytest.fail(f"Failed to login with {username} and {password}.")


    @allure.step("User is successfully logged in")
    def user_successfully_logged_in(self):
        try:
            swag_labs_logo_is_displayed = self.wait.until(EC.visibility_of_element_located(self._swag_labs_logo)).is_displayed()
            assert swag_labs_logo_is_displayed, "Swag labs logo should be displayed"
        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to login.")
            raise


    @allure.step("Enter username and password")
    def enter_username_and_password(self, username, password):
        try:
            self.wait.until(EC.visibility_of_element_located(self._username_textbox)).send_keys(username)
            self.wait.until(EC.visibility_of_element_located(self._password_textbox)).send_keys(password)
        except TimeoutException:
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to enter username and password.")
            pytest.fail("Failed to enter username and password.")


    @allure.step("Verify invalid login error message is displayed")
    def verify_invalid_login_error_message(self, expected_error_message):
        try:
            error_message = self.wait.until(EC.visibility_of_element_located(self._invalid_login_error_message)).text
            self.log.info(f"Actual Error Message = {error_message}")
            assert error_message == expected_error_message, \
                f"Error message mismatch: Expected = '{expected_error_message}', Actual = '{error_message}'"
        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to verify error message.")
            raise


