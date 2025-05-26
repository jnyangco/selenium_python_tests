import allure
import time
import logging
import inspect
from conftest import driver
from pages.saucedemo.cart_page_saucedemo import CartPageSaucedemo
from pages.saucedemo.checkout_complete_page_saucedemo import CheckoutCompletePageSaucedemo
from pages.saucedemo.checkout_information_page_saucedemo import CheckoutInformationPageSaucedemo
from pages.saucedemo.checkout_overview_page_saucedemo import CheckoutOverviewPageSaucedemo
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from pages.saucedemo.product_page_saucedemo import ProductPageSaucedemo
from utils.config_reader import read_config as data


@allure.feature("Order")
class TestOrderSaucedemo:

    @allure.title("SauceDemo: Order One Product")
    def test_order_one_product(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageSaucedemo(driver)

        # variables
        item_name = "Sauce Labs Backpack"

        log.info("Step: Open SauceDemo Website")
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(5)

        log.info("Step: Add to cart the item 1")
        product_page = ProductPageSaucedemo(driver)
        product_page.add_to_cart_first_item(item_name)
        time.sleep(1)
        product_page.add_to_cart_button_change_to_remove(item_name)

        log.info("Step: Verify cart total text")
        product_page.verify_cart_total_text(1)
        product_page.open_cart()
        time.sleep(2)

        log.info("Step: Verify items are added in the cart")
        cart_page = CartPageSaucedemo(driver)
        cart_page.verify_secondary_header_text("Your Cart")
        cart_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name, 1)
        #
        # log.info("Step: Click checkout button")
        # cart_page.click_checkout_button()
        # time.sleep(2)
        #
        # log.info("Step: Fillup checkout information")
        # checkout_information_page = CheckoutInformationPageSaucedemo(driver)
        # checkout_information_page.verify_secondary_header_text("Checkout: Your Information")
        # checkout_information_page.fillup_checkout_information("QA", "Test", "12345")
        # time.sleep(1)
        #
        # log.info("Step: Click continue button")
        # checkout_information_page.click_continue_button()
        # time.sleep(2)
        #
        # log.info("Step: Verify total price in the cart")
        # checkout_overview_page = CheckoutOverviewPageSaucedemo(driver)
        # checkout_overview_page.verify_secondary_header_text("Checkout: Overview")
        # checkout_overview_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name, 1)
        #
        # log.info("Step: Click finish button")
        # checkout_overview_page.click_finish_button()
        # time.sleep(2)
        #
        # log.info("Step: Verify checkout success message")
        # checkout_complete_page = CheckoutCompletePageSaucedemo(driver)
        # checkout_complete_page.verify_secondary_header_text("Checkout: Complete!")
        # checkout_complete_page.verify_checkout_success_message_text("Thank you for your order!")
        # checkout_complete_page.verify_checkout_success_message_description("Your order has been dispatched, and will arrive just "
        #                                                   "as fast as the pony can get there!")
        # time.sleep(2)



    @allure.title("SauceDemo: Order Two Products")
    def test_order_two_products(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        steps = LoginPageSaucedemo(driver)

        # variables
        item_name1 = "Sauce Labs Backpack"
        item_name2 = "Sauce Labs Bike Light"

        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open_url(data("saucedemo", "base_url"))

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Add to cart the item 1 and item 2")
        product_page = ProductPageSaucedemo(driver)
        product_page.add_to_cart_first_item(item_name1)
        product_page.add_to_cart_second_item(item_name2)
        product_page.add_to_cart_button_change_to_remove(item_name1)
        product_page.add_to_cart_button_change_to_remove(item_name2)

        log.info("Step: Verify cart total text")
        product_page.verify_cart_total_text(2)
        time.sleep(1)
        product_page.open_cart()
        time.sleep(2)

        log.info("Step: Verify items are added in the cart")
        cart_page = CartPageSaucedemo(driver)
        cart_page.verify_secondary_header_text("Your Cart")
        cart_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name1, 1, "item one")
        cart_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name2, 1, "item two")

        log.info("Step: Click checkout button")
        cart_page.click_checkout_button()
        time.sleep(1)

        log.info("Step: Fillup checkout information")
        checkout_page_information = CheckoutInformationPageSaucedemo(driver)
        checkout_page_information.verify_secondary_header_text("Checkout: Your Information")
        checkout_page_information.fillup_checkout_information("QA", "Test", "12345")
        time.sleep(1)

        log.info("Step: Click continue button")
        checkout_page_information.click_continue_button()

        log.info("Step: Verify total price in the cart")
        checkout_overview_page = CheckoutOverviewPageSaucedemo(driver)
        checkout_overview_page.verify_secondary_header_text("Checkout: Overview")
        checkout_overview_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name1, 1, "item one")
        checkout_overview_page.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name2, 1, "item two")
        checkout_overview_page.verify_item_total()

        log.info("Step: Click finish button")
        checkout_overview_page.click_finish_button()
        time.sleep(2)

        log.info("Step: Verify checkout success message")
        checkout_complete_page = CheckoutCompletePageSaucedemo(driver)
        checkout_complete_page.verify_secondary_header_text("Checkout: Complete!")
        checkout_complete_page.verify_checkout_success_message_text("Thank you for your order!")
        checkout_complete_page.verify_checkout_success_message_description("Your order has been dispatched, and will arrive just "
                                                          "as fast as the pony can get there!")
        time.sleep(2)









