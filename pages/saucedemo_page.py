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


class SauceDemoPage:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(driver, 10)

    _username_textbox = (By.XPATH, "//input[@id='user-name']")
    _password_textbox = (By.XPATH, "//input[@id='password']")
    _login_button = (By.XPATH, "//input[@id='login-button']")
    _swag_labs_logo = (By.XPATH, "//div[@class='app_logo']")
    _swag_labs_logo2 = (By.XPATH, "//div[@class='app_logo2']")
    _burger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    _burger_menu_list = (By.XPATH, "//nav[@class='bm-item-list']/a")

    _invalid_login_error_message = (By.XPATH, "//h3[@data-test='error']")


    @allure.step("Open SauceDemo Website")
    def open_saucedemo_website(self):
        self.driver.get(self.base_url)


    @allure.step("Login using username and password")
    def login_with_username_and_password(self, username, password):
        try:
            username_textbox = self.wait.until(EC.visibility_of_element_located(self._username_textbox))
            username_textbox.send_keys(username)
            password_textbox = self.wait.until(EC.visibility_of_element_located(self._password_textbox))
            password_textbox.send_keys(password)
            login_button = self.wait.until(EC.element_to_be_clickable(self._login_button))
            login_button.click()
        except Exception as e:
            self.log.error(f"User is unable to login. Error -> {e}")
            pytest.fail(f"User is unable to login.")


    @allure.step("Enter username and password")
    def enter_username_and_password(self, username, password):
        try:
            username_textbox = self.wait.until(EC.visibility_of_element_located(self._username_textbox))
            username_textbox.send_keys(username)
            password_textbox = self.wait.until(EC.visibility_of_element_located(self._password_textbox))
            password_textbox.send_keys(password)
        except Exception as e:
            self.log.error(f"User is unable to enter username and password. Error -> {e}")
            pytest.fail(f"User is unable to enter username and password.")


    @allure.step("Click Login Button")
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self._login_button))
        login_button.click()


    @allure.step("Verify invalid login error message")
    def verify_invalid_login_error_message(self, expected_error_message):
        error_message = self.wait.until(EC.visibility_of_element_located(self._invalid_login_error_message)).text
        self.log.info(f"Actual Error Message = {error_message}")
        try:
            assert error_message == expected_error_message, \
                f"Incorrect error message: Expected = {expected_error_message}, Actual = {error_message}"
        except Exception:
            pytest.fail(f"Incorrect error message: Expected = {expected_error_message}, Actual = {error_message}")


    @allure.step("Swag Labs logo should be displayed")
    def swag_labs_logo_should_be_displayed(self):
        try:
            swag_labs_logo = self.wait.until(EC.visibility_of_element_located(self._swag_labs_logo)).is_displayed()
            assert swag_labs_logo == True
        except TimeoutException as e:
            self.log.error(f"Swag Labs logo is not displayed")
            pytest.fail(f"Swag Labs logo is not displayed")


    @allure.step("Click hamburger menu")
    def click_hamburger_menu(self):
        burger_menu = self.wait.until(EC.element_to_be_clickable(self._burger_menu))
        burger_menu.click()


    # @allure.step("Verify hamburger menu list")
    # def verify_hamburger_menu_list(self, expected_hamburger_list):
    #     # global expected_element
    #     # global actual_element
    #     # expected_hamburger_list = ["All Items", "About", "Logout", "Reset App State"]
    #     actual_hamburger_list = self.wait.until(EC.visibility_of_all_elements_located(self._burger_menu_list))
    #     try:
    #         assert len(actual_hamburger_list) == len(expected_hamburger_list)
    #     except:
    #         pytest.fail(f"Hamburger menu list count does not matched. Actual Count = {len(actual_hamburger_list)}, "
    #                     f"Expected Count = {len(expected_hamburger_list)}")
    #
    #     try:
    #         for index, element in enumerate(actual_hamburger_list):
    #             expected_element = expected_hamburger_list[index]
    #             actual_element = element.text
    #             assert actual_element == expected_element
    #     except:
    #         pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")


    @allure.step("Verify hamburger menu list")
    def verify_hamburger_menu_list(self, expected_hamburger_list):
        actual_hamburger_list = self.wait.until(EC.visibility_of_all_elements_located(self._burger_menu_list))
        assert len(actual_hamburger_list) == len(expected_hamburger_list), \
            pytest.fail(f"Hamburger menu list count does not matched. Actual Count = "
                        f"{len(actual_hamburger_list)}, Expected Count = {len(expected_hamburger_list)}")

        for index, element in enumerate(actual_hamburger_list):
            expected_element = expected_hamburger_list[index]
            actual_element = element.text
            assert actual_element == expected_element, \
                pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")

    # pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")








