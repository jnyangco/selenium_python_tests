import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoUIVerification:

    @allure.title("Test Case: Sauce Demo Hamburger List")
    def test_hamburger_menu_list(self, driver):
        log = cl.custom_logger(logging.INFO)
        steps = SauceDemoPage(driver)
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        steps.click_hamburger_menu()
        steps.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State", "Test"])


