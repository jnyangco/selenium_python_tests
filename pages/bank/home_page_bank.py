import allure
from selenium.webdriver.common.by import By
from pages.bank.header_page_bank import HeaderPageBank
from utils.data_utils import get_data as data


class HomePageBank(HeaderPageBank):

    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Customer Login']")
    BANK_MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Bank Manager Login']")

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

    @allure.step("Get page title")
    def get_bank_page_title(self):
        """Get the current page title"""
        return self.get_page_title()

    @allure.step("Get display status of home page elements")
    def get_display_status_home_page_elements(self):
        """Get home page elements"""

        # elements_status = {
        #     'customer_login_button': self.is_element_displayed(self.CUSTOMER_LOGIN_BUTTON),
        #     'bank_manager_login_button': self.is_element_displayed(self.BANK_MANAGER_LOGIN_BUTTON)
        # }

        # elements_status = {
        #     f'{self.CUSTOMER_LOGIN_BUTTON}': self.is_element_displayed(self.CUSTOMER_LOGIN_BUTTON),
        #     f'{self.BANK_MANAGER_LOGIN_BUTTON}': self.is_element_displayed(self.BANK_MANAGER_LOGIN_BUTTON)
        # }

        elements_status = {
            'CUSTOMER_LOGIN_BUTTON': self.is_element_displayed(self.CUSTOMER_LOGIN_BUTTON),
            'BANK_MANAGER_LOGIN_BUTTON': self.is_element_displayed(self.BANK_MANAGER_LOGIN_BUTTON)
        }

        return elements_status



