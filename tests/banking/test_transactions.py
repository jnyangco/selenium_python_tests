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
from utils.decorators_utils import allure_step

@pytest.mark.banking
@pytest.mark.transactions
@allure.feature("Banking: Transactions")
class TestTransactions(BaseTest):

    def login_as_customer(self, driver):
        """Helper method to login as customer"""
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_customer_login_button()

        customer_login_page = CustomerLoginPage(driver)
        customer_name = data("banking", "customer_name")  # Harry Potter
        customer_login_page.login_as_customer(customer_name)

        return CustomerAccountPage(driver)



    @allure.title("Banking: Deposit and Withdraw money")
    def test_deposit_and_withdraw_money(self, driver):
        """Test deposit transactions"""
        customer_account_page = self.login_as_customer(driver)

        # First deposit money to ensure sufficient balance
        customer_account_page.deposit_money(500)
        transaction_message = customer_account_page.get_transaction_success_message()
        assert transaction_message == "Deposit Successful", \
            f"Incorrect transaction message. Expected 'Deposit Successful', but got '{transaction_message}'"

        balance = customer_account_page.get_balance()
        assert balance == 500, f"Incorrect balance: Expected '500', but got '{balance}'"

        # Perform withdrawal
        withdraw_amount = 200
        customer_account_page.withdraw_money(withdraw_amount)

        transaction_message = customer_account_page.get_transaction_success_message()
        assert transaction_message == "Transaction successful", \
            f"Incorrect transaction message. Expected 'Transaction successful', but got '{transaction_message}'"

        balance = customer_account_page.get_balance()
        remaining_balance = 500 - withdraw_amount
        assert balance == remaining_balance, f"Incorrect balance. Expected '{remaining_balance}', but got '{balance}'"


























