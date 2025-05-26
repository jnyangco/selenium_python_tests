import allure
import time
import logging
import inspect
from conftest import driver
from pages.orangehrm.orangehrm_page import OrangeHrmPage
from utils.config_reader import read_config as data


class TestOrangeHrmLogin:

    @allure.title("OrangeHrm: Valid Login")
    def test_orangehrm_valid_login(self, driver):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
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




