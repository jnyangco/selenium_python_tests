import allure
import time

import utils.custom_logger as cl
import logging
from conftest import driver
from pages.orangehrm_page import OrangeHrmPage
from utils.config_reader import read_config as data


class TestOrangeHrmLogin:

    @allure.title("OrangeHrm: Valid Login")
    def test_orangehrm_valid_login(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_orangehrm_valid_login")
        steps = OrangeHrmPage(driver)

        log.info("Step: Open the OrangeHrm website")
        steps.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        steps.login_with_username_and_password(username, password)

        log.info("Step: User is landed on dashboard page")
        steps.user_landed_on_dashboard_page()
        time.sleep(2)




