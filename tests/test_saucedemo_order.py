import allure
import time
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.saucedemo_page import SauceDemoPage


class TestSauceDemoOrder:

    @allure.title("SauceDemo: Order One Product")
    def test_order_one_product(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting tests: test_order_item")
        steps = SauceDemoPage(driver)

        # variables
        item_name = "Sauce Labs Backpack"

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Add to cart the item 1")
        steps.add_to_cart_first_item(item_name)
        time.sleep(1)
        steps.add_to_cart_button_change_to_remove(item_name)

        log.info("Step: Verify cart total text")
        steps.verify_cart_total_text(1)
        steps.open_cart()
        time.sleep(2)

        log.info("Step: Verify items are added in the cart")
        steps.verify_secondary_header_text("Your Cart")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name, 1)

        log.info("Step: Click checkout button")
        steps.click_checkout_button()
        time.sleep(2)

        log.info("Step: Fillup checkout information")
        steps.verify_secondary_header_text("Checkout: Your Information")
        steps.fillup_checkout_information("QA", "Test", "12345")
        time.sleep(1)

        log.info("Step: Click continue button")
        steps.click_continue_button()
        time.sleep(2)

        log.info("Step: Verify total price in the cart")
        steps.verify_secondary_header_text("Checkout: Overview")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name, 1)

        log.info("Step: Click finish button")
        steps.click_finish_button()
        time.sleep(2)

        log.info("Step: Verify checkout success message")
        steps.verify_secondary_header_text("Checkout: Complete!")
        steps.verify_checkout_success_message_text("Thank you for your order!")
        steps.verify_checkout_success_message_description("Your order has been dispatched, and will arrive just "
                                                          "as fast as the pony can get there!")
        time.sleep(2)



    @allure.title("SauceDemo: Order Two Products")
    def test_order_two_products(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting tests: test_order_item")
        steps = SauceDemoPage(driver)

        # variables
        item_name1 = "Sauce Labs Backpack"
        item_name2 = "Sauce Labs Bike Light"

        log.info("Step: Login to website")
        steps.open_saucedemo_website()
        steps.login_with_username_and_password("standard_user", "secret_sauce")

        log.info("Step: Add to cart the item 1 and item 2")
        steps.add_to_cart_first_item(item_name1)
        steps.add_to_cart_second_item(item_name2)
        steps.add_to_cart_button_change_to_remove(item_name1)
        steps.add_to_cart_button_change_to_remove(item_name2)

        log.info("Step: Verify cart total text")
        steps.verify_cart_total_text(2)
        time.sleep(1)
        steps.open_cart()
        time.sleep(2)

        log.info("Step: Verify items are added in the cart")
        steps.verify_secondary_header_text("Your Cart")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name1, 1, "item one")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name2, 1, "item two")

        log.info("Step: Click checkout button")
        steps.click_checkout_button()
        time.sleep(1)

        log.info("Step: Fillup checkout information")
        steps.verify_secondary_header_text("Checkout: Your Information")
        steps.fillup_checkout_information("QA", "Test", "12345")
        time.sleep(1)

        log.info("Step: Click continue button")
        steps.click_continue_button()

        log.info("Step: Verify total price in the cart")
        steps.verify_secondary_header_text("Checkout: Overview")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name1, 1, "item one")
        steps.verify_item_name_quantity_and_price_displayed_in_cart_page(item_name2, 1, "item two")
        steps.verify_item_total()

        log.info("Step: Click finish button")
        steps.click_finish_button()
        time.sleep(2)

        log.info("Step: Verify checkout success message")
        steps.verify_secondary_header_text("Checkout: Complete!")
        steps.verify_checkout_success_message_text("Thank you for your order!")
        steps.verify_checkout_success_message_description("Your order has been dispatched, and will arrive just "
                                                          "as fast as the pony can get there!")
        time.sleep(2)









