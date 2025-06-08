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
    __middle_name = (By.XPATH, "//input[@name='middleName']")
    _last_name = (By.XPATH, "//input[@name='lastName']")
    _cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    _save_button = (By.XPATH, "//button[normalize-space()='Save']")
    _create_login_details_toggle = (By.XPATH, "//p[text()='Create Login Details']/following-sibling::div[1]")
    _username = (By.XPATH, "//label[text()='Username']/../..//input[1]")
    _password = (By.XPATH, "//label[text()='Password']/../..//input[1]")
    _confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../../div[2]")
    _enabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[1]")
    _disabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[2]")
    _employee_name_label = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']//h6")


    # Functions
    def add_employee(self):
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
        self.enter_text(self._password, "Password#1")
        self.wait_seconds(2)


















