import allure
import pytest

from pages.bank.customer_login_page import CustomerLoginPage
from pages.bank.header_page import HeaderPage
from pages.bank.manager_page import ManagerPage
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest
from pages.bank.home_page import HomePage
from utils.decorators_utils import screenshot_on_failure


@pytest.mark.banking
@pytest.mark.ui
@allure.feature("Banking: UI & Navigation")
class TestUINavigationBank(BaseTest):

    @allure.title("Verify home page elements are displayed")
    def test_home_page_elements_bank(self, driver):
        # use assert helper in base test
        home_page = HomePage(driver)
        home_page.open_bank_website()
        with allure.step("Verify homepage_element_status"):
            homepage_element_status = home_page.get_elements_displayed_status().items()
            for element, status in homepage_element_status:
                assert status, f"Element '{element}' is not displayed"

        # use assert helper in base test
        header_page = HeaderPage(driver)
        with allure.step("Verify header_page_element_status"):
            header_page_element_status = header_page.get_header_elements_displayed_status().items()
            for element, status in header_page_element_status:
                assert status, f"Element '{element}' is not displayed"

        # use assert helper in base test
        with allure.step("Verify header_text: XYZ Bank"):
            header_text = header_page.get_header_text()
            assert header_text == "XYZ Bank", f"Incorrect header text. Expected 'XYZ Bank', but got = '{header_text}'"


    @allure.title("Verify banking home page title")
    def test_home_page_title_bank(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()

        with allure.step("Verify Page Title = XYZ Bank"):
            page_title = home_page.get_bank_page_title()
            assert page_title == "XYZ Bank", f"Incorrect page title. Expected = 'XYZ Bank', but got = '{page_title}'"


    @allure.title("Navigate between pages")
    def test_navigation_between_pages(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_customer_login_button()

        # Customer Login Page
        customer_login_page = CustomerLoginPage(driver)
        with allure.step("Verify Customer Dropdown is displayed"):
            element_status = customer_login_page.is_customer_dropdown_visible()
            assert element_status, f"Element 'CUSTOMER_DROPDOWN' is not displayed"

        home_page = HomePage(driver)
        home_page.click_home_button()
        with allure.step("Verify CUSTOMER_LOGIN_BUTTON and BANK_MANAGER_LOGIN_BUTTON are displayed"):
            elements_status = home_page.get_elements_displayed_status()
            assert elements_status['CUSTOMER_LOGIN_BUTTON'], f"Element 'CUSTOMER_LOGIN_BUTTON' is not displayed"
            assert elements_status['BANK_MANAGER_LOGIN_BUTTON'], f"Element 'BANK_MANAGER_LOGIN_BUTTON' is not displayed"

        # Manager Login Page
        home_page.click_bank_manager_login_button()
        manager_login_page = ManagerPage(driver)
        with allure.step("Verify ADD_CUSTOMER_BUTTON, OPEN_ACCOUNT_BUTTON, CUSTOMERS_BUTTON are displayed"):
            elements_status = manager_login_page.get_elements_displayed_status()
            assert elements_status['ADD_CUSTOMER_BUTTON'], f"Element 'ADD_CUSTOMER_BUTTON' is not displayed"
            assert elements_status['OPEN_ACCOUNT_BUTTON'], f"Element 'OPEN_ACCOUNT_BUTTON' is not displayed"
            assert elements_status['CUSTOMERS_BUTTON'], f"Element 'CUSTOMERS_BUTTON' is not displayed"





















