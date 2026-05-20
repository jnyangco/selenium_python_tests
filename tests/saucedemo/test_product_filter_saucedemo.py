import allure
import time
import pytest
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from pages.saucedemo.product_page_saucedemo import ProductPageSaucedemo
from utils.data_utils import get_data as data
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.saucedemo
@pytest.mark.filter
@allure.feature("Saucedemo: Filter")
class TestProductFilterSaucedemo:

    @allure.title("SauceDemo: Verify Product Cards in Ascending Order")
    def test_product_filter_ascending(self, driver, config):
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Select dropdown filter 'Name (A to Z)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Name (A to Z)")

        log.info("Step: Verify product cards in ascending order")
        # product_page.verify_product_cards_ordering("ascending")
        actual_names = product_page.get_product_card_names()
        expected_names = sorted(actual_names)
        assert actual_names == expected_names, (f"Incorrect product cards order. "
                                                f"Expected ascending order {expected_names}, but found {actual_names}")


    @allure.title("SauceDemo: Verify Product Cards in Descending Order")
    def test_product_filter_descending(self, driver, config):
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Select dropdown filter 'Name (Z to A)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Name (Z to A)")

        log.info("Step: Verify product cards in descending order")
        # product_page.verify_product_cards_ordering("descending")
        actual_names = product_page.get_product_card_names()
        expected_names = sorted(actual_names, reverse=True)
        assert actual_names == expected_names, (f"Incorrect product cards order. "
                                                f"Expected descending order {expected_names}, but found {actual_names}")


    @allure.title("SauceDemo: Verify Product Cards Order Price Low to High")
    def test_product_filter_price_low_to_high(self, driver, config):
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Select dropdown filter 'Price (low to high)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Price (low to high)")

        log.info("Step: Verify product cards order Price low to high")
        # product_page.verify_product_cards_ordering("Price low to high")
        actual_prices = product_page.get_product_prices()
        expected_prices = sorted(actual_prices)
        assert actual_prices == expected_prices, (f"Incorrect product price order. "
                                                f"Expected {expected_prices}, but found {actual_prices}")


    @allure.title("SauceDemo: Verify Product Cards Order Price High to Low")
    def test_product_filter_price_high_to_low(self, driver, config):
        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Select dropdown filter 'Price (high to low)'")
        product_page = ProductPageSaucedemo(driver)
        product_page.select_dropdown_filter("Price (high to low)")

        log.info("Step: Verify product cards order Price high to low")
        # product_page.verify_product_cards_ordering("Price high to low")
        actual_prices = product_page.get_product_prices()
        expected_prices = sorted(actual_prices, reverse=True)
        assert actual_prices == expected_prices, (f"Incorrect product price order. "
                                                f"Expected {expected_prices}, but found {actual_prices}")

