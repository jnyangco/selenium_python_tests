import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoInvalidLogin:

    @allure.title("SauceDemo: Invalid Login using Incorrect Password")
    def test_saucedemo_invalid_login_incorrect_password(self, driver):
        log = cl.custom_logger(logging.INFO)
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.enter_username_and_password("standard_user", "secret_sauce78234")
        steps.click_login_button()

        log.info("Step: Verify the error message")
        steps.verify_invalid_login_error_message("Epic sadface: Username and password do not match any user in this service")


    @allure.title("SauceDemo: Invalid login using locked out user")
    def test_saucedemo_invalid_login_locked_out_user(self, driver):
        log = cl.custom_logger(logging.INFO)
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.enter_username_and_password("locked_out_user", "secret_sauce")
        steps.click_login_button()

        log.info("Step: Verify the error message")
        steps.verify_invalid_login_error_message("Epic sadface: Sorry, this user has been locked out.")

