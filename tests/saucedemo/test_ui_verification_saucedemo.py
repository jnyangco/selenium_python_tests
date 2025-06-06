import allure
import logging
import inspect
from conftest import driver
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from pages.saucedemo.product_page_saucedemo import ProductPageSaucedemo
from utils.data_utils import get_data as data
from base.base_test import BaseTest


@allure.feature("User Interface")
class TestUIVerificationSaucedemo(BaseTest):

    @allure.title("SauceDemo: Verify Hamburger List")
    def test_hamburger_menu_list(self, driver, config):

        self.log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        self.log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        self.log.info("Step: Click hamburger menu")
        product_page = ProductPageSaucedemo(driver)
        product_page.click_hamburger_menu()

        self.log.info("Step: Verify hamburger menu list")
        product_page.verify_hamburger_menu_list(["All Items", "About", "Logout", "Reset App State"])


    @allure.title("SauceDemo: Verify Total Product Cards Displayed")
    def test_total_product_cards_displayed(self, driver, config):

        self.log.info("Step: Login to website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))
        login_page.login("standard_user", "secret_sauce")

        self.log.info("Step: Verify total product cards displayed")
        products_page = ProductPageSaucedemo(driver)
        products_page.verify_total_product_cards_displayed(6)

