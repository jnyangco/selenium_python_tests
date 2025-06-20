import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data
from selenium.webdriver.support import expected_conditions as EC
from utils.decorators_utils import allure_step


class TransactionsPage(HeaderPage):

    # Locators
    BACK_BUTTON = (By.XPATH, "//button[text()='Back']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Reset']")
    CALENDAR_START = (By.XPATH, "//input[@id='start']")
    CALENDAR_END = (By.XPATH, "//input[@id='end']")
    TRANSACTIONS_TABLE = (By.XPATH, "//table[@class='table table-bordered table-striped']")
    TRANSACTIONS_TABLE_DYNAMIC_XPATH = "//tr/td[@class='ng-binding'][2][text()='{amount}']/following-sibling::td[text()='{transaction_type}']"

    TRANSACTION_ROWS = (By.XPATH, "//table/tbody/tr")



    # Functions
    @allure_step("Get elements displayed status")
    def get_elements_displayed_status(self):
        elements_status_dict = {
            'BACK_BUTTON': self.is_element_displayed(self.BACK_BUTTON),
            'RESET_BUTTON': self.is_element_displayed(self.RESET_BUTTON),
            'CALENDAR_START': self.is_element_displayed(self.CALENDAR_START),
            'CALENDAR_END': self.is_element_displayed(self.CALENDAR_END),
            'TRANSACTIONS_TABLE': self.is_element_displayed(self.TRANSACTIONS_TABLE)
        }
        return elements_status_dict

    # @allure_step("Is transactions displayed for: Amount {amount}, Transaction type {transaction_type}")
    # def is_transactions_displayed(self, amount, transaction_type):
    #     table_dynamic_xpath = (By.XPATH, self.TRANSACTIONS_TABLE_DYNAMIC_XPATH.format(amount=amount, transaction_type=transaction_type))
    #     return self.is_element_displayed(table_dynamic_xpath)

    @allure_step("Get transaction count")
    def get_transaction_count(self):
        transaction_rows = self.find_web_elements(self.TRANSACTION_ROWS)
        self.log.info(f"Transaction count = {len(transaction_rows)}")
        return len(transaction_rows)


    @allure_step("Get all transactions")
    def get_all_transactions(self):
        all_transactions = []
        transaction_rows = self.find_web_elements(self.TRANSACTION_ROWS)

        for row in transaction_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 3:
                transaction = {
                    'date_time': cells[0].text,
                    'amount': cells[1].text,
                    'transaction_type': cells[2].text
                }
                all_transactions.append(transaction)
        self.log.info(f"all_transactions = {all_transactions}")
        return all_transactions


    @allure_step("Is transaction exists: Amount '{amount}', Transaction type '{transaction_type}'")
    def is_transaction_exists(self, amount, transaction_type):
        all_transactions = self.get_all_transactions()

        for transaction in all_transactions:
            if str(amount) in transaction['amount'] and transaction_type in transaction['transaction_type']:
                self.log.info(f"Transaction exists: amount '{transaction['amount']}', transaction_type '{transaction['transaction_type']}'")
                return True
        return False


    @allure_step("Click Back button")
    def click_back_button(self):
        self.click_element(self.BACK_BUTTON)

    @allure_step("Click Reset button")
    def click_reset_button(self):
        self.click_element(self.RESET_BUTTON)






