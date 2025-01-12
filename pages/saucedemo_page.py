import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver
# from base.selenium_driver import SeleniumDriver
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus


class SauceDemoPage:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(driver, 10)

    _username_textbox = (By.XPATH, "//input[@id='user-name']")
    _password_textbox = (By.XPATH, "//input[@id='password']")
    _login_button = (By.XPATH, "//input[@id='login-button']")
    _swag_labs_logo = (By.XPATH, "//div[@class='app_logo']")
    _swag_labs_logo2 = (By.XPATH, "//div[@class='app_logo2']")
    _burger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    _burger_menu_list = (By.XPATH, "//nav[@class='bm-item-list']/a")

    _invalid_login_error_message = (By.XPATH, "//h3[@data-test='error']")

    _inventory_list = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item_name ']")
    # _add_to_cart_item_button_dynamic_xpath = "//div[@class='inventory_item_name ' and contains(.,'{}')]/../../..//button[1]"
    _add_to_cart_item_button_dynamic_xpath = "//div[@class='inventory_item_name ' and contains(.,'{}')]/../../..//button[1]"
    _cart_total_text = (By.XPATH, "//div[@id='shopping_cart_container']//span")
    _cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

    # Cart page elements
    _cart_item_list_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']"
    _cart_item_quantity_dynamic_xpath = "//div[@class='cart_item']//div[text()='{}']/../../../div[@class='cart_quantity']"
    _checkout_button = (By.XPATH, "//button[@id='checkout']")



    @allure.step("Open SauceDemo Website")
    def open_saucedemo_website(self):
        self.driver.get(self.base_url)


    @allure.step("Login using username and password")
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
        except TimeoutException as e:
            self.log.error(f"Swag Labs logo is not displayed")
            pytest.fail(f"Swag Labs logo is not displayed")


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


    @allure.step("Verify total inventory list")
    def verify_total_inventory_list(self, expected_total_list):
        inventory_list = self.wait.until(EC.visibility_of_all_elements_located(self._inventory_list))
        actual_total_list = len(inventory_list)
        print(f"actual_total_list -> {actual_total_list}")
        for element in inventory_list:
            print(f"Element = {element.text}")
        assert actual_total_list == expected_total_list, pytest.fail(f"Total inventory list does not matched. Actual = {actual_total_list}, Expected = {expected_total_list}")


    @allure.step("Click Add To Cart button using Item name")
    def add_to_cart_item(self, item_name):
        add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        add_to_cart_button.click()
        # add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        # print(f">>> add_to_cart_button text = {add_to_cart_button.text}")


    @allure.step("Add To Cart should be change to Remove")
    def add_to_cart_button_change_to_remove(self, item_name):
        add_to_cart_xpath = self._add_to_cart_item_button_dynamic_xpath.format(item_name)
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        assert add_to_cart_button.text == "Remove", pytest.fail(f"FAILED: Incorrect button text. Expected = 'Remove', Actual = {add_to_cart_button.text}")


    @allure.step("Verify cart total")
    def verify_cart_total_text(self, expected_total):
        cart_total_text = self.wait.until(EC.visibility_of_element_located(self._cart_total_text)).text
        assert int(cart_total_text) == expected_total, pytest.fail(f"FAILED: Incorrect cart total. Expected = {expected_total}, Actual = {cart_total_text}")


    @allure.step("Open Cart")
    def open_cart(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable(self._cart_icon))
        cart_icon.click()


    @allure.step("Verify item displayed in cart page - item name and quantity")
    def verify_item_displayed_in_cart_page(self, item_name, expected_item_quantity):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_list_dynamic_xpath.format(item_name))))
        except TimeoutException:
            pytest.fail(f"FAILED: Element not visible. Expected = 'True', Actual = 'False'")

        actual_item_quantity = self.wait.until(EC.visibility_of_element_located((By.XPATH, self._cart_item_quantity_dynamic_xpath.format(item_name)))).text
        assert int(actual_item_quantity) == expected_item_quantity, pytest.fail(f"FAILED: Incorrect item quantity for '{item_name}'. Expected = {expected_item_quantity}, Actual = {actual_item_quantity}")


    @allure.step("Click Checkout button")
    def click_checkout_button(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(self._checkout_button))
        checkout_button.click()










