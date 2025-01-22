import allure
import time

import utils
import utils.custom_logger as cl
import logging
from conftest import driver
from pages.orangehrm_page import OrangeHrmPage
from pages.saucedemo_page import SauceDemoPage
from utils.config_reader import read_config as data


class TestOrangeHrmUIVerification:

    @allure.title("OrangeHrm: Side bar menu crawler")
    def test_orangehrm_ui_verification(self, driver):
        log = cl.custom_logger(logging.INFO)
        log.info("Starting test: test_orangehrm_valid_login")
        steps = OrangeHrmPage(driver)

        log.info("Step: Open the OrangeHrm website")
        steps.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        steps.login_with_username_and_password(username, password)

        log.info("Step: User is landed on dashboard page")
        steps.user_landed_on_dashboard_page()

        log.info("Step: Verify search menu is displayed")
        steps.verify_search_menu_displayed()

        log.info("Step: Verify side bar menus are correct")
        steps.verify_side_bar_menus(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])

        log.info("Step: Click on each menu and user should be redirected to correct url")
        steps.side_bar_menu_crawler(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])





