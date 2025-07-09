import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.banking.header_page import HeaderPage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class ManagerAddCustomerPage(HeaderPage):

    # Locators
    FIRST_NAME_TEXTBOX = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_TEXTBOX = (By.XPATH, "//input[@ng-model='lName']")
    POSTAL_CODE_TEXTBOX = (By.XPATH, "//input[@ng-model='postCd']")
    ADD_CUSTOMER_SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Add Customer'])[2]")



    # Functions
    @allure_step("Fill up new customer form")
    def fill_up_new_customer_form(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_TEXTBOX, first_name)
        self.enter_text(self.LAST_NAME_TEXTBOX, last_name)
        self.enter_text(self.POSTAL_CODE_TEXTBOX, postal_code)

    @allure_step("Click Add Customer Save button")
    def click_add_customer_save_button(self):
        self.click_element(self.ADD_CUSTOMER_SAVE_BUTTON)


    @allure_step("Accept Alert popup")
    def accept_alert_popup(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure_step("Get alert text details")
    def get_alert_text_details(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text_body = alert.text[:-1]
        alert_text_customer_id = alert.text[-1:]

        self.log.info(f"Alert text = {alert.text}")
        self.log.info(f"alert_text_body = {alert_text_body}")
        self.log.info(f"alert_text_customer_id = {alert_text_customer_id}")

        alert_text_details = {
            'alert_text_body': alert_text_body,
            'alert_text_customer_id': alert_text_customer_id
        }
        return alert_text_details


    @allure_step("Get new customer form values")
    def get_new_customer_form_values(self):
        return {
            'FIRST_NAME_TEXTBOX': self.get_text(self.FIRST_NAME_TEXTBOX),
            'LAST_NAME_TEXTBOX': self.get_text(self.LAST_NAME_TEXTBOX),
            'POSTAL_CODE_TEXTBOX': self.get_text(self.POSTAL_CODE_TEXTBOX)
        }









