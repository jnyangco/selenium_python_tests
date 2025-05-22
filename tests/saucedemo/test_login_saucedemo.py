import allure
import logging
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.config_reader import read_config as data
import time


@allure.feature("Login")
class TestLoginSaucedemo:

    @allure.title("Valid Login Test")
    @allure.description("Test Login with valid credentials")
    def test_valid_login_saucedemo(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)

        log.info("Starting test: test_saucedemo_valid_login")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)
        time.sleep(10)

        log.info("Step: Swag Labs logo should be displayed")
        login_page.swag_labs_logo_should_be_displayed()


    @allure.title("Invalid Login Test")
    @allure.description("Test Login with invalid secret_sauce78234")
    def test_invalid_login_saucedemo(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)

        log.info("Starting test: test_saucedemo_valid_login")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        login_page.login(username, "secret 78234349")
        time.sleep(10)

        log.info("Step: Swag Labs logo should be displayed")
        # login_page.swag_labs_logo_should_be_displayed2()
        # login_page.is_element_displayed('test');
        login_page.is_swag_labs_logo_displayed()



