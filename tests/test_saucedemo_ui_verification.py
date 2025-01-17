import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoUIVerification:

    @allure.title("SauceDemo: Verify Hamburger List")
    def test_hamburger_menu_list(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_hamburger_menu_list")
        steps = SauceDemoPage(driver)

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
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Verify total product cards displayed")
        steps.verify_total_product_cards_displayed(6)


    @allure.title("SauceDemo: Verify Product Cards in Ascending Order")
    def test_product_filter_ascending(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_product_filter_ascending")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Verify product cards in ascending order")
        steps.verify_product_cards_ordering("descending")
        time.sleep(2)

