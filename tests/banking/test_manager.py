import allure
import pytest

from pages.bank.customer_account_page import CustomerAccountPage
from pages.bank.customer_login_page import CustomerLoginPage
from pages.bank.header_page import HeaderPage
from pages.bank.manager_page import ManagerPage
from pages.bank.transactions_page import TransactionsPage
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest
from pages.bank.home_page import HomePage
from utils.decorators_utils import allure_step
from utils.faker_utils import generate_random_last_name, generate_random_postal_code

@pytest.mark.banking
@pytest.mark.manager
@allure.feature("Banking: Manager")
class TestManager(BaseTest):


    @allure.title("Banking: Manager access dashboard")
    def test_access_manager_dashboard(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_bank_manager_login_button()

        manager_page = ManagerPage(driver)
        elements_status = manager_page.get_elements_displayed_status()
        assert elements_status['ADD_CUSTOMER_BUTTON'], f"Element 'ADD_CUSTOMER_BUTTON' is not displayed"
        assert elements_status['OPEN_ACCOUNT_BUTTON'], f"Element 'OPEN_ACCOUNT_BUTTON' is not displayed"
        assert elements_status['CUSTOMERS_BUTTON'], f"Element 'CUSTOMERS_BUTTON' is not displayed"


    @allure.title("Banking: Add new customer")
    def test_add_customer(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_bank_manager_login_button()

        manager_page = ManagerPage(driver)
        manager_page.click_add_customer_button()
        first_name = "QA"
        last_name = generate_random_last_name()
        postal_code = generate_random_postal_code()

        manager_page.fill_up_new_customer_form(first_name, last_name, postal_code)
        manager_page.click_add_customer_save_button()
        alert_text = manager_page.get_alert_text_details()

        alert_text_body = alert_text['alert_text_body']
        assert alert_text_body == "Customer added successfully with customer id :", \
            f"Alert text body mismatch: Expected 'Customer added successfully with customer id :', but got '{alert_text_body}'"

        alert_text_customer_id = int(alert_text['alert_text_customer_id'])
        assert alert_text_customer_id >= 0, f"Invalid Customer Id: Expected to be a number, but got '{alert_text_customer_id}'"

        manager_page.accept_alert_popup()

        # Customer form should be cleared
        new_customer_form_values = manager_page.get_new_customer_form_values()
        assert new_customer_form_values['FIRST_NAME_TEXTBOX'] == "", f"Textbox 'FIRST_NAME_TEXTBOX' is not cleared"
        assert new_customer_form_values['LAST_NAME_TEXTBOX'] == "", f"Textbox 'LAST_NAME_TEXTBOX' is not cleared"
        assert new_customer_form_values['POSTAL_CODE_TEXTBOX'] == "", f"Textbox 'POSTAL_CODE_TEXTBOX' is not cleared"


    @allure.title("Banking: Add new customer and verify account is created")
    def test_add_customer_and_verify_account(self):
        print("Test")










































