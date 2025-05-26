import allure
import logging
import inspect
from pages.orangehrm.login_page_orangehrm import OrangeHrmPage
from utils.config_reader import read_config as data
import time


@allure.feature("Crawler")
class TestCrawlerOrangehrm:

    @allure.title("OrangeHrm: Side bar menu crawler")
    def test_crawler_sidebar_menu_orangehrm(self, driver, config):
        log = logging.getLogger(__name__)
        log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
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





