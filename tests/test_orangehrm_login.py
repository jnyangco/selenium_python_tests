import allure
import time

import utils
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.orangehrm_page import OrangeHrmPage
from pages.saucedemo_page import SauceDemoPage


class TestOrangeHrmLogin:

    @allure.title("OrangeHrm: Valid Login")
    def test_orangehrm_valid_login(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_orangehrm_valid_login")
        steps = OrangeHrmPage(driver)

        log.info("Step: Login to website")
        steps.open_orangehrm_website()
        steps.login_with_username_and_password("Admin", "admin123")
        time.sleep(2)




