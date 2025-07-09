import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.banking.header_page import HeaderPage
from utils.data_utils import get_data as data
from selenium.webdriver.support import expected_conditions as EC
from utils.decorators_utils import allure_step


class CustomerLoginPage(HeaderPage):

    # Locators
    CUSTOMER_DROPDOWN = (By.XPATH, "//select[@id='userSelect']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")


    # Functions
    @allure_step("Customer dropdown is displayed")
    def is_customer_dropdown_visible(self):
        return self.is_element_displayed(self.CUSTOMER_DROPDOWN)


    @allure_step("Get customer dropdown options")
    def get_customer_dropdown_options(self):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_DROPDOWN))
        select = Select(dropdown)
        # options = select.options

        options = [option.text for option in select.options]
        return options[1:]  # skip first option

        # for option in select.options:
        #     print(option.text)
        # print(f">>> options = {options[1:]}")

    @allure_step("Login as customer: '{customer_name}'")
    def login_as_customer(self, customer_name):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_DROPDOWN))
        select = Select(dropdown)
        options = select.options
        if options:
            select.select_by_visible_text(customer_name)
        self.click_login_button()

    @allure_step("Click Login button")
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)





