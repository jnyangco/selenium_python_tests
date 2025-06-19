import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data
from selenium.webdriver.support import expected_conditions as EC


class CustomerAccountPage(HeaderPage):

    # Locators
    WELCOME_MESSAGE = (By.XPATH, "//span[@class='fontBig ng-binding']/../../strong[1]")
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[normalize-space()='Transactions']")
    DEPOSIT_BUTTON = (By.XPATH, "//button[normalize-space()='Deposit']")
    WITHDRAWL_BUTTON = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    ACCOUNT_LABELS = (By.XPATH, "//div[@ng-hide='noAccount'][1]")


    # Functions
    @allure.step("Get welcome message")
    def get_welcome_message(self):
        welcome_message = self.wait.until(EC.visibility_of_element_located(self.WELCOME_MESSAGE)).text
        self.log.info(f">>> welcome_message = {welcome_message}")
        return welcome_message


    @allure.step("Get button elements displayed status")
    def get_button_elements_displayed_status(self):
        elements_status = {
            "TRANSACTIONS_BUTTON": self.is_element_displayed(self.TRANSACTIONS_BUTTON),
            "DEPOSIT_BUTTON": self.is_element_displayed(self.DEPOSIT_BUTTON),
            "WITHDRAWL_BUTTON": self.is_element_displayed(self.WITHDRAWL_BUTTON)
        }
        return elements_status

    @allure.step("Get account labels displayed status")
    def get_account_labels_displayed_status(self):
        label_text = self.find_web_element(self.ACCOUNT_LABELS).text
        self.log.info(f">>> label_text = {label_text}")
        labels_status = {
            "Account Number": "Account Number" in label_text,
            "Balance": "Balance" in label_text,
            "Currency": "Currency" in label_text
        }
        return labels_status



