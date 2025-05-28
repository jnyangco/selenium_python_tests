import allure
import logging
import inspect

from pages.orangehrm.dashboard_page_orangehrm import DashboardPageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.config_reader import read_config as data
import time


@allure.feature("Login")
class TestLoginOrangehrm:

    @allure.title("OrangeHrm: Valid Login")
    def test_valid_login_orangehrm(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageOrangehrm(driver)

        log.info("Step: Open the OrangeHrm website")
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        log.info("Step: User is landed on dashboard page")
        dashboard_page = DashboardPageOrangehrm(driver)
        dashboard_page.user_landed_on_dashboard_page()
        time.sleep(2)


    @allure.title("OrangeHrm: Error message should show up when using invalid password")
    def test_invalid_password_orangehrm(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageOrangehrm(driver)

        log.info("Step: Open the OrangeHrm website")
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and incorrect password")
        username = data("orangehrm", "username")
        password = "Password#%&!3278"
        login_page.login_with_username_and_password(username, password)

        log.info("Step: Verify error message is displayed.")
        login_page.show_login_error_message("Invalid credentials")
        time.sleep(2)




