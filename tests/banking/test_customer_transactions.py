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

@pytest.mark.banking
@pytest.mark.transactions
@allure.feature("Banking: Transactions")
class TestCustomerTransactions(BaseTest):

    def login_as_customer(self, driver):
        """Helper method to login as customer"""
        home_page = HomePage(driver)
        home_page.open_bank_website()
        home_page.click_customer_login_button()

        customer_login_page = CustomerLoginPage(driver)
        customer_name = data("banking", "customer_name")  # Harry Potter
        customer_login_page.login_as_customer(customer_name)

        return CustomerAccountPage(driver)



    @allure.title("Banking: Deposit and withdraw money and check balance")
    def test_deposit_and_withdraw_money(self, driver):
        customer_account_page = self.login_as_customer(driver)

        # First deposit money to ensure sufficient balance
        deposit_amount = 500
        customer_account_page.deposit_money(deposit_amount)
        transaction_message = customer_account_page.get_transaction_message()
        assert transaction_message == "Deposit Successful", \
            f"Incorrect transaction message. Expected 'Deposit Successful', but got '{transaction_message}'"

        balance = customer_account_page.get_balance()
        assert balance == deposit_amount, f"Incorrect balance: Expected '{deposit_amount}', but got '{balance}'"

        # Perform withdrawal
        withdraw_amount = 200
        customer_account_page.withdraw_money(withdraw_amount)

        transaction_message = customer_account_page.get_transaction_message()
        assert transaction_message == "Transaction successful", \
            f"Incorrect transaction message. Expected 'Transaction successful', but got '{transaction_message}'"

        balance = customer_account_page.get_balance()
        remaining_balance = deposit_amount - withdraw_amount
        assert balance == remaining_balance, f"Incorrect balance. Expected '{remaining_balance}', but got '{balance}'"


    @allure.title("Banking: Withdraw insufficient funds should show error message and not proceed")
    def test_withdraw_insufficient_funds(self, driver):
        customer_account_page = self.login_as_customer(driver)

        # First deposit money to ensure sufficient balance
        deposit_amount = 500
        customer_account_page.deposit_money(deposit_amount)
        transaction_message = customer_account_page.get_transaction_message()
        assert transaction_message == "Deposit Successful", \
            f"Incorrect transaction message. Expected 'Deposit Successful', but got '{transaction_message}'"

        balance = customer_account_page.get_balance()
        assert balance == deposit_amount, f"Incorrect balance: Expected '{deposit_amount}', but got '{balance}'"

        # Withdraw excessive amount - transaction should be failed and balance not changed
        excessive_amount = 40000
        customer_account_page.withdraw_money(excessive_amount)

        transaction_message = customer_account_page.get_transaction_message()
        expected_message = "Transaction Failed. You can not withdraw amount more than the balance."
        assert transaction_message == expected_message, \
            f"Incorrect transaction message. Expected '{expected_message}', but got '{transaction_message}'"

        last_balance = balance
        current_balance = customer_account_page.get_balance()
        assert current_balance == last_balance, \
            f"Balance should not be changed while transaction failed. Expected '{last_balance}', but got '{current_balance}'"


    @allure.title("Banking: View transaction history for deposit and withdraw details")
    def test_view_transaction_history(self, driver):
        customer_account_page = self.login_as_customer(driver)

        # Perform som transactions - deposit and withdraw
        deposit_amount = 1000
        customer_account_page.deposit_money(deposit_amount)

        withdraw_amount = 500
        customer_account_page.withdraw_money(withdraw_amount)

        customer_account_page.click_transactions_button()
        transactions_page = TransactionsPage(driver)

        # Check transaction elements are displayed
        transactions_elements = transactions_page.get_elements_displayed_status()
        assert transactions_elements['BACK_BUTTON'], f"Back button is not displayed"
        assert transactions_elements['RESET_BUTTON'], f"Reset button is not displayed"
        assert transactions_elements['CALENDAR_START'], f"Calendar start is not displayed"
        assert transactions_elements['CALENDAR_END'], f"Calendar end is not displayed"
        assert transactions_elements['TRANSACTIONS_TABLE'], f"Transactions table is not displayed"

        # Check transaction table is visible with records
        transaction_count = transactions_page.get_transaction_count()
        assert transaction_count == 2, f"Transaction count should be 2, but found '{transaction_count}'"


        # Verify row: Date, Amount, Transaction Type
        # Check transaction rows exists for deposit(credit) and withdraw(debit)
        transaction_exist = transactions_page.is_transaction_exists(deposit_amount, "Credit")
        assert transaction_exist, \
            f"Deposit transaction is not exists for:  Date 'todays date', Deposit Amount {deposit_amount}, Transaction Type 'Credit'"

        transaction_exist = transactions_page.is_transaction_exists(withdraw_amount, "Debit")
        assert transaction_exist, \
            f"Withdraw transaction is not exists for:  Date 'todays date', Withdraw Amount {withdraw_amount}, Transaction Type 'Debit'"


    @allure.title("Banking: Reset transaction")
    def test_reset_transaction(self):
        self.log.info("Test Case")

































