import allure
import logging
import inspect

from pages.orangehrm.global_page_orangehrm import GlobalPageOrangehrm
from pages.orangehrm.home_page_orangehrm import HomepageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.config_reader import read_config as data
import time


@allure.feature("Add Employee")
class TestAddEmployeeOrangehrm:

    @allure.title("OrangeHrm: Add Employee")
    def test_orangehrm_add_employee(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageOrangehrm(driver)

        log.info("Step: Open the OrangeHrm website")
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        log.info("Step: Click PIM side bar menu")
        home_page = HomepageOrangehrm(driver)
        home_page.click_side_bar_menu("PIM")
        time.sleep(2)

        log.info("Step: Click Add Employee top bar menu")
        global_page = GlobalPageOrangehrm(driver)
        global_page.click_top_bar_menu("Add Employee")
        # steps.add_employee()


        time.sleep(5)




