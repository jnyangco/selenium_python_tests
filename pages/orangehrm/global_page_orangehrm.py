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


class GlobalPageOrangehrm(BasePage):

    # Locators - Global Page (gp)
    # _gp_topbar_menu_dynamic_xpath = "//nav[@aria-label='Topbar Menu']/ul/li/a[text()='{}']"
    _gp_topbar_menu_dynamic_xpath = "//a[text()='{}']/.."

    _gp_topbar_menu_add_employee = (By.XPATH, "//a[text()='Add Employee']")
    # _gp_topbar_menu_add_employee = (By.XPATH, "//nav[@aria-label='Topbar Menu']/ul/li/a[text()='Add Employee']/..")


    # Functions
    @allure.step("Click top bar menu")
    def click_top_bar_menu(self, menu):
        # top_bar_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self._gp_topbar_menu_dynamic_xpath.format(menu))))
        # top_bar_menu.click()

        # Try Javascript click
        top_bar_menu_add_employee = self.driver.find_element(*self._gp_topbar_menu_add_employee)
        self.driver.execute_script("arguments[0].click();", top_bar_menu_add_employee)

        # Try ACTIONS
        # top_bar_menu_add_employee = self.driver.find_element(*self._gp_topbar_menu_add_employee)
        # actions = ActionChains(self.driver)
        # actions.click(top_bar_menu_add_employee)
        # actions.perform()












