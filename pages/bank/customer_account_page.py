import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data
from selenium.webdriver.support import expected_conditions as EC
from utils.decorators_utils import allure_step


class CustomerAccountPage(HeaderPage):

    # Locators
    WELCOME_MESSAGE = (By.XPATH, "//span[@class='fontBig ng-binding']/../../strong[1]")
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[normalize-space()='Transactions']")
    DEPOSIT_BUTTON = (By.XPATH, "//button[normalize-space()='Deposit']")
    WITHDRAWL_BUTTON = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    ACCOUNT_LABELS = (By.XPATH, "//div[@ng-hide='noAccount'][1]")
    ACCOUNT_NUMBER_TEXT = (By.XPATH, "//div[@ng-hide='noAccount']/strong[1]")
    BALANCE_TEXT = (By.XPATH, "//div[@ng-hide='noAccount']/strong[2]")
    CURRENCY_TEXT = (By.XPATH, "//div[@ng-hide='noAccount']/strong[3]")
    AMOUNT_TO_DEPOSIT_TEXTBOX = (By.XPATH, "//label[contains(.,'Deposit')]/following-sibling::input")
    AMOUNT_TO_WITHDRAW_TEXTBOX = (By.XPATH, "//label[contains(.,'Withdraw')]/following-sibling::input")
    DEPOSIT_SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Deposit'])[2]")
    TRANSACTION_MESSAGE = (By.XPATH, "//span[@ng-show='message']")
    WITHDRAW_SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Withdraw'])[1]")


    # Functions
    @allure_step("Get welcome message")
    def get_welcome_message(self):
        welcome_message = self.wait.until(EC.visibility_of_element_located(self.WELCOME_MESSAGE)).text
        self.log.info(f">>> welcome_message = {welcome_message}")
        return welcome_message


    @allure_step("Get button elements displayed status")
    def get_button_elements_displayed_status(self):
        elements_status = {
            "TRANSACTIONS_BUTTON": self.is_element_displayed(self.TRANSACTIONS_BUTTON),
            "DEPOSIT_BUTTON": self.is_element_displayed(self.DEPOSIT_BUTTON),
            "WITHDRAWL_BUTTON": self.is_element_displayed(self.WITHDRAWL_BUTTON)
        }
        return elements_status

    @allure_step("Get account labels displayed status")
    def get_account_labels_displayed_status(self):
        label_text = self.find_web_element(self.ACCOUNT_LABELS).text
        self.log.info(f">>> label_text = {label_text}")
        labels_status = {
            "Account Number": "Account Number" in label_text,
            "Balance": "Balance" in label_text,
            "Currency": "Currency" in label_text
        }
        return labels_status


    @allure_step("Get account number")
    def get_account_number(self):
        return self.find_web_element(self.ACCOUNT_NUMBER_TEXT).text.strip()

    @allure_step("Get balance")
    def get_balance(self):
        return int(self.find_web_element(self.BALANCE_TEXT).text.strip())

    @allure_step("Get currency")
    def get_currency(self):
        return self.find_web_element(self.CURRENCY_TEXT).text.strip()

    @allure_step("Deposit money: {amount}")
    def deposit_money(self, amount):
        self.click_element(self.DEPOSIT_BUTTON)
        self.enter_text(self.AMOUNT_TO_DEPOSIT_TEXTBOX, amount)
        self.click_element(self.DEPOSIT_SAVE_BUTTON)
        self.wait_seconds(1)

    @allure_step("Get transaction message")
    def get_transaction_message(self):
        return self.get_text(self.TRANSACTION_MESSAGE)

    @allure_step("Withdraw money: '{amount}'")
    def withdraw_money(self, amount):
        self.click_element(self.WITHDRAWL_BUTTON)
        self.enter_text(self.AMOUNT_TO_WITHDRAW_TEXTBOX, amount)
        self.click_element(self.WITHDRAW_SAVE_BUTTON)
        self.wait_seconds(1)

    @allure_step("Click Transactions button")
    def click_transactions_button(self):
        self.click_element(self.TRANSACTIONS_BUTTON)

    @allure_step("Click Deposit button")
    def click_deposit_button(self):
        self.click_element(self.DEPOSIT_BUTTON)

    @allure_step("Click Withdraw button")
    def click_withdraw_button(self):
        self.click_element(self.WITHDRAWL_BUTTON)







