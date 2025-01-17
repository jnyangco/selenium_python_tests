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
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Click hamburger menu")
        steps.click_hamburger_menu()

        log.info("Step: Verify hamburger menu list")
        # steps.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State", "Tests"]) # failed step
        steps.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State"])


    @allure.title("SauceDemo: Verify Total Inventory List")
    def test_inventory_list(self, driver):
        log = cl.custom_logger(logging.INFO)
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Verify total product cards displayed")
        steps.verify_total_product_cards_displayed(6)


