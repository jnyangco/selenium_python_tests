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


class CheckoutCompletePageSaucedemo(BasePage):

    # Variables
    item_price_1 = 0
    item_price_2 = 0

    # Locators
    _checkout_success_message_text = (By.XPATH, "//h2[@class='complete-header']")
    _checkout_success_message_description = (By.XPATH, "//div[@class='complete-text']")
    _back_home_button = (By.XPATH, "//button[@id='back-to-products']")


    # ========================================================================
    # NEW
    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username, password):
        """Perform login action"""
        self.enter_text(self._username_textbox, username)
        self.enter_text(self._password_textbox, password)
        self.click_element(self._login_button)

    # @allure.step("Login with username: {username} and password: {password}")
    # def login_v2(self, username, password):
    #     """Perform login action"""
    #     username_textbox = self.find_web_element(self._username_textbox)
    #     username_textbox.send_keys(username)
    #     password_textbox = self.find_web_element(self._password_textbox)
    #     password_textbox.send_keys(password)
    #     self.click_element(self._login_button)

    @allure.step("Check if swag labs logo is displayed")
    def is_swag_labs_logo_displayed(self):
        try:
            assert self.is_element_displayed(self._swag_labs_logo)
        except Exception as e:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Swag labs logo is not displayed. \nError: {e}")
            pytest.fail(f"Swag labs logo is not displayed. \nError: {e}")


    @allure.step("Check if error message is displayed")
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_displayed(self.ERROR_MESSAGE)

    @allure.step("Get error message text")
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)





    # ========================================================================


    @allure.step("Open SauceDemo Website")
    def open_saucedemo_website(self):
        # self.driver.get(self.base_url)
        self.driver.get("https://www.google.com")


    @allure.step("Login using username - {username} and password - {password}")
    def login_with_username_and_password(self, username, password):
        try:
            username_textbox = self.wait.until(EC.visibility_of_element_located(self._username_textbox))
            username_textbox.send_keys(username)
            password_textbox = self.wait.until(EC.visibility_of_element_located(self._password_textbox))
            password_textbox.send_keys(password)
            login_button = self.wait.until(EC.element_to_be_clickable(self._login_button))
            login_button.click()
        except Exception as e:
            self.log.error(f"User is unable to login. Error -> {e}")
            pytest.fail(f"User is unable to login.")


    @allure.step("Enter username and password")
    def enter_username_and_password(self, username, password):
        try:
            username_textbox = self.wait.until(EC.visibility_of_element_located(self._username_textbox))
            username_textbox.send_keys(username)
            password_textbox = self.wait.until(EC.visibility_of_element_located(self._password_textbox))
            password_textbox.send_keys(password)
        except Exception as e:
            self.log.error(f"User is unable to enter username and password. Error -> {e}")
            pytest.fail(f"User is unable to enter username and password.")


    @allure.step("Click Login Button")
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self._login_button))
        login_button.click()


    @allure.step("Verify invalid login error message")
    def verify_invalid_login_error_message(self, expected_error_message):
        error_message = self.wait.until(EC.visibility_of_element_located(self._invalid_login_error_message)).text
        self.log.info(f"Actual Error Message = {error_message}")
        try:
            assert error_message == expected_error_message, \
                f"Incorrect error message: Expected = {expected_error_message}, Actual = {error_message}"
        except Exception:
            pytest.fail(f"Incorrect error message: Expected = {expected_error_message}, Actual = {error_message}")


    @allure.step("Swag Labs logo should be displayed")
    def swag_labs_logo_should_be_displayed(self):
        try:
            swag_labs_logo = self.wait.until(EC.visibility_of_element_located(self._swag_labs_logo)).is_displayed()
            assert swag_labs_logo == True
        except TimeoutException:
            self.log.error(f"Swag Labs logo is not displayed")
            self.screenshot_util.take_screenshot()
            pytest.fail(f"Swag Labs logo is not displayed")

            # self.log.error(f"Element not found: {locator}")
            # self.screenshot_util.take_screenshot("element_not_found")
            # self.screenshot_util.take_screenshot()
            # pytest.fail(f"Element not found: {locator}")
            # raise

    @allure.step("Swag Labs logo should be displayed")
    def swag_labs_logo_should_be_displayed2(self):
        swag_labs_logo_displayed = ""
        try:
            swag_labs_logo_displayed = self.is_element_displayed(self._swag_labs_logo)
            assert swag_labs_logo_displayed == True
        except TimeoutException:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Swag Labs logo not displayed: {swag_labs_logo_displayed}")
            pytest.fail(f"Swag Labs logo not displayed: {swag_labs_logo_displayed}")

            # self.log.error(f"Element not found: {locator}")
            # self.screenshot_util.take_screenshot("element_not_found")
            # self.screenshot_util.take_screenshot()
            # pytest.fail(f"Element not found: {locator}")
            # raise

    @allure.step("Click hamburger menu")
    def click_hamburger_menu(self):
        burger_menu = self.wait.until(EC.element_to_be_clickable(self._burger_menu))
        burger_menu.click()


    # @allure.step("Verify hamburger menu list")
    # def verify_hamburger_menu_list(self, expected_hamburger_list):
    #     # global expected_element
    #     # global actual_element
    #     # expected_hamburger_list = ["All Items", "About", "Logout", "Reset App State"]
    #     actual_hamburger_list = self.wait.until(EC.visibility_of_all_elements_located(self._burger_menu_list))
    #     try:
    #         assert len(actual_hamburger_list) == len(expected_hamburger_list)
    #     except:
    #         pytest.fail(f"Hamburger menu list count does not matched. Actual Count = {len(actual_hamburger_list)}, "
    #                     f"Expected Count = {len(expected_hamburger_list)}")
    #
    #     try:
    #         for index, element in enumerate(actual_hamburger_list):
    #             expected_element = expected_hamburger_list[index]
    #             actual_element = element.text
    #             assert actual_element == expected_element
    #     except:
    #         pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")


    @allure.step("Verify hamburger menu list")
    def verify_hamburger_menu_list(self, expected_hamburger_list):
        actual_hamburger_list = self.wait.until(EC.visibility_of_all_elements_located(self._burger_menu_list))
        assert len(actual_hamburger_list) == len(expected_hamburger_list), \
            pytest.fail(f"Hamburger menu list count does not matched. Actual Count = "
                        f"{len(actual_hamburger_list)}, Expected Count = {len(expected_hamburger_list)}")

        for index, element in enumerate(actual_hamburger_list):
            expected_element = expected_hamburger_list[index]
            actual_element = element.text
            assert actual_element == expected_element, \
                pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")

    # pytest.fail(f"Element not matched. Expected = {expected_element}, Actual = {actual_element}")


    @allure.step("Verify total product cards displayed")
    def verify_total_product_cards_displayed(self, expected_total_list):
        product_cards = self.wait.until(EC.visibility_of_all_elements_located(self._product_cards))
        actual_total_list = len(product_cards)
        print(f"actual_total_list -> {actual_total_list}")
        for element in product_cards:
            print(f"Element = {element.text}")
        assert actual_total_list == expected_total_list, pytest.fail(f"Total product cards displayed does not matched. Actual = {actual_total_list}, Expected = {expected_total_list}")


    @allure.step("Click Add To Cart button on the First Item using Item name")
    def add_to_cart_first_item(self, item_name):
        add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        add_to_cart_button.click()
        # add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        # print(f">>> add_to_cart_button text = {add_to_cart_button.text}")
        # self.get_item_price(item_name)
        self.item_price_1 = self.get_item_price(item_name)
        print(f">>> self.item_price_1 = {self.item_price_1}")


    @allure.step("Click Add To Cart button on the Second Item using Item name")
    def add_to_cart_second_item(self, item_name):
        add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        add_to_cart_button.click()
        # add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        # print(f">>> add_to_cart_button text = {add_to_cart_button.text}")
        # self.get_item_price(item_name)
        self.item_price_2 = self.get_item_price(item_name)
        print(f">>> self.item_price_2 = {self.item_price_2}")


    @allure.step("Get Item Price")
    def get_item_price(self, item_name):
        item_price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._product_item_price_added_to_cart_dynamic_xpath.format(item_name)))).text
        item_price = item_price.replace("$","")
        # self.item_price_1 = item_price
        # print(f"self.item_price = item_price = {self.item_price_1}")
        return item_price

    @allure.step("Add To Cart should be change to Remove")
    def add_to_cart_button_change_to_remove(self, item_name):
        add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        assert add_to_cart_button.text == "Remove", pytest.fail(f"Incorrect button text. Expected = 'Remove', Actual = {add_to_cart_button.text}")


    @allure.step("Verify cart total")
    def verify_cart_total_text(self, expected_total):
        cart_total_text = self.wait.until(EC.visibility_of_element_located(self._cart_total_text)).text
        assert int(cart_total_text) == expected_total, pytest.fail(f"Incorrect cart total. Expected = {expected_total}, Actual = {cart_total_text}")


    @allure.step("Open Cart")
    def open_cart(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable(self._cart_icon))
        cart_icon = self.wait.until(EC.element_to_be_clickable(self._cart_icon))
        cart_icon.click()


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







