import allure
from selenium.webdriver.common.by import By
from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data


class CustomerLoginPage(HeaderPage):

    # Locators
    CUSTOMER_DROPDOWN = (By.XPATH, "//select[@id='userSelect']")


    # Functions
    @allure.step("Customer dropdown is displayed")
    def is_customer_dropdown_visible(self):
        return self.is_element_displayed(self.CUSTOMER_DROPDOWN)


