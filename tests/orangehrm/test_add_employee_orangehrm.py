import allure
import pytest
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from pages.orangehrm.pim_page_orangehrm import PimPageOrangehrm
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest


@pytest.mark.orangehrm
@pytest.mark.employee
@allure.feature("Orangehrm: Employee")
class TestAddEmployeeOrangehrm(BaseTest):

    @allure.title("Orangehrm: Add Employee")
    def test_orangehrm_add_employee(self, driver, config):

        self.log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        self.log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        self.log.info("Step: Click PIM side bar menu")
        # login_page inherit base_page_orangehrm
        # login_page.click_side_bar_menu("PIM") # make test confusing? - check code

        # use base_page_orangehrm
        base_page = BasePageOrangehrm(driver)
        base_page.click_side_bar_menu("PIM")
        time.sleep(2)

        self.log.info("Step: Click Add Employee top bar menu")
        base_page.click_top_bar_menu("Add Employee")

        self.log.info("Step: Add an employee")
        pim_page = PimPageOrangehrm(driver)
        pim_page.add_employee()
        # pim_page.search_newly_added_employee()


    # TRY TO USE DIFFERENT TEST AND ACCESS CONTEXT VARIABLE - WORKING
    # @allure.title("Orangehrm: Search newly added employee")
    # def test_search_newly_added_employee(self, driver, config):
    #     self.log.info("Step: Open the OrangeHrm website")
    #     login_page = LoginPageOrangehrm(driver)
    #     login_page.open_orangehrm_website()
    #
    #     self.log.info("Step: Login using username and password")
    #     username = data("orangehrm", "username")
    #     password = data("orangehrm", "password")
    #     login_page.login_with_username_and_password(username, password)
    #
    #     self.log.info("Step: Click PIM side bar menu")
    #     base_page = BasePageOrangehrm(driver)
    #     base_page.click_side_bar_menu("PIM")
    #
    #     self.log.info("Step: Click Add Employee top bar menu")
    #     base_page.click_top_bar_menu("Add Employee")
    #
    #     self.log.info("Step: Add an employee")
    #     pim_page = PimPageOrangehrm(driver)
    #     pim_page.search_newly_added_employee()





