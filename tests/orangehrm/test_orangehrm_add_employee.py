import allure
import time
import logging
from conftest import driver
from pages.orangehrm.orangehrm_page import OrangeHrmPage
from utils.config_reader import read_config as data


class TestOrangeAddEmployee:

    @allure.title("OrangeHrm: Add Employee")
    def test_orangehrm_add_employee(self, driver):
        log = logging.getLogger(__name__)
        log.info("Starting test: test_orangehrm_add_employee")
        steps = OrangeHrmPage(driver)

        log.info("Step: Open the OrangeHrm website")
        steps.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        steps.login_with_username_and_password(username, password)

        log.info("Step: Click PIM side bar menu")
        steps.click_side_bar_menu("PIM")
        time.sleep(2)

        log.info("Step: Click Add Employee top bar menu")
        steps.click_top_bar_menu("Add Employee")
        # steps.add_employee()


        time.sleep(5)




