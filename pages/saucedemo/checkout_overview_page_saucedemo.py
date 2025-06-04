import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class CheckoutOverviewPageSaucedemo(BasePage):

    # Locators
    _finish_button = (By.XPATH, "//button[@id='finish']")
    _item_total = (By.XPATH, "//div[@class='summary_subtotal_label']")
    _tax = (By.XPATH, "//div[@class='summary_tax_label']")
    _total = (By.XPATH, "//div[@class='summary_total_label']")
    _secondary_header_text = (By.XPATH, "//div[@data-test='secondary-header']/span")
    _cart_item_list_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']"
    _cart_item_quantity_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../../div[@class='cart_quantity']"
    _cart_item_price_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../..//div[@class='inventory_item_price']"


    @allure.step("Verify secondary header text")
    def verify_secondary_header_text(self, expected_secondary_text):
        try:
            actual_secondary_text = self.wait.until(EC.visibility_of_element_located(self._secondary_header_text)).text
            assert actual_secondary_text == expected_secondary_text, \
                f"Secondary header text mismatch: Expected = '{expected_secondary_text}', Actual = '{actual_secondary_text}'"
        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to verify secondary header text.")
            raise


    @allure.step("Verify item displayed in cart page - item name and quantity")
    def verify_item_quantity(self, item_name, expected_item_quantity):
        try:
            actual_item_quantity = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._cart_item_quantity_dynamic_xpath.format(item_name)))).text
            assert int(actual_item_quantity) == expected_item_quantity, \
                f"Incorrect item quantity for '{item_name}': Expected = '{expected_item_quantity}', Actual = '{actual_item_quantity}'"
        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to verify item name and quantity.")
            raise


    @allure.step("Verify item price")
    def verify_item_price(self, item_name, expected_item_price):
        try:
            actual_item_price = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._cart_item_price_dynamic_xpath.format(item_name)))).text
            actual_item_price = actual_item_price.replace("$", "")
            assert actual_item_price == expected_item_price, \
                f"Incorrect item price: Expected: {expected_item_price}, Actual: {actual_item_price}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to verify item price.")
            raise


    @allure.step("Click Finish Button")
    def click_finish_button(self):
        try:
            finish_button = self.wait.until(EC.element_to_be_clickable(self._finish_button))
            finish_button.click()
        except TimeoutException:
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to click Finish button.")
            pytest.fail("Failed to click Finish button.")


    @allure.step("Verify Item Total")
    def verify_item_total(self, price1, price2=0, price3=0, price4=0):
        try:
            expected_item_total = price1 + price2 + price3 + price4
            actual_item_total = self.wait.until(EC.visibility_of_element_located(self._item_total)).text
            actual_item_total = actual_item_total.split("$")
            print(f">>> expected_item_total = {expected_item_total}")
            print(f">>> actual_item_total = {actual_item_total[1]}")
            assert float(actual_item_total[1]) == expected_item_total, \
                f"Incorrect Item Total: Expected = {expected_item_total}, Actual = {actual_item_total}"

            tax = self.wait.until(EC.visibility_of_element_located(self._tax)).text
            tax = tax.split("$")
            expected_total = float(actual_item_total[1]) + float(tax[1])

            actual_total = self.wait.until(EC.visibility_of_element_located(self._total)).text
            actual_total = actual_total.split("$")
            print(f">>> expected_total = {expected_total}")
            print(f">>> actual_total[1] = {actual_total[1]}")
            assert float(actual_total[1]) == expected_total, \
                f"Incorrect Total: Expected = {expected_total}, Actual = {actual_total}"

        except (TimeoutException, AssertionError):
            self.screenshot_util.take_screenshot()
            self.log.error("Failed to verify item total.")
            raise

    # @allure.step("Compute Item Total")
    # def compute_item_total(self):
    #     try:
    #         item_total = float(self.item_price_1) + float(self.item_price_2)
    #         return item_total
    #     except TimeoutException:
    #         self.screenshot_util.take_screenshot()
    #         self.log.error("Failed to compute item total.")
    #         pytest.fail("Failed to compute item total.")
    #         return None






