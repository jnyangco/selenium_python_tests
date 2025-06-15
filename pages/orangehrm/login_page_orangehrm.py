import allure
from selenium.webdriver.common.by import By
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from utils.data_utils import get_data as data


class LoginPageOrangehrm(BasePageOrangehrm):

    # Locators - Login Page (lp)
    _username_textbox = (By.XPATH, "//input[@name='username']")
    _password_textbox = (By.XPATH, "//input[@name='password']")
    _login_button = (By.XPATH, "//button[text()=' Login ']")
    _login_error_message = (By.XPATH, "//div[@class='orangehrm-login-error']//div[1]//p")


    # Functions
    @allure.step("Open Orangehrm website")
    def open_orangehrm_website(self):
        self.log.info("Open Orangehrm Website")
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


    @allure.step("Login using username: {username} and password: {password}")
    def login_with_username_and_password(self, username, password):
        self.log.info("Login using username and password")
        self.enter_text(self._username_textbox, username)
        self.enter_text(self._password_textbox, password)
        self.click_element(self._login_button)


    # implemented the code in the page class
    # @allure.step("Verify login error message using invalid login: {expected_error_message}.")
    # def verify_login_error_message(self, expected_error_message):
    #     actual_error_message = ""
    #     try:
    #         actual_error_message = self.get_text(self._login_error_message)
    #         assert actual_error_message == expected_error_message, \
    #             f"Error message mismatch: Expected = '{expected_error_message}', Actual = '{actual_error_message}'"
    #     except AssertionError:
    #         self.screenshot_util.take_screenshot()
    #         self.log.error(f"Error message mismatch: Expected = '{expected_error_message}', Actual = '{actual_error_message}'")
    #         raise

    # implemented the code in the basepage class and reuse it from page class
    @allure.step("Verify login error message using invalid login: {expected_error_message}.")
    def verify_login_error_message(self, expected_error_message):
        self.assert_element_text_matches(self._login_error_message, expected_error_message, "Error message mismatch")
        self.log.info("Verified login error message successfully.")



