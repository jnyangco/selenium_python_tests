import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from core.base.base_page import BasePage
from utils.data_utils import get_data as data


class BasePageOrangehrm(BasePage):

    # Locators - Global Page (gp)
    _topbar_menu_dynamic_xpath = "//a[text()='{}']/.."
    # _gp_topbar_menu_dynamic_xpath = "//nav[@aria-label='Topbar Menu']/ul/li/a[text()='{}']"
    _topbar_menu_add_employee = (By.XPATH, "//a[text()='Add Employee']")
    # _gp_topbar_menu_add_employee = (By.XPATH, "//nav[@aria-label='Topbar Menu']/ul/li/a[text()='Add Employee']/..")

    # Locators - Homepage (hp)
    _sidebar_menus = (By.XPATH, "//ul[@class='oxd-main-menu']/li//span")
    _sidebar_menus_dynamic_xpath = "//ul[@class='oxd-main-menu']/li//span[text()='{}']"
    _search_menu = (By.XPATH, "//input[@placeholder='Search']")


    # Functions
    @allure.step("Click top bar menu: {menu}")
    def click_top_bar_menu(self, menu):
        # top_bar_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self._gp_topbar_menu_dynamic_xpath.format(menu))))
        # top_bar_menu.click()

        # Try Javascript click
        top_bar_menu_add_employee = self.driver.find_element(*self._topbar_menu_add_employee)
        self.driver.execute_script("arguments[0].click();", top_bar_menu_add_employee)

        # Try ACTIONS
        # top_bar_menu_add_employee = self.driver.find_element(*self._gp_topbar_menu_add_employee)
        # actions = ActionChains(self.driver)
        # actions.click(top_bar_menu_add_employee)
        # actions.perform()


    # Functions
    @allure.step("Verify search menu is displayed")
    def verify_search_menu_displayed(self):
        try:
            search_menu = self.is_element_displayed(self._search_menu)
            assert search_menu, f"Search menu is not displayed."
        except AssertionError:
            self.screenshot_util.capture_screenshot()
            self.log.error("Search menu is not displayed.")
            raise


    @allure.step("Verify side bar menus are displayed")
    def verify_side_bar_menus_displayed(self, expected_sub_menus):
        menus = self.wait.until(EC.visibility_of_all_elements_located(self._sidebar_menus))
        actual_sub_menus = []

        for menu in menus:
            actual_sub_menus.append(menu.text)

        # for index, menu in enumerate(menus):
        #     assert menu.text == expected_menus[index], pytest.fail(f"Incorrect menu displayed. Expected = {expected_menus[index]}, Actual = {menu.text}"]

        print(f">>> actual total menu = {len(menus)}")
        print(f">>> expected total menu = {len(expected_sub_menus)}")
        assert len(menus) == len(expected_sub_menus), pytest.fail(f"Incorrect total sub menus. Expected = {len(expected_sub_menus)}, Actual = {len(actual_sub_menus)}")

        print(f">>> actual_sub_menus = {actual_sub_menus}")
        print(f">>> expected__sub_menus = {expected_sub_menus}")
        assert actual_sub_menus == expected_sub_menus, pytest.fail(f"Incorrect menus. Expected = {expected_sub_menus}, Actual = {actual_sub_menus}")


    @allure.step("Side bar menu crawler")
    def side_bar_menu_crawler(self, menus):
        base_url = data("orangehrm", "base_url") + "/web/index.php"
        expected_url = ""
        current_url = ""

        for index in range(len(menus)):
            menu = menus[index]
            try:
                # option 1
                # self.wait.until(EC.element_to_be_clickable((By.XPATH, self._sidebar_menus_dynamic_xpath.format(menu)))).click()
                # option 2
                # menu_element = (By.XPATH, self._sidebar_menus_dynamic_xpath.format(menu))
                # self.click_element(menu_element)

                # option 3
                # element = (By.XPATH, self._sidebar_menus_dynamic_xpath.format(menu))
                self.click_element_dynamic_xpath(self._sidebar_menus_dynamic_xpath.format(menu))
            except TimeoutException:
                self.log.error(f"Failed to click menu element '{menu}'.")
                raise

            try:
                current_url = self.get_current_url(menu)
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

                assert current_url == expected_url, \
                    f"Incorrect url for '{menu}': Expected = {expected_url}, Actual = {current_url}"
            except (TimeoutException, AssertionError):
                self.screenshot_util.capture_screenshot()
                self.log.error(f"Incorrect url for menu '{menu}': Expected = {expected_url}, Actual = {current_url}")
                raise


    @allure.step("Click side bar menu: {menu}")
    def click_side_bar_menu(self, menu):
        # side_bar_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self._sidebar_menus_dynamic_xpath.format(menu))))
        # side_bar_menu.click()
        self.click_element_dynamic_xpath(self._sidebar_menus_dynamic_xpath.format(menu))
































