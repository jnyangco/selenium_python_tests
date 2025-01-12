import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoOrder:

    @allure.title("SauceDemo: Order an Item")
    def test_order_item(self, driver):
        log = cl.custom_logger(logging.INFO)
        steps = SauceDemoPage(driver)

        # variables
        item_name = "Sauce Labs Backpack"

        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")
        time.sleep(2)
        steps.add_to_cart_item(item_name)
        time.sleep(1)
        steps.add_to_cart_button_change_to_remove(item_name)
        steps.verify_cart_total_text(1)
        steps.open_cart()
        time.sleep(2)

        steps.verify_item_displayed_in_cart_page(item_name, 1)
        steps.click_checkout_button()
        time.sleep(5)






