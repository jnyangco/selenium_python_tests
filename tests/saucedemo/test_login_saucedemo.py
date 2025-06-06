import allure
import logging
import inspect
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
import time
from base.base_test import BaseTest


@allure.feature("Login")
class TestLoginSaucedemo(BaseTest):

    @allure.title("Valid Login Test")
    @allure.description("Test description: Test Login with valid credentials")
    def test_login_valid_credentials(self, driver, config):
        """Test login with valid credentials"""

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)

        self.log.info("Step: User is successfully logged in")
        login_page.user_successfully_logged_in()


    @allure.title("Invalid Login Test - Invalid Password")
    @allure.description("Test description: Test Login with invalid password secret_sauce78234")
    def test_login_invalid_password(self, driver, config):
        """Test login with valid credentials"""

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        login_page.login(username, "secret 78234349")

        self.log.info("Step: Verify error message is displayed")
        login_page.verify_invalid_login_error_message("Epic sadface: Username and password do not match any user in this service")


    @allure.title("Invalid Login Test - Locked Out User")
    @allure.description("Test description: Invalid Login Test - Locked Out User")
    def test_login_locked_out_user(self, driver, config):
        """Test login with valid credentials"""

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login using username and password")
        username = data("saucedemo", "locked_out_user")
        password = data("saucedemo", "locked_out_password")
        login_page.login(username, password)

        self.log.info("Step: Verify error message is displayed")
        login_page.verify_invalid_login_error_message("Epic sadface: Sorry, this user has been locked out.")



