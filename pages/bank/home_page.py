import allure
from selenium.webdriver.common.by import By
from pages.bank.header_page import HeaderPage
from utils.data_utils import get_data as data


class HomePage(HeaderPage):

    # Locators
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Customer Login']")
    BANK_MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Bank Manager Login']")


    # Functions
    @allure.step("Open banking website")
    def open_bank_website(self):
        self.log.info("Open banking website")
        url = data("bank", "base_url")
        self.open_url(url)


    @allure.step("Click Customer Login button")
    def click_customer_login_button(self):
        self.click_element(self.CUSTOMER_LOGIN_BUTTON)


    @allure.step("Click Bank Manager Login button")
    def click_bank_manager_login_button(self):
        self.click_element(self.BANK_MANAGER_LOGIN_BUTTON)


    @allure.step("Get bank page title")
    def get_bank_page_title(self):
        """Get the current page title"""
        return self.get_page_title()


    @allure.step("Get elements displayed status")
    def get_elements_displayed_status(self):
        """Get home page elements display status"""
        elements_status = {
            'CUSTOMER_LOGIN_BUTTON': self.is_element_displayed(self.CUSTOMER_LOGIN_BUTTON),
            'BANK_MANAGER_LOGIN_BUTTON': self.is_element_displayed(self.BANK_MANAGER_LOGIN_BUTTON)
        }

        return elements_status



