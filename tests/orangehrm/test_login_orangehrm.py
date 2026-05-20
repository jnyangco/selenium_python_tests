import allure
import pytest
from pages.orangehrm.dashboard_page_orangehrm import DashboardPageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.data_utils import get_data as data
import time
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.orangehrm
@pytest.mark.login
@allure.feature("Orangehrm: Login")
class TestLoginOrangehrm:

    @pytest.mark.single_test
    @allure.title("Orangehrm: User should be able to login using valid credentials")
    def test_valid_login_orangehrm(self, driver):
        """Test login with valid credentials"""

        log.info("Step: Login to Orangehrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.login()

        log.info("Step: User is landed on dashboard page")
        dashboard_page = DashboardPageOrangehrm(driver)
        dashboard_page.user_landed_on_dashboard_page()
        time.sleep(2)


    @allure.title("Orangehrm: Error message should show up when using invalid password")
    def test_invalid_password_orangehrm(self, driver):

        log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and incorrect password")
        username = data("orangehrm", "username")
        password = "Password#%&!3278"
        login_page.login_with_username_and_password(username, password)

        log.info("Step: Verify error message is displayed.")
        login_page.verify_login_error_message("Invalid credentials")
        time.sleep(2)




