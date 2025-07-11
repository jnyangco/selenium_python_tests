import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from core.base.base_page import BasePage


class CheckoutInformationPageSaucedemo(BasePage):

    # Locators
    _first_name_info = (By.XPATH, "//input[@id='first-name']")
    _last_name_info = (By.XPATH, "//input[@id='last-name']")
    _zip_code_info = (By.XPATH, "//input[@id='postal-code']")
    _continue_button = (By.XPATH, "//input[@id='continue']")
    _secondary_header_text = (By.XPATH, "//div[@data-test='secondary-header']/span")


    @allure.step("Click continue button")
    def click_continue_button(self):
        try:
            continue_button = self.wait.until(EC.element_to_be_clickable(self._continue_button))
            continue_button.click()
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to click continue button.")
            pytest.fail("Failed to click continue button.")


    @allure.step("Verify secondary header text")
    def verify_secondary_header_text(self, expected_secondary_text):
        try:
            actual_secondary_text = self.wait.until(EC.visibility_of_element_located(self._secondary_header_text)).text
            assert actual_secondary_text == expected_secondary_text, \
                f"Incorrect secondary header text: Expected = {expected_secondary_text}, Actual = {actual_secondary_text}"
        except (TimeoutException, AssertionError):
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to verify secondary header text.")
            raise


    @allure.step("Fillup Checkout Information")
    def fillup_checkout_information(self, first_name, last_name, zip_code):
        try:
            first_name_element = self.wait.until(EC.visibility_of_element_located(self._first_name_info))
            first_name_element.send_keys(first_name)
            last_name_element = self.wait.until(EC.element_to_be_clickable(self._last_name_info))
            last_name_element.send_keys(last_name)
            zip_code_element = self.wait.until(EC.element_to_be_clickable(self._zip_code_info))
            zip_code_element.send_keys(zip_code)
        except TimeoutException:
            self.screenshot_util.capture_screenshot()
            self.log.error("Failed to fillup checkout information.")
            pytest.fail("Failed to fillup checkout information.")




