import allure
from selenium.webdriver.common.by import By
from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step

class ManagerLoginPage(HeaderPage):

    # Locators
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//button[normalize-space()='Add Customer']")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Open Account']")
    CUSTOMERS_BUTTON = (By.XPATH, "//button[normalize-space()='Customers']")


    # Functions
    @allure_step("Get elements displayed status")
    def get_elements_displayed_status(self):
        elements_status = {
            'ADD_CUSTOMER_BUTTON': self.is_element_displayed(self.ADD_CUSTOMER_BUTTON),
            'OPEN_ACCOUNT_BUTTON': self.is_element_displayed(self.OPEN_ACCOUNT_BUTTON),
            'CUSTOMERS_BUTTON': self.is_element_displayed(self.CUSTOMERS_BUTTON)
        }
        return elements_status


