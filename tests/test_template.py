import allure
import pytest
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.saucedemo
@pytest.mark.login
@allure.feature("Test: Login")
class TestTemplate:

    @allure.title("Test: Valid Login Test")
    @allure.description("Test description: Test Login with valid credentials")
    def test_valid_login(self, driver):
        """Test login with valid credentials"""

        log.info("Step: Open Test Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)

        log.info("Step: User is successfully logged in")
        login_page.user_successfully_logged_in()