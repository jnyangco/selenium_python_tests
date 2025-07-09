import allure
import pytest
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.saucedemo
@pytest.mark.login
@allure.feature("Saucedemo: Login")
class TestTemplate(BaseTest):

    @allure.title("Saucedemo: Valid Login Test")
    @allure.description("Test description: Test Login with valid credentials")
    def test_valid_login(self, driver):
        """Test login with valid credentials"""

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)

        self.log.info("Step: User is successfully logged in")
        login_page.user_successfully_logged_in()