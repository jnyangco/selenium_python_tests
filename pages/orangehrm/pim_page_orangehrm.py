import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from utils.data_utils import get_data as data


class PimPageOrangehrm(BasePageOrangehrm):

    # Locators - PIM Page (pg)
    _pim_first_name = (By.XPATH, "//input[@name='firstName']")
    _pim_middle_name = (By.XPATH, "//input[@name='middleName']")
    _pim_last_name = (By.XPATH, "//input[@name='lastName']")
    _pim_cancel_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    _pim_save_button = (By.XPATH, "//button[normalize-space()='Save']")
    _pim_create_login_details_toggle = (By.XPATH, "//p[text()='Create Login Details']/following-sibling::div[1]")
    _pim_username = (By.XPATH, "//label[text()='Username']/../..//input[1]")
    _pim_password = (By.XPATH, "//label[text()='Password']/../..//input[1]")
    _pim_confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../../div[2]")
    _pim_enabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[1]")
    _pim_disabled_radio_button = (By.XPATH, "(//input[@type='radio']/following-sibling::span)[2]")
    _pim_employee_name_label = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']//h6")


    # Functions
    # def add_employee(self):
    #     random_name = util.generate_random_names()
    #     random_name = random_name.split(" ")
    #     self.wait.until(EC.visibility_of_element_located(self._pim_first_name)).send_keys(random_name[0])
    #     self.wait.until(EC.visibility_of_element_located(self._pim_last_name)).send_keys(random_name[1])
    #     self.wait.until(EC.element_to_be_clickable(self._pim_create_login_details_toggle)).click()
    #     time.sleep(1)
    #     self.wait.until(EC.visibility_of_element_located(self._pim_username)).send_keys(random_name[0]+random_name[1])
    #     self.wait.until(EC.visibility_of_element_located(self._pim_password)).send_keys("Password#1")
    #     # self.wait.until(EC.visibility_of_element_located(self._pim_confirm_password)).send_keys("Password#1")
    #     # self.wait.until(EC.element_to_be_clickable(self._pim_save_button)).click()

















