import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.banking.header_page import HeaderPage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class ManagerPage(HeaderPage):

    # Locators
    ADD_CUSTOMER_BUTTON = (By.XPATH, "(//button[normalize-space()='Add Customer'])[1]")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Open Account']")
    CUSTOMERS_BUTTON = (By.XPATH, "//button[normalize-space()='Customers']")

    FIRST_NAME_TEXTBOX = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_TEXTBOX = (By.XPATH, "//input[@ng-model='lName']")
    POSTAL_CODE_TEXTBOX = (By.XPATH, "//input[@ng-model='postCd']")
    ADD_CUSTOMER_SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Add Customer'])[2]")



    # Functions
    @allure_step("Get elements displayed status")
    def get_elements_displayed_status(self):
        elements_status = {
            'ADD_CUSTOMER_BUTTON': self.is_element_displayed(self.ADD_CUSTOMER_BUTTON),
            'OPEN_ACCOUNT_BUTTON': self.is_element_displayed(self.OPEN_ACCOUNT_BUTTON),
            'CUSTOMERS_BUTTON': self.is_element_displayed(self.CUSTOMERS_BUTTON)
        }
        return elements_status

    @allure_step("Click Add Customer button")
    def click_add_customer_button(self):
        self.click_element(self.ADD_CUSTOMER_BUTTON)

    @allure_step("Click Open Account button")
    def click_open_account_button(self):
        self.click_element(self.OPEN_ACCOUNT_BUTTON)

    @allure_step("Click Customers button")
    def click_customers_button(self):
        self.click_element(self.CUSTOMERS_BUTTON)











