import allure
import pytest

from pages.bank.customer_account_page import CustomerAccountPage
from pages.bank.customer_login_page import CustomerLoginPage
from pages.bank.header_page import HeaderPage
from pages.bank.manager_login_page import ManagerLoginPage
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest
from pages.bank.home_page import HomePage
from utils.decorators_utils import screenshot_on_failure


@pytest.mark.banking
@pytest.mark.login
@allure.feature("Banking: Customer Login")
class TestCustomerLogin(BaseTest):

    @allure.title("Banking: Verify Customer Dropdown has options")
    def test_customer_dropdown_has_options(self, driver):
        """Test customer dropdown options contains available customers"""
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_customer_login_button()

        customer_login_page = CustomerLoginPage(driver)
        customer_dropdown_options = customer_login_page.get_customer_dropdown_options()
        assert len(customer_dropdown_options) > 0, "Customer dropdown option is empty"
        assert all(option for option in customer_dropdown_options), "All customer dropdown options should not be empty"


    @allure.title("Banking: Valid Customer Login")
    def test_customer_valid_login(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_customer_login_button()

        customer_login_page = CustomerLoginPage(driver)
        customer_name = data("banking", "customer_name") # Harry Potter
        customer_login_page.login_as_customer(customer_name)

        customer_account_page = CustomerAccountPage(driver)
        welcome_message = customer_account_page.get_welcome_message()
        assert welcome_message.strip() == f"Welcome {customer_name} !!"

        buttons = customer_account_page.get_button_elements_displayed_status().items()
        for button, status in buttons:
            assert status, f"Button '{button}' is not displayed"


        # print(f">>> TEST = {customer_account_page.get_account_labels_displayed_status()}")

        labels_status = customer_account_page.get_account_labels_displayed_status().items()
        for label, status in labels_status:
            assert status, f"Label '{label}' is not displayed"



























