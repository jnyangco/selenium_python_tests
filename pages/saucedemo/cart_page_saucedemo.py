import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from core.base.base_page import BasePage


class CartPageSaucedemo(BasePage):

    # Locators
    _secondary_header_text = (By.XPATH, "//div[@data-test='secondary-header']/span")
    _cart_item_list_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']"
    _cart_item_quantity_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../../div[@class='cart_quantity']"
    _cart_item_price_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../..//div[@class='inventory_item_price']"
    _checkout_button = (By.XPATH, "//button[@id='checkout']")
    _cart_total_text = (By.XPATH, "//div[@id='shopping_cart_container']//span")
    _continue_button = (By.XPATH, "//input[@id='continue']")


    @allure.step("Get item price - Cart Page")
    def get_item_price(self, item_name):
        try:
            item_price = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._cart_item_price_dynamic_xpath.format(item_name)))).text
            item_price = item_price.replace("$", "")
            return item_price
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to get item price in the cart page.")
            pytest.fail("Failed to get item price in the cart page.")
            return None


    @allure.step("Verify item price")
    def verify_item_price(self, item_name, expected_item_price):
        try:
            actual_item_price = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._cart_item_price_dynamic_xpath.format(item_name)))).text
            actual_item_price = actual_item_price.replace("$", "")
            assert actual_item_price == expected_item_price, \
                f"Incorrect item price: Expected: {expected_item_price}, Actual: {actual_item_price}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify item price.")
            raise


    @allure.step("Verify item displayed in cart page - item name and quantity")
    def verify_item_quantity(self, item_name, expected_item_quantity):
        try:
            actual_item_quantity = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._cart_item_quantity_dynamic_xpath.format(item_name)))).text
            assert int(actual_item_quantity) == expected_item_quantity, \
                f"Incorrect item quantity for '{item_name}': Expected = {expected_item_quantity}, Actual = {actual_item_quantity}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify item displayed in cart page - item name and quantity.")
            raise


    @allure.step("Click Checkout button")
    def click_checkout_button(self):
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable(self._checkout_button))
            checkout_button.click()
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to click checkout button.")
            pytest.fail("Failed to click checkout button.")


    @allure.step("Verify secondary header text")
    def verify_secondary_header_text(self, expected_secondary_text):
        try:
            actual_secondary_text = self.wait.until(EC.visibility_of_element_located(self._secondary_header_text)).text
            assert actual_secondary_text == expected_secondary_text, \
                f"Incorrect secondary header text: Expected = '{expected_secondary_text}', Actual = '{actual_secondary_text}'"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify secondary header text.")
            raise









