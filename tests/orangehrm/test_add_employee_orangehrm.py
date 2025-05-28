import allure
import logging
import inspect
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.config_reader import read_config as data
import time
from base.base_test import BaseTest


@allure.feature("Add Employee")
class TestAddEmployeeOrangehrm(BaseTest):

    @allure.title("OrangeHrm: Add Employee")
    def test_orangehrm_add_employee(self, driver, config):

        self.log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        self.log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        self.log.info("Step: Click PIM side bar menu")
        login_page.click_side_bar_menu("PIM")
        base_page = BasePageOrangehrm(driver)
        base_page.click_side_bar_menu("PIM")
        time.sleep(2)

        self.log.info("Step: Click Add Employee top bar menu")
        base_page.click_top_bar_menu("Add Employee")
        # steps.add_employee()

        time.sleep(5)




