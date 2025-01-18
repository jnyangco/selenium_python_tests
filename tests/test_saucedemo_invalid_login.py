import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage
from utils.config_reader import read_config as data


class TestSauceDemoInvalidLogin:

    @allure.title("SauceDemo: Invalid Login using Incorrect Password")
    def test_saucedemo_invalid_login_incorrect_password(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_saucedemo_invalid_login_incorrect_password")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        time.sleep(1)

        log.info("Step: Enter user and invalid password and click login button")
        steps.enter_username_and_password("standard_user", "secret_sauce78234")
        steps.click_login_button()
        time.sleep(2)

        log.info("Step: Verify the error message")
        steps.verify_invalid_login_error_message("Epic sadface: Username and password do not match any user in this service")


    @allure.title("SauceDemo: Invalid login using locked out user")
    def test_saucedemo_invalid_login_locked_out_user(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_saucedemo_invalid_login_incorrect_password")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        time.sleep(1)

        log.info("Step: Enter locked out user and click login button")
        username = data("saucedemo", "locked_out_user")
        password = data("saucedemo", "locked_out_password")
        steps.enter_username_and_password(username, password)
        steps.click_login_button()
        time.sleep(2)

        log.info("Step: Verify the error message")
        steps.verify_invalid_login_error_message("Epic sadface: Sorry, this user has been locked out.")

