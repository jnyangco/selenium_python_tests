import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from core.base.base_page import BasePage
from utils.data_utils import get_data as data


class LoginPageSaucedemo(BasePage):

    # ============================================================================
    # LOCATORS
    # ============================================================================
    _username_textbox = (By.XPATH, "//input[@id='user-name']")
    _password_textbox = (By.XPATH, "//input[@id='password']")
    _login_button = (By.XPATH, "//input[@id='login-button']")
    _swag_labs_logo = (By.XPATH, "//div[@class='app_logo']")
    _swag_labs_logo2 = (By.XPATH, "//div[@class='app_logo2']")
    _invalid_login_error_message = (By.XPATH, "//h3[@data-test='error']")


    # ============================================================================
    # METHODS
    # ============================================================================
    @allure.step("Open page")
    def open(self):
        super().open(data("saucedemo", "base_url"))


    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username, password):
        """Perform login action"""
        try:
            # self.wait.until(EC.visibility_of_element_located(self._username_textbox)).send_keys(username)
            # self.wait.until(EC.visibility_of_element_located(self._password_textbox)).send_keys(password)
            # self.wait.until(EC.element_to_be_clickable(self._login_button)).click()
            self.enter_text(self._username_textbox, username)
            self.enter_text(self._password_textbox, password)
            self.click_element(self._login_button)
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error(f"Failed to login with {username} and {password}.")
            raise


    @allure.step("Verify user is logged in")
    def is_logged_in(self):
        # return self.wait.until(EC.visibility_of_element_located(self._swag_labs_logo)).is_displayed()
        return self.is_displayed(self._swag_labs_logo)


    @allure.step("Enter username and password")
    def enter_username_and_password(self, username, password):
        # self.wait.until(EC.visibility_of_element_located(self._username_textbox)).send_keys(username)
        # self.wait.until(EC.visibility_of_element_located(self._password_textbox)).send_keys(password)
        self.enter_text(self._username_textbox, username)
        self.enter_text(self._password_textbox, password)


    @allure.step("Get error message")
    def get_error_message(self):
        return self.get_text(self._invalid_login_error_message)




