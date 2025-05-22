import allure
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo.saucedemo_page import SauceDemoPage
from utils.config_reader import read_config as data

import time
import pytest

@allure.feature("Login")
class TestSauceDemoLogin:

    @allure.title("SauceDemo: Valid Login")
    @allure.description("Test Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_saucedemo_valid_login(self, driver):

        # saucedemopage = SauceDemoPage(driver)
        log = logging.getLogger(__name__)

        # log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_saucedemo_valid_login")
        steps = SauceDemoPage(driver)

        # steps.open_url(config.BASE_URL_SAUCEDEMO)
        steps.open_url("https://www.saucedemo.com/")


        # log.info("Step: Open SauceDemo Website")
        # steps.open_saucedemo_website()

        # log.info("Step: Login using username and password")
        # username = data("saucedemo", "standard_user")
        # password = data("saucedemo", "standard_password")
        # steps.login_with_username_and_password(username, password)

        log.info("Step: Login using username and password")
        # username = data("saucedemo", "standard_user")
        # password = data("saucedemo", "standard_password")
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(10)

        # log.info("Step: Swag Labs logo should be displayed")
        steps.swag_labs_logo_should_be_displayed()



