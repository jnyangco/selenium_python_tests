import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from utils.config_reader import read_config as data


class DashboardPageOrangehrm(BasePage):


    # Locators - Dashboard Page (dp)
    _dp_header_dashboard = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6[text()='Dashboard']")
    _dp_search_menu = (By.XPATH, "//input[@placeholder='Search']")

    # PIM Page (pg)
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
    @allure.step("User is landed on dashboard page")
    def user_landed_on_dashboard_page(self):
        # NOT WORKING
        # self.wait.until(EC.visibility_of_element_located(self._dp_header_dashboard), pytest.fail("Header dashboard is not displayed."))

        # WORKING - but result is not failed -> it is broken (yellow in allure report)
        try:
            self.wait.until(EC.visibility_of_element_located(self._dp_header_dashboard))
        except TimeoutException:
            pytest.fail("Header dashboard is not displayed.")


        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, pytest.fail(f"Incorrect title. Expected = {expected_url}, Actual = {actual_url}")




