import allure
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo


class TestSauceDemoUIVerification:

    @allure.title("SauceDemo: Verify Hamburger List")
    def test_hamburger_menu_list(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_hamburger_menu_list")
        steps = LoginPageSaucedemo(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Click hamburger menu")
        steps.click_hamburger_menu()

        log.info("Step: Verify hamburger menu list")
        # steps.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State", "Tests"]) # failed step
        steps.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State"])


    @allure.title("SauceDemo: Verify Total Product Cards Displayed")
    def test_total_product_cards_displayed(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_total_product_cards_displayed")
        steps = LoginPageSaucedemo(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Verify total product cards displayed")
        steps.verify_total_product_cards_displayed(6)

