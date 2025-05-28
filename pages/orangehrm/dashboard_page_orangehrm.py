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
from utils.config_reader import read_config as data


class DashboardPageOrangehrm(BasePageOrangehrm):

    # Locators - Dashboard Page (dp)
    _dp_header_dashboard = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6[text()='Dashboard']")
    _dp_search_menu = (By.XPATH, "//input[@placeholder='Search']")

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




