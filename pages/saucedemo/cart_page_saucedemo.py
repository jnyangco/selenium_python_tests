import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver
# from base.selenium_driver import SeleniumDriver
# from utils import custom_logger as cl
import logging
from base.base_page import BasePage
# from utils.report_status import ReportStatus


class CartPageSaucedemo(BasePage):

    # Variables
    item_price_1 = 0
    item_price_2 = 0

    # Locators
    _secondary_header_text = (By.XPATH, "//div[@data-test='secondary-header']/span")
    _cart_item_list_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']"
    _cart_item_quantity_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../../div[@class='cart_quantity']"
    _cart_item_price_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../..//div[@class='inventory_item_price']"
    _checkout_button = (By.XPATH, "//button[@id='checkout']")

    _cart_total_text = (By.XPATH, "//div[@id='shopping_cart_container']//span")

    # # Checkout: Information
    # _first_name_info = (By.XPATH, "//input[@id='first-name']")
    # _last_name_info = (By.XPATH, "//input[@id='last-name']")
    # _zip_code_info = (By.XPATH, "//input[@id='postal-code']")
    # _continue_button = (By.XPATH, "//input[@id='continue']")
    #
    # # Checkout: Overview
    # _finish_button = (By.XPATH, "//button[@id='finish']")
    # _item_total = (By.XPATH, "//div[@class='summary_subtotal_label']")
    # _tax = (By.XPATH, "//div[@class='summary_tax_label']")
    # _total = (By.XPATH, "//div[@class='summary_total_label']")
    #
    # # Checkout: Complete
    # _checkout_success_message_text = (By.XPATH, "//h2[@class='complete-header']")
    # _checkout_success_message_description = (By.XPATH, "//div[@class='complete-text']")
    # _back_home_button = (By.XPATH, "//button[@id='back-to-products']")





    @allure.step("Verify item displayed in cart page - item name and quantity")
    def verify_item_name_quantity_and_price_displayed_in_cart_page(self, item_name, expected_item_quantity, item_number="item one"):
        if item_number == 'item one':
            print(f">>> IF -> item_number = {item_number}")
            expected_item_price = self.item_price_1
        else:
            print(f">>> ELSE -> item_number = {item_number}")
            expected_item_price = self.item_price_2

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_list_dynamic_xpath.format(item_name))))

        except TimeoutException:
            pytest.fail(f"Element not visible. Expected = 'True', Actual = 'False'")

        actual_item_price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_price_dynamic_xpath.format(item_name)))).text
        actual_item_price = actual_item_price.replace("$", "")
        assert actual_item_price == expected_item_price, pytest.fail(f"Incorrect item price. Expected = {expected_item_price}, Actual = {actual_item_price}")

        actual_item_quantity = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_quantity_dynamic_xpath.format(item_name)))).text
        assert int(actual_item_quantity) == expected_item_quantity, pytest.fail(f"Incorrect item quantity for '{item_name}'. Expected = {expected_item_quantity}, Actual = {actual_item_quantity}")


    @allure.step("Click Checkout button")
    def click_checkout_button(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(self._checkout_button))
        checkout_button.click()


    def click_continue_button(self):
        continue_button = self.wait.until(EC.element_to_be_clickable(self._continue_button))
        continue_button.click()


    @allure.step("Verify secondary header text")
    def verify_secondary_header_text(self, expected_secondary_text):
        actual_secondary_text = self.wait.until(EC.visibility_of_element_located(self._secondary_header_text)).text
        assert actual_secondary_text == expected_secondary_text, pytest.fail(f"Incorrect secondary header text. Expected = {expected_secondary_text}, Actual = {actual_secondary_text}")


    @allure.step("Fillup Checkout Information")
    def fillup_checkout_information(self, first_name, last_name, zip_code):
        first_name_element = self.wait.until(EC.visibility_of_element_located(self._first_name_info))
        first_name_element.send_keys(first_name)
        last_name_element = self.wait.until(EC.element_to_be_clickable(self._last_name_info))
        last_name_element.send_keys(last_name)
        zip_code_element = self.wait.until(EC.element_to_be_clickable(self._zip_code_info))
        zip_code_element.send_keys(zip_code)


    @allure.step("Click Finish Button")
    def click_finish_button(self):
        finish_button = self.wait.until(EC.element_to_be_clickable(self._finish_button))
        finish_button.click()


    @allure.step("Verify Item Total")
    def verify_item_total(self):
        expected_item_total = self.compute_item_total()
        actual_item_total = self.wait.until(EC.visibility_of_element_located(self._item_total)).text
        actual_item_total = actual_item_total.split("$")
        print(f">>> expected_item_total = {expected_item_total}")
        print(f">>> actual_item_total = {actual_item_total[1]}")
        assert float(actual_item_total[1]) == expected_item_total, pytest.fail(f"Incorrect Item Total. Expected = {expected_item_total}, Actual = {actual_item_total}")

        tax = self.wait.until(EC.visibility_of_element_located(self._tax)).text
        tax = tax.split("$")
        expected_total = float(actual_item_total[1]) + float(tax[1])

        actual_total = self.wait.until(EC.visibility_of_element_located(self._total)).text
        actual_total = actual_total.split("$")
        print(f">>> expected_total = {expected_total}")
        print(f">>> actual_total[1] = {actual_total[1]}")
        assert float(actual_total[1]) == expected_total, pytest.fail(f"Incorrect Total. Expected = {expected_total}, Actual = {actual_total}")


    @allure.step("Compute Item Total")
    def compute_item_total(self):
        item_total = float(self.item_price_1) + float(self.item_price_2)
        return item_total


    @allure.step("Verify checkout success message text")
    def verify_checkout_success_message_text(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self._checkout_success_message_text)).text
        assert actual_text == expected_text, pytest.fail(f"FAILED: Incorrect checkout success message text. Expected = {expected_text}, Actual = {actual_text}")


    @allure.step("Verify checkout success message description")
    def verify_checkout_success_message_description(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self._checkout_success_message_description)).text
        assert actual_text == expected_text, pytest.fail(f"Incorrect checkout success message description. Expected = {expected_text}, Actual = {actual_text}")


    @allure.step("Verify product cards ordering")
    def verify_product_cards_ordering(self, order_type="ascending"): #default = ascending
        actual_product_list = []
        product_cards = self.wait.until(EC.visibility_of_all_elements_located(self._product_cards))
        print(f">>> product_cards = {product_cards}")

        actual_product_price = []
        product_price = self.wait.until(EC.visibility_of_all_elements_located(self._product_price))

        if order_type.lower() == "ascending":
            for product in product_cards:
                print(f">>> product = {product.text}")
                actual_product_list.append(product.text)
            expected_product_list = sorted(actual_product_list)
            print(f">>> actual_product_list = {actual_product_list}")
            print(f">>> expected_product_list = {expected_product_list}")
            assert actual_product_list == expected_product_list, pytest.fail(f"Product is not in ascending order: "
                                            f"Expected = \n{expected_product_list}, Actual = \n{actual_product_list}")

        elif order_type.lower() == "descending":
            for product in product_cards:
                print(f">>> product = {product.text}")
                actual_product_list.append(product.text)
            expected_product_list = sorted(actual_product_list, reverse=True)
            print(f">>> actual_product_list = {actual_product_list}")
            print(f">>> expected_product_list = {expected_product_list}")
            assert actual_product_list == expected_product_list, pytest.fail(f"Product is not in ascending order: "
                                            f"Expected = \n{expected_product_list}, Actual = \n{actual_product_list}")

        elif order_type.lower() == "price low to high":
            for price in product_price:
                price = float(price.text.replace("$",""))
                print(f">>> price = {price}")
                actual_product_price.append(price)

            expected_product_price = sorted(actual_product_price)
            print(f">>> actual_product_price = {actual_product_price}")
            print(f">>> expected_product_price = {expected_product_price}")
            assert actual_product_price == expected_product_price, pytest.fail(f"Product price is not in ascending order: "
                                            f"Expected = \n{expected_product_price}, Actual = \n{actual_product_price}")

        elif order_type.lower() == "price high to low":
            for price in product_price:
                price = float(price.text.replace("$",""))
                print(f">>> price = {price}")
                actual_product_price.append(price)

            expected_product_price = sorted(actual_product_price, reverse=True)
            print(f">>> actual_product_price = {actual_product_price}")
            print(f">>> expected_product_price = {expected_product_price}")
            assert actual_product_price == expected_product_price, pytest.fail(f"Product price is not in descending order: "
                                            f"Expected = \n{expected_product_price}, Actual = \n{actual_product_price}")


    @allure.step("Select dropdown filter")
    def select_dropdown_filter(self, sort_by):
        dropdown = self.wait.until(EC.visibility_of_element_located(self._filter_product))
        dropdown = Select(dropdown)
        dropdown.select_by_visible_text(sort_by)


    @allure.step("Verify cart total")
    def verify_cart_total_text(self, expected_total):
        cart_total_text = self.wait.until(EC.visibility_of_element_located(self._cart_total_text)).text
        assert int(cart_total_text) == expected_total, pytest.fail(f"Incorrect cart total. Expected = {expected_total}, Actual = {cart_total_text}")



    @allure.step("Verify item displayed in cart page - item name and quantity")
    def verify_item_name_quantity_and_price_displayed_in_cart_page(self, item_name, expected_item_quantity, item_number="item one"):
        if item_number == 'item one':
            expected_item_price = self.item_price_1
        else:
            expected_item_price = self.item_price_2

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_list_dynamic_xpath.format(item_name))))

        except TimeoutException:
            pytest.fail(f"Element not visible. Expected = 'True', Actual = 'False'")

        actual_item_price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_price_dynamic_xpath.format(item_name)))).text
        actual_item_price = actual_item_price.replace("$", "")
        assert actual_item_price == expected_item_price, pytest.fail(f"Incorrect item price. Expected = {expected_item_price}, Actual = {actual_item_price}")

        actual_item_quantity = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_quantity_dynamic_xpath.format(item_name)))).text
        assert int(actual_item_quantity) == expected_item_quantity, pytest.fail(f"Incorrect item quantity for '{item_name}'. Expected = {expected_item_quantity}, Actual = {actual_item_quantity}")








