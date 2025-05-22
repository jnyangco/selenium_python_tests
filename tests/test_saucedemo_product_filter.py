import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo.saucedemo_page import SauceDemoPage


class TestSauceDemoProductFilter:

    @allure.title("SauceDemo: Verify Product Cards in Ascending Order")
    def test_product_filter_ascending(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_product_filter_ascending")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(2)

        log.info("Step: Select dropdown filter 'Name (A to Z)'")
        steps.select_dropdown_filter("Name (A to Z)")
        time.sleep(1)

        log.info("Step: Verify product cards in ascending order")
        steps.verify_product_cards_ordering("ascending")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards in Descending Order")
    def test_product_filter_descending(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_product_filter_descending")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(2)

        log.info("Step: Select dropdown filter 'Name (Z to A)'")
        steps.select_dropdown_filter("Name (Z to A)")
        time.sleep(1)

        log.info("Step: Verify product cards in descending order")
        steps.verify_product_cards_ordering("descending")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards Order Price Low to High")
    def test_product_filter_price_low_to_high(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_product_filter_price_low_to_high")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(2)

        log.info("Step: Select dropdown filter 'Price (low to high)'")
        steps.select_dropdown_filter("Price (low to high)")
        time.sleep(1)

        log.info("Step: Verify product cards order Price low to high")
        steps.verify_product_cards_ordering("Price low to high")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards Order Price High to Low")
    def test_product_filter_price_high_to_low(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_product_filter_price_high_to_low")
        steps = SauceDemoPage(driver)

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(2)

        log.info("Step: Select dropdown filter 'Price (high to low)'")
        steps.select_dropdown_filter("Price (high to low)")
        time.sleep(1)

        log.info("Step: Verify product cards order Price low to high")
        steps.verify_product_cards_ordering("Price high to low")
        time.sleep(2)

