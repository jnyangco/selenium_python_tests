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


class DashboardPageOrangehrm(BasePageOrangehrm):

    # Locators - Dashboard Page (dp)
    _header_dashboard = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6[text()='Dashboard']")
    _search_menu = (By.XPATH, "//input[@placeholder='Search']")

    # Functions
    @allure.step("User is landed on dashboard page")
    def user_landed_on_dashboard_page(self):
        try:
            assert self.is_element_displayed(self._header_dashboard), "Header dashboard element is not displayed."
        except AssertionError:
            self.screenshot_util.take_screenshot()
            self.log.error("Header dashboard element is not displayed.")
            raise

        actual_url = ""
        expected_url = data("orangehrm", "dashboard_url")
        try:
            actual_url = self.get_current_url()
            assert actual_url == expected_url, f"Incorrect page url: Expected = {expected_url}, Actual: {actual_url}"
        except AssertionError:
            self.screenshot_util.take_screenshot()
            self.log.error(f"Incorrect page url: Expected = {expected_url}, Actual: {actual_url}")
            raise




