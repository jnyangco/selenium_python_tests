import allure
import logging
import inspect

import pytest
from pages.orangehrm.dashboard_page_orangehrm import DashboardPageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.data_utils import get_data as data
import time
from base.base_test import BaseTest


@pytest.mark.orangehrm
@pytest.mark.login
@allure.feature("Login")
class TestLoginOrangehrm(BaseTest):

    @allure.title("OrangeHrm: Valid Login")
    def test_valid_login_orangehrm(self, driver):
        """Test login with valid credentials"""

        self.log.info("Step: Login to Orangehrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.login()

        self.log.info("Step: User is landed on dashboard page")
        dashboard_page = DashboardPageOrangehrm(driver)
        dashboard_page.user_landed_on_dashboard_page()
        time.sleep(2)


    @allure.title("OrangeHrm: Error message should show up when using invalid password")
    def test_invalid_password_orangehrm(self, driver):

        self.log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        self.log.info("Step: Login using username and incorrect password")
        username = data("orangehrm", "username")
        password = "Password#%&!3278"
        login_page.login_with_username_and_password(username, password)

        self.log.info("Step: Verify error message is displayed.")
        login_page.verify_login_error_message("Invalid credentials")
        time.sleep(2)




