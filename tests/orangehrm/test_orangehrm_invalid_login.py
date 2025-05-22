import allure
import time

import utils.custom_logger as cl
import logging
from conftest import driver
from pages.orangehrm.orangehrm_page import OrangeHrmPage
from utils.config_reader import read_config as data


class TestOrangeHrmInvalidLogin:

    @allure.title("OrangeHrm: Error message should show up when using invalid password")
    def test_orangehrm_invalid_password(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_orangehrm_invalid_password")
        steps = OrangeHrmPage(driver)

        log.info("Step: Open the OrangeHrm website")
        steps.open_orangehrm_website()

        log.info("Step: Login using username and incorrect password")
        username = data("orangehrm", "username")
        password = "Password#%&!3278"
        steps.login_with_username_and_password(username, password)

        log.info("Step: Verify error message is displayed.")
        steps.show_login_error_message("Invalid credentials")
        time.sleep(2)




