import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.banking.header_page import HeaderPage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class ManagerOpenAccountPage(HeaderPage):

    # Locators
    CUSTOMER_DROPDOWN = (By.XPATH, "//select[@id='userSelect']")
    CURRENCY_DROPDOWN = (By.XPATH, "//select[@id='currency']")
    PROCESS_BUTTON = (By.XPATH, "//button[text()='Process']")


    # Functions
    @allure_step("Select customer name: '{customer_name}'")
    def select_customer(self, customer_name):
        dropdown = self.find_web_element(self.CUSTOMER_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(customer_name)

    @allure_step("Select currency: '{currency}'")
    def select_currency(self, currency):
        dropdown = self.find_web_element(self.CURRENCY_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(currency)

    @allure_step("Click Process button")
    def click_process_button(self):
        self.click_element(self.PROCESS_BUTTON)


    @allure_step("Accept Alert popup")
    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


    @allure_step("Get alert text")
    def get_alert_text(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text

        alert_text_details = {
            'alert_text_body': alert_text[:-4],
            'alert_text_account_number': alert_text[-4:]
        }

        self.log.info(f"alert text = {alert_text_details}")
        return alert_text_details

    @allure_step("Get text customer dropdown")
    def get_text_customer_dropdown(self):
        return self.get_text(self.CUSTOMER_DROPDOWN).strip()

    @allure_step("Get text currency dropdown")
    def get_text_currency_dropdown(self):
        return self.get_text(self.CURRENCY_DROPDOWN).strip()









