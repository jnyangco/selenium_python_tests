import allure
import logging
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.config_reader import read_config as data
import time


@allure.feature("Login")
class TestTemplate:

    @allure.title("Valid Login Test")
    @allure.description("Test Login with valid credentials")
    def test_template_appname(self, driver, config):
        """Test login with valid credentials"""
        log = logging.getLogger(__name__)

        log.info("Starting test: test_saucedemo_valid_login")
        login_page = LoginPageSaucedemo(driver)

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login using username and password")
        username = data("saucedemo", "username")
        password = data("saucedemo", "password")
        login_page.login(username, password)
        # time.sleep(10)

        log.info("Step: Swag Labs logo should be displayed")
        login_page.user_successfully_logged_in()

