import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from core.base.base_page import BasePage


class ProductPageSaucedemo(BasePage):

    # Locators
    _product_cards = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item_name ']")
    _product_price = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item_price']")
    _add_to_cart_item_button_dynamic_xpath = "//div[@class='inventory_item_name ' and contains(.,'{}')]/../../..//button[1]"
    _product_item_price_added_to_cart_dynamic_xpath = "//div[@class='inventory_item_name ' and contains(.,'{}')]/../../..//div[@class='inventory_item_price']"
    _cart_total_text = (By.XPATH, "//div[@id='shopping_cart_container']//span")
    _cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    _filter_product = (By.XPATH, "//select[@class='product_sort_container']")
    _burger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    _burger_menu_list = (By.XPATH, "//nav[@class='bm-item-list']/a")


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
        try:
            actual_hamburger_list = self.wait.until(EC.visibility_of_all_elements_located(self._burger_menu_list))
            assert len(actual_hamburger_list) == len(expected_hamburger_list), \
                f"Hamburger menu list count mismatch. Actual = {len(actual_hamburger_list)}, Expected = {len(expected_hamburger_list)}"

            for index, element in enumerate(actual_hamburger_list):
                expected_element = expected_hamburger_list[index]
                actual_element = element.text
                assert actual_element == expected_element, \
                    f"Element mismatch at index {index}. Expected = {expected_element}, Actual = {actual_element}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error(f"Hamburger menu list verification failed.")
            raise


    @allure.step("Verify total product cards displayed")
    def verify_total_product_cards_displayed(self, expected_total_list):
        try:
            product_cards = self.wait.until(EC.visibility_of_all_elements_located(self._product_cards))
            actual_total_list = len(product_cards)
            print(f"actual_total_list -> {actual_total_list}")
            for element in product_cards:
                print(f"Element = {element.text}")
            assert actual_total_list == expected_total_list, \
                f"Total product cards displayed mismatch: Actual = {actual_total_list}, Expected = {expected_total_list}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error(f"Total products verification failed.")
            raise


    @allure.step("Verify cart total")
    def verify_cart_total_text(self, expected_total):
        try:
            cart_total_text = self.wait.until(EC.visibility_of_element_located(self._cart_total_text)).text
            assert int(cart_total_text) == expected_total, \
                f"Incorrect cart total: Expected = {expected_total}, Actual = {cart_total_text}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error(f"Cart total verification failed.")
            raise


    @allure.step("Open Cart")
    def open_cart(self):
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable(self._cart_icon))
            cart_icon.click()
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to open cart.")
            pytest.fail("Failed to open cart.")


    @allure.step("Click Add To Cart button on the First Item using Item name")
    def add_to_cart_first_item(self, item_name):
        try:
            add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
            add_to_cart_button.click()
            item_price_1 = self.get_item_price(item_name)
            print(f">>> self.item_price_1 = {item_price_1}")
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to click add to cart button.")
            pytest.fail("Failed to click add to cart button.")


    @allure.step("Click Add To Cart button on the Second Item using Item name")
    def add_to_cart_second_item(self, item_name):
        try:
            add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
            add_to_cart_button.click()
            item_price_2 = self.get_item_price(item_name)
            print(f">>> self.item_price_2 = {item_price_2}")
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to click add to cart button.")
            pytest.fail("Failed to click add to cart button.")


    @allure.step("Get Item Price")
    def get_item_price(self, item_name):
        try:
            item_price = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                self._product_item_price_added_to_cart_dynamic_xpath.format(item_name)))).text
            item_price = item_price.replace("$","")
            return item_price
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to get item price.")
            pytest.fail("Failed to get item price.")
            return None

    @allure.step("Add To Cart should be change to Remove")
    def add_to_cart_button_change_to_remove(self, item_name):
        try:
            add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
            assert add_to_cart_button.text == "Remove", f"Button text mismatch. Expected = 'Remove', Actual = '{add_to_cart_button.text}'"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify add to cart change to remove.")
            raise


    @allure.step("Select dropdown filter")
    def select_dropdown_filter(self, sort_by):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(self._filter_product))
            dropdown = Select(dropdown)
            dropdown.select_by_visible_text(sort_by)
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to select dropdown filter.")
            pytest.fail("Failed to select dropdown filter.")


    @allure.step("Verify product cards ordering")
    def verify_product_cards_ordering(self, order_type="ascending"): #default = ascending
        try:
            actual_product_list = []
            actual_product_price = []

            product_cards = self.wait.until(EC.visibility_of_all_elements_located(self._product_cards))
            print(f">>> product_cards = {product_cards}")

            product_price = self.wait.until(EC.visibility_of_all_elements_located(self._product_price))

            if order_type.lower() == "ascending":
                for product in product_cards:
                    print(f">>> product = {product.text}")
                    actual_product_list.append(product.text)
                expected_product_list = sorted(actual_product_list)
                print(f">>> actual_product_list = {actual_product_list}")
                print(f">>> expected_product_list = {expected_product_list}")
                assert actual_product_list == expected_product_list, \
                    f"Product is not in ascending order: Expected = \n'{expected_product_list}', Actual = \n'{actual_product_list}'"

            elif order_type.lower() == "descending":
                for product in product_cards:
                    print(f">>> product = {product.text}")
                    actual_product_list.append(product.text)
                expected_product_list = sorted(actual_product_list, reverse=True)
                print(f">>> actual_product_list = {actual_product_list}")
                print(f">>> expected_product_list = {expected_product_list}")
                assert actual_product_list == expected_product_list, \
                    f"Product is not in ascending order: Expected = \n'{expected_product_list}', Actual = \n'{actual_product_list}'"

            elif order_type.lower() == "price low to high":
                for price in product_price:
                    price = float(price.text.replace("$",""))
                    print(f">>> price = {price}")
                    actual_product_price.append(price)

                expected_product_price = sorted(actual_product_price)
                print(f">>> actual_product_price = {actual_product_price}")
                print(f">>> expected_product_price = {expected_product_price}")
                assert actual_product_price == expected_product_price, \
                    f"Product price is not in ascending order: Expected = \n'{expected_product_price}', Actual = \n'{actual_product_price}'"

            elif order_type.lower() == "price high to low":
                for price in product_price:
                    price = float(price.text.replace("$",""))
                    print(f">>> price = {price}")
                    actual_product_price.append(price)

                expected_product_price = sorted(actual_product_price, reverse=True)
                print(f">>> actual_product_price = {actual_product_price}")
                print(f">>> expected_product_price = {expected_product_price}")
                assert actual_product_price == expected_product_price, \
                    f"Product price is not in descending order: Expected = \n'{expected_product_price}', Actual = \n'{actual_product_price}'"

        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify product cards ordering.")
            raise










