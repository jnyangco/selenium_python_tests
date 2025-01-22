import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver
# from base.selenium_driver import SeleniumDriver
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus
from utils.config_reader import read_config as data


class OrangeHrmPage:

    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        # self.base_url = "https://opensource-demo.orangehrmlive.com/"
        self.wait = WebDriverWait(driver, 10)

    # ELEMENTS
    # Login Page (lp)
    _lp_username_textbox = (By.XPATH, "//input[@name='username']")
    _lp_password_textbox = (By.XPATH, "//input[@name='password']")
    _lp_login_button = (By.XPATH, "//button[text()=' Login ']")
    _lp_error_message = (By.XPATH, "//div[@class='orangehrm-login-error']//div[1]//p")

    # Homepage (hp)
    _hp_sidebar_menus = (By.XPATH, "//ul[@class='oxd-main-menu']/li//span")
    _hp_sidebar_menus_dynamic_xpath = "//ul[@class='oxd-main-menu']/li//span[text()='{}']"

    # Dashboard Page (dp)
    _dp_header_dashboard = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6[text()='Dashboard']")
    _dp_search_menu = (By.XPATH, "//input[@placeholder='Search']")



    # Login Page Functions
    @allure.step("Open OrangeHRM Website")
    def open_orangehrm_website(self):
        self.log.info("Open OrangeHRM Website")
        base_url = data("orangehrm", "base_url")
        self.driver.get(base_url)

    @allure.step("Login using username and password")
    def login_with_username_and_password(self, username, password):
        self.log.info("Login using username and password")
        self.log.info(f"Enter username '{username}'")
        username_textbox = self.wait.until(EC.element_to_be_clickable(self._lp_username_textbox))
        username_textbox.send_keys(username)

        self.log.info(f"Enter password '{password}'")
        password_textbox = self.wait.until(EC.element_to_be_clickable(self._lp_password_textbox))
        password_textbox.send_keys(password)

        self.log.info("Click Login button")
        login_button = self.wait.until(EC.element_to_be_clickable(self._lp_login_button))
        login_button.click()


    @allure.step("Verify error message using invalid login.")
    def show_login_error_message(self, expected_error_message):
        actual_error_message = self.wait.until(EC.visibility_of_element_located(self._lp_error_message)).text
        assert actual_error_message == expected_error_message, pytest.fail(f"Incorrect error message. Expected = {expected_error_message}, Actual = {actual_error_message}")




    # Homepage
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






    # Dashboard Page
    @allure.step("User is landed on dashboard page")
    def user_landed_on_dashboard_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._dp_header_dashboard))
        except TimeoutException:
            pytest.fail("Header dashboard is not displayed.")

        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, pytest.fail(f"Incorrect title. Expected = {expected_url}, Actual = {actual_url}")












