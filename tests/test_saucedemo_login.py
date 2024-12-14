import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoUI:

    @allure.title("Test Case: SauceDemo Valid Login")
    def test_saucedemo_valid_login(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting tests: test_saucedemo_valid_login")
        steps = SauceDemoPage(driver)

        log.info("Open SauceDemo Website")
        steps.open_saucedemo_website()

        log.info("Login using username and password")
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Swag Labs logo should be displayed")
        steps.swag_labs_logo_should_be_displayed()



