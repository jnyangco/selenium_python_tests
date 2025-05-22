import allure
import logging
from conftest import driver
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.config_reader import read_config as data

import time

@allure.feature("Login")
class TestLoginSaucedemo:

    @allure.title("Saucedemo: Valid Login")
    @allure.description("Test Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login_saucedemo(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)
        log.info("Starting test: test_saucedemo_valid_login")

        # log = cl.custom_logger(logging.INFO)
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(config.BASE_URL_SAUCEDEMO)

        log.info("Step: Login using username and password")
        username = data("saucedemo", "standard_user")
        password = data("saucedemo", "standard_password")
        login_page.login_with_username_and_password(username, password)

        log.info("Step: Login using username and password")
        # username = data("saucedemo", "standard_user")
        # password = data("saucedemo", "standard_password")
        # login_page.login("standard_user", "secret_sauce")
        time.sleep(10)

        # log.info("Step: Swag Labs logo should be displayed")
        login_page.swag_labs_logo_should_be_displayed()



