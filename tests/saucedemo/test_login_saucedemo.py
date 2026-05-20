import allure
import pytest
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.saucedemo
@pytest.mark.login
@allure.feature("Saucedemo: Login")
class TestLoginSaucedemo:

    @allure.title("Saucedemo: Valid Login Test")
    @allure.description("Test description: Test Login with valid credentials")
    def test_login_valid_credentials(self, driver, config):
        """Test login with valid credentials"""
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)

        log.info("Step: Verify user is logged in")
        assert login_page.is_logged_in(), f"User failed to login"


    @allure.title("Saucedemo: Invalid Login Test - Invalid Password")
    @allure.description("Test description: Test Login with invalid password secret_sauce78234")
    def test_login_invalid_password(self, driver, config):
        """Test login with valid credentials"""
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        login_page.login(username, "secret 78234349")

        log.info("Step: Verify error message is displayed")
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = login_page.get_error_message()
        assert actual_message == expected_message, (f"Incorrect error message: Expected '{expected_message}', "
                                                    f"but found '{actual_message}'")


    @allure.title("Saucedemo: Invalid Login Test - Locked Out User")
    @allure.description("Test description: Invalid Login Test - Locked Out User")
    def test_login_locked_out_user(self, driver, config):
        """Test login with valid credentials"""
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login using username and password")
        username = data("saucedemo", "locked_out_user")
        password = data("saucedemo", "locked_out_password")
        login_page.login(username, password)

        log.info("Step: Verify error message is displayed")
        expected_message = "Epic sadface: Sorry, this user has been locked out."
        actual_message = login_page.get_error_message()
        assert actual_message == expected_message, (f"Incorrect error message: Expected '{expected_message}', "
                                                    f"but found '{actual_message}'")






