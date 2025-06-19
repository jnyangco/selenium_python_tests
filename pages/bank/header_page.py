import allure
from selenium.webdriver.common.by import By
from core.base.base_page import BasePage
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step


class HeaderPage(BasePage):

    # Locators
    XYZ_BANK_HEADER = (By.XPATH, "//strong[text()='XYZ Bank']")
    HEADER = (By.XPATH, "//*[@class='mainHeading']")
    HOME_BUTTON = (By.XPATH, "//button[@class='btn home']")


    # Functions
    @allure_step("Get Header text")
    def get_header_text(self):
        header_text = self.get_text(self.HEADER)
        return header_text


    @allure_step("Click Home button")
    def click_home_button(self):
        self.click_element(self.HOME_BUTTON)


    @allure_step("Get header elements displayed status")
    def get_header_elements_displayed_status(self):
        elements_status = {
            'HEADER': self.is_element_displayed(self.HEADER),
            'HOME_BUTTON': self.is_element_displayed(self.HOME_BUTTON)
        }
        return elements_status


