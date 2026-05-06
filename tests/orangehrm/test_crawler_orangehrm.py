import allure
import pytest
from pages.orangehrm.base_page_orangehrm import BasePageOrangehrm
from pages.orangehrm.login_page_orangehrm import LoginPageOrangehrm
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.orangehrm
@pytest.mark.crawler
@allure.feature("Orangehrm: Crawler")
class TestCrawlerOrangehrm:

    @allure.title("OrangeHrm: Side bar menu crawler")
    def test_crawler_sidebar_menu_orangehrm(self, driver, config):

        log.info("Step: Open the OrangeHrm website")
        login_page = LoginPageOrangehrm(driver)
        login_page.open_orangehrm_website()

        log.info("Step: Login using username and password")
        login_page.login()

        log.info("Step: Verify search menu is displayed")
        base_page = BasePageOrangehrm(driver)
        base_page.verify_search_menu_displayed()

        log.info("Step: Verify side bar menus are correct")
        # side_bar_menus = []
        base_page.verify_side_bar_menus_displayed([
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Claim",
            "Buzz"
        ])

        log.info("Step: Click on each menu and user should be redirected to correct url")
        base_page.side_bar_menu_crawler([
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Claim",
            "Buzz"
        ])

