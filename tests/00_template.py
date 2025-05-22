import allure
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo


class Template:

    @allure.title("Test Case: Template")
    def template(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting tests: template")
        steps = LoginPageSaucedemo(driver)

        log.info("Open SauceDemo Website")
        steps.open_saucedemo_website()

        log.info("Login using username and password")
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Swag Labs logo should be displayed")
        steps.swag_labs_logo_should_be_displayed()

