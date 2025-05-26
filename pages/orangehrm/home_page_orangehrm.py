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


class HomepageOrangehrm(BasePage):

    # Locators - Homepage (hp)
    _hp_sidebar_menus = (By.XPATH, "//ul[@class='oxd-main-menu']/li//span")
    _hp_sidebar_menus_dynamic_xpath = "//ul[@class='oxd-main-menu']/li//span[text()='{}']"


    # Functions
    @allure.step("Verify search menu is displayed")
    def verify_search_menu_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._dp_search_menu))
        except TimeoutException:
            pytest.fail(f"Search menu is not displayed")


    @allure.step("Verify side bar menus")
    def verify_side_bar_menus(self, expected_menus):
        menus = self.wait.until(EC.visibility_of_all_elements_located(self._hp_sidebar_menus))
        actual_menus = []
        for menu in menus:
            actual_menus.append(menu.text)

        # for index, menu in enumerate(menus):
        #     assert menu.text == expected_menus[index], pytest.fail(f"Incorrect menu displayed. Expected = {expected_menus[index]}, Actual = {menu.text}"]

        print(f">>> actual total menu = {len(menus)}")
        print(f">>> expected total menu = {len(expected_menus)}")
        assert len(menus) == len(expected_menus), pytest.fail(f"Incorrect total menus. Expected = {len(expected_menus)}, Actual = {len(actual_menus)}")

        print(f">>> actual_menus = {actual_menus}")
        print(f">>> expected_menus = {expected_menus}")
        assert actual_menus == expected_menus, pytest.fail(f"Incorrect menus. Expected = {expected_menus}, Actual = {actual_menus}")


    @allure.step("Side bar menu crawler")
    def side_bar_menu_crawler(self, menus):
        base_url = data("orangehrm", "base_url") + "/web/index.php"
        expected_url = ""

        for index in range(len(menus)):
            menu = menus[index]
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self._hp_sidebar_menus_dynamic_xpath.format(menu)))).click()
            except TimeoutException:
                pytest.fail(f"Menu '{menu}' not found")

            current_url = self.driver.current_url

            if menu == "Admin":
                expected_url = base_url + "/admin/viewSystemUsers"
            elif menu == "PIM":
                expected_url = base_url + "/pim/viewEmployeeList"
            elif menu == "Leave":
                expected_url = base_url + "/leave/viewLeaveList"
            elif menu == "Time":
                expected_url = base_url + "/time/viewEmployeeTimesheet"
            elif menu == "Recruitment":
                expected_url = base_url + "/recruitment/viewCandidates"
            elif menu == "My Info":
                expected_url = base_url + "/pim/viewPersonalDetails/empNumber/7"
            elif menu == "Performance":
                expected_url = base_url + "/performance/searchEvaluatePerformanceReview"
            elif menu == "Dashboard":
                expected_url = base_url + "/dashboard/index"
            elif menu == "Directory":
                expected_url = base_url + "/directory/viewDirectory"
            elif menu == "Maintenance":
                expected_url = base_url + "/maintenance/purgeEmployee"
                self.driver.back()
            elif menu == "Claim":
                expected_url = base_url + "/claim/viewAssignClaim"
            elif menu == "Buzz":
                expected_url = base_url + "/buzz/viewBuzz"

            print(f">>> current_url = {current_url}")
            print(f">>> expected_url = {expected_url}")
            assert current_url == expected_url, pytest.fail(f"Incorrect url for '{menu}'. Expected = {expected_url}, Actual = {current_url}")


    @allure.step("Click side bar menu")
    def click_side_bar_menu(self, menu):
        side_bar_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self._hp_sidebar_menus_dynamic_xpath.format(menu))))
        side_bar_menu.click()



















