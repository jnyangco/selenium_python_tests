import allure
import time
import logging
import inspect
from conftest import driver
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from pages.saucedemo.product_page_saucedemo import ProductPageSaucedemo
from utils.data_utils import get_data as data
from base.base_test import BaseTest


@allure.feature("Filter")
class TestProductFilterSaucedemo(BaseTest):

    @allure.title("SauceDemo: Verify Product Cards in Ascending Order")
    def test_product_filter_ascending(self, driver, config):
        login_page = LoginPageSaucedemo(driver)

        self.log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

        self.log.info("Step: Select dropdown filter 'Name (A to Z)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Name (A to Z)")
        time.sleep(1)

        self.log.info("Step: Verify product cards in ascending order")
        product_page.verify_product_cards_ordering("ascending")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards in Descending Order")
    def test_product_filter_descending(self, driver, config):

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

        self.log.info("Step: Select dropdown filter 'Name (Z to A)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Name (Z to A)")
        time.sleep(1)

        self.log.info("Step: Verify product cards in descending order")
        product_page.verify_product_cards_ordering("descending")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards Order Price Low to High")
    def test_product_filter_price_low_to_high(self, driver, config):

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

        self.log.info("Step: Select dropdown filter 'Price (low to high)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Price (low to high)")
        time.sleep(1)

        self.log.info("Step: Verify product cards order Price low to high")
        product_page.verify_product_cards_ordering("Price low to high")
        time.sleep(2)


    @allure.title("SauceDemo: Verify Product Cards Order Price High to Low")
    def test_product_filter_price_high_to_low(self, driver, config):

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

        self.log.info("Step: Select dropdown filter 'Price (high to low)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Price (high to low)")
        time.sleep(1)

        self.log.info("Step: Verify product cards order Price low to high")
        product_page.verify_product_cards_ordering("Price high to low")
        time.sleep(2)

