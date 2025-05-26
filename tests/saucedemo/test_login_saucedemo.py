import allure
import logging
import inspect
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.config_reader import read_config as data
import time



@allure.feature("Login")
class TestLoginSaucedemo:

    @allure.title("Valid Login Test")
    @allure.description("Test description: Test Login with valid credentials")
    def test_login_valid_credentials(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)

        log.info("Step: User is successfully logged in")
        login_page.user_successfully_logged_in()


    @allure.title("Invalid Login Test - Invalid Password")
    @allure.description("Test description: Test Login with invalid password secret_sauce78234")
    def test_login_invalid_password(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        login_page.login(username, "secret 78234349")

        log.info("Step: Verify error message is displayed")
        login_page.verify_invalid_login_error_message("Epic sadface: Username and password do not match any user in this service")


    @allure.title("Invalid Login Test - Locked Out User")
    @allure.description("Test description: Invalid Login Test - Locked Out User")
    def test_login_locked_out_user(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "locked_out_user")
        password = data("saucedemo", "locked_out_password")
        login_page.login(username, password)

        log.info("Step: Verify error message is displayed")
        login_page.verify_invalid_login_error_message("Epic sadface: Sorry, this user has been locked out.")



