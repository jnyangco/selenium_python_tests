import allure
import pytest
from pages.banking.customer_account_page import CustomerAccountPage
from pages.banking.customer_login_page import CustomerLoginPage
from pages.banking.header_page import HeaderPage
from pages.banking.manager_add_customer_page import ManagerAddCustomerPage
from pages.banking.manager_customers_page import ManagerCustomersPage
from pages.banking.manager_open_account_page import ManagerOpenAccountPage
from pages.banking.manager_page import ManagerPage
from pages.banking.transactions_page import TransactionsPage
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest
from pages.banking.home_page import HomePage
from utils.decorators_utils import step
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

        manager_add_customer_page = ManagerAddCustomerPage(driver)
        first_name = "QA"
        last_name = generate_random_last_name()
        postal_code = generate_random_postal_code()

        manager_add_customer_page.fill_up_new_customer_form(first_name, last_name, postal_code)
        manager_add_customer_page.click_add_customer_save_button()
        alert_text = manager_add_customer_page.get_alert_text_details()

        alert_text_body = alert_text['alert_text_body']
        assert alert_text_body == "Customer added successfully with customer id :", \
            f"Alert text body mismatch: Expected 'Customer added successfully with customer id :', but got '{alert_text_body}'"

        alert_text_customer_id = int(alert_text['alert_text_customer_id'])
        assert alert_text_customer_id >= 0, f"Invalid Customer Id: Expected to be a number, but got '{alert_text_customer_id}'"

        manager_add_customer_page.accept_alert_popup()

        # Customer form should be cleared
        new_customer_form_values = manager_add_customer_page.get_new_customer_form_values()
        assert new_customer_form_values['FIRST_NAME_TEXTBOX'] == "", f"Textbox 'FIRST_NAME_TEXTBOX' is not cleared"
        assert new_customer_form_values['LAST_NAME_TEXTBOX'] == "", f"Textbox 'LAST_NAME_TEXTBOX' is not cleared"
        assert new_customer_form_values['POSTAL_CODE_TEXTBOX'] == "", f"Textbox 'POSTAL_CODE_TEXTBOX' is not cleared"


    @allure.title("Banking: Add new customer and verify customer is added to the customer table")
    def test_add_customer_and_verify_customer_table(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_bank_manager_login_button()

        manager_page = ManagerPage(driver)
        manager_page.click_add_customer_button()

        manager_add_customer_page = ManagerAddCustomerPage(driver)
        first_name = "QA"
        last_name = generate_random_last_name()
        postal_code = generate_random_postal_code()

        manager_add_customer_page.fill_up_new_customer_form(first_name, last_name, postal_code)
        manager_add_customer_page.click_add_customer_save_button()
        manager_add_customer_page.accept_alert_popup()

        manager_page = ManagerPage(driver)
        manager_page.click_customers_button()

        manager_customers_page = ManagerCustomersPage(driver)
        manager_customers_page.is_customer_exists(first_name, last_name, postal_code)


    @allure.title("Banking: Open an account")
    def test_open_account(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_bank_manager_login_button()

        manager_page = ManagerPage(driver)
        manager_page.click_add_customer_button()

        # Manager Add Customer
        manager_add_customer_page = ManagerAddCustomerPage(driver)
        first_name = "QA"
        last_name = generate_random_last_name()
        postal_code = generate_random_postal_code()

        manager_add_customer_page.fill_up_new_customer_form(first_name, last_name, postal_code)
        manager_add_customer_page.click_add_customer_save_button()
        manager_add_customer_page.accept_alert_popup()

        manager_page = ManagerPage(driver)
        manager_page.click_open_account_button()

        # Manager Open Account Page
        manager_open_account_page = ManagerOpenAccountPage(driver)
        manager_open_account_page.select_customer(first_name + " " +last_name)
        manager_open_account_page.select_currency("Dollar")
        manager_open_account_page.click_process_button()

        alert_text = manager_open_account_page.get_alert_text()

        alert_text_body = "Account created successfully with account Number :"
        assert alert_text_body in alert_text['alert_text_body'], \
            f"Alert text body mismatch. Expected '{alert_text_body}', but found '{alert_text['alert_text_body']}'"

        alert_text_account_number = alert_text['alert_text_account_number']
        assert len(alert_text_account_number) == 4, f"Invalid account number: {alert_text_account_number}"
        assert int(alert_text_account_number) > 0, f"Invalid account number: {alert_text_account_number}"

        manager_open_account_page.accept_alert()

        # Check dropdown values are cleared
        with step("Verify Customer and Currency dropdown values are cleared"):
            customer_dropdown_text = manager_open_account_page.get_text_customer_dropdown()
            currency_dropdown_text = manager_open_account_page.get_text_currency_dropdown()

            assert "---Customer Name---" in customer_dropdown_text, \
                f"Customer dropdown is not cleared. Expected '---Customer Name---', but found '{customer_dropdown_text}'"

            assert "---Currency---" in currency_dropdown_text, \
                f"Currency dropdown is not cleared. Expected '---Currency---', but found '{currency_dropdown_text}'"


    @allure.title("Banking: Open an account and customer login")
    def test_open_account_and_customer_login(self, driver):
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_bank_manager_login_button()

        manager_page = ManagerPage(driver)
        manager_page.click_add_customer_button()

        # Manager Add Customer
        manager_add_customer_page = ManagerAddCustomerPage(driver)
        first_name = "QA"
        last_name = generate_random_last_name()
        postal_code = generate_random_postal_code()

        manager_add_customer_page.fill_up_new_customer_form(first_name, last_name, postal_code)
        manager_add_customer_page.click_add_customer_save_button()
        manager_add_customer_page.accept_alert_popup()

        manager_page = ManagerPage(driver)
        manager_page.click_open_account_button()

        # Manager Open Account Page
        manager_open_account_page = ManagerOpenAccountPage(driver)
        manager_open_account_page.select_customer(first_name + " " + last_name)
        manager_open_account_page.select_currency("Dollar")
        manager_open_account_page.click_process_button()
        manager_open_account_page.accept_alert()
        manager_open_account_page.click_home_button()

        home_page = HomePage(driver)
        home_page.click_customer_login_button()

        customer_login_page = CustomerLoginPage(driver)
        customer_name = first_name + " " + last_name
        customer_login_page.login_as_customer(customer_name)

        customer_account_page = CustomerAccountPage(driver)
        account_number = customer_account_page.get_account_number()
        assert account_number, f"Account number is empty"  # is not None, 0, "", [], {}, etc...
        assert len(account_number) == 4, f"Account number '{account_number}' should be 4 digits"

        balance = customer_account_page.get_balance()
        assert balance >= 0, f"Invalid balance: '{balance}'"

        currency = customer_account_page.get_currency()
        assert currency == "Dollar", f"Currency '{currency}' should be 'Dollar'"














































