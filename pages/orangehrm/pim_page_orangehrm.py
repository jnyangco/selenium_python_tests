import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.faker_utils import generate_random_fullname
from base.base_page import BasePage
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from utils.data_utils import get_data as data


class PimPageOrangehrm(BasePageOrangehrm):

    # Locators - PIM Page (pg)
    _first_name = (By.XPATH, "//input[@name='firstName']")
    _middle_name = (By.XPATH, "//input[@name='middleName']")
    _last_name = (By.XPATH, "//input[@name='lastName']")
    _cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    _save_button = (By.XPATH, "//button[normalize-space()='Save']")
    _create_login_details_toggle = (By.XPATH, "//p[text()='Create Login Details']/following-sibling::div[1]")
    _username = (By.XPATH, "//label[text()='Username']/../..//input[1]")
    _password = (By.XPATH, "//label[text()='Password']/../..//input[1]")
    _confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../..//input[1]")
    _enabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[1]")
    _disabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[2]")
    _employee_name_label = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']//h6")
    _employee_id_auto_generated = (By.XPATH, "//label[text()='Employee Id']/../..//input[1]")
    _saved_success_message = (By.XPATH, "//div[@aria-live='assertive']")

    # Employee List (tab)
    _employee_list_tab = (By.XPATH, "//a[text()='Employee List']")
    _employee_id_textbox = (By.XPATH, "//label[text()='Employee Id']/../..//input[1]")
    _search_button = (By.XPATH, "//button[normalize-space()='Search']")


    # Functions
    @allure.step("Adding employee...")
    def add_employee(self):
        # Set Context Variable
        element = self.wait.until(EC.visibility_of_element_located(self._employee_id_auto_generated))
        self.context.employee_id = element.get_attribute("value")

        random_fullname = generate_random_fullname()
        self.log.info(f"Generated random fullname: {random_fullname}")
        random_fullname = random_fullname.split(" ")

        self.log.info(f"Enter firstname: {random_fullname[0]}, lastname: {random_fullname[1]}")
        self.enter_text(self._first_name, random_fullname[0])
        self.enter_text(self._last_name, random_fullname[1])
        self.click_element(self._create_login_details_toggle)
        self.wait_seconds(2)

        username = (random_fullname[0]+random_fullname[1]).lower()
        self.log.info(f"Enter username: {username}")
        self.enter_text(self._username, username)

        password = "Password#1"
        self.log.info(f"Enter password: {password}")
        self.enter_text(self._password, password)
        self.enter_text(self._confirm_password, password)
        self.wait_seconds(2)


        # Get value using different methods
        # Get element first
        # element = self.wait.until(EC.visibility_of_element_located(self._employee_id))

        # METHOD 1: Using different attribute methods
        # value = element.get_attribute("value")
        # print(f">>> value = {value}")
        #
        # inner_text = element.get_attribute("innerText")
        # print(f">>> inner_text = {inner_text}")
        #
        # placeholder = element.get_attribute("placeholder")
        # print(f">>> placeholder = {placeholder}")
        #
        # text_content = element.get_attribute("textContent")
        # print(f">>> text_content = {text_content}")

        # METHOD 2: Execute Javascript to get the value
        # value_javascript = self.driver.execute_script("return arguments[0].value;", element)
        # print(f">>> value_javascript = {value_javascript}")

        self.click_element(self._save_button)

        success_message = self.get_text(self._saved_success_message).split("\n")
        print(f">>> message = {success_message}")

        self.screenshot_util.take_screenshot()
        try:
            assert success_message[0] == "Success", \
                f"Success message mismatch: Expected = 'Success', Actual = '{success_message[0]}'"
            assert success_message[1] == "Successfully Saved", \
                f"Success message mismatch: Expected = 'Successfully Saved', Actual = '{success_message[1]}'"
        except AssertionError:
            self.screenshot_util.take_screenshot()
            self.log.error("Success message mismatch")
            raise

        self.wait_seconds(2)



    @allure.step("Search newly added employee")
    def search_newly_added_employee(self):
        self.log.info(f"")
        self.click_element(self._employee_list_tab)
        self.wait_seconds(4)
        self.enter_text(self._employee_id_textbox, self.context.employee_id)
        self.click_element(self._search_button)
        self.wait_seconds(5)
























