import allure
import logging
import inspect
from pages.orangehrm.dashboard_page_orangehrm import DashboardPageOrangehrm
from pages.orangehrm.home_page_orangehrm import HomepageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.config_reader import read_config as data
import time
from base.base_test import BaseTest


@allure.feature("Crawler")
class TestCrawlerOrangehrm(BaseTest):

    @allure.title("OrangeHrm: Side bar menu crawler")
    def test_crawler_sidebar_menu_orangehrm(self, driver, config):

        self.log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        self.log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        self.log.info("Step: User is landed on dashboard page")
        dashboard_page = DashboardPageOrangehrm(driver)
        dashboard_page.user_landed_on_dashboard_page()

        self.log.info("Step: Verify search menu is displayed")
        home_page = HomepageOrangehrm(driver)
        home_page.verify_search_menu_displayed()

        self.log.info("Step: Verify side bar menus are correct")
        home_page.verify_side_bar_menus(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])

        self.log.info("Step: Click on each menu and user should be redirected to correct url")
        home_page.side_bar_menu_crawler(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])





