import allure
import logging
import inspect

from pages.orangehrm.dashboard_page_orangehrm import DashboardPageOrangehrm
from pages.orangehrm.home_page_orangehrm import HomepageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.config_reader import read_config as data
import time


@allure.feature("Crawler")
class TestCrawlerOrangehrm:

    @allure.title("OrangeHrm: Side bar menu crawler")
    def test_crawler_sidebar_menu_orangehrm(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        login_page = LoginPageOrangehrm(driver)

        log.info("Step: Open the OrangeHrm website")
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and password")
        username = data("orangehrm", "username")
        password = data("orangehrm", "password")
        login_page.login_with_username_and_password(username, password)

        log.info("Step: User is landed on dashboard page")
        dashboard_page = DashboardPageOrangehrm(driver)
        dashboard_page.user_landed_on_dashboard_page()

        log.info("Step: Verify search menu is displayed")
        home_page = HomepageOrangehrm(driver)
        home_page.verify_search_menu_displayed()

        log.info("Step: Verify side bar menus are correct")
        home_page.verify_side_bar_menus(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])

        log.info("Step: Click on each menu and user should be redirected to correct url")
        home_page.side_bar_menu_crawler(["Admin", "PIM", "Leave", "Time",
                                     "Recruitment", "My Info", "Performance", "Dashboard",
                                     "Directory", "Maintenance", "Claim", "Buzz"])





