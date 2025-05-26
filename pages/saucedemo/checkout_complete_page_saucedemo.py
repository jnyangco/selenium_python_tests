import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class CheckoutCompletePageSaucedemo(BasePage):

    # Locators
    _checkout_success_message_text = (By.XPATH, "//h2[@class='complete-header']")
    _checkout_success_message_description = (By.XPATH, "//div[@class='complete-text']")
    _back_home_button = (By.XPATH, "//button[@id='back-to-products']")
    _secondary_header_text = (By.XPATH, "//div[@data-test='secondary-header']/span")


    @allure.step("Verify secondary header text")
    def verify_secondary_header_text(self, expected_secondary_text):
        actual_secondary_text = self.wait.until(EC.visibility_of_element_located(self._secondary_header_text)).text
        assert actual_secondary_text == expected_secondary_text, pytest.fail(f"Incorrect secondary header text. Expected = {expected_secondary_text}, Actual = {actual_secondary_text}")


    @allure.step("Verify checkout success message text")
    def verify_checkout_success_message_text(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self._checkout_success_message_text)).text
        assert actual_text == expected_text, pytest.fail(f"FAILED: Incorrect checkout success message text. Expected = {expected_text}, Actual = {actual_text}")


    @allure.step("Verify checkout success message description")
    def verify_checkout_success_message_description(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self._checkout_success_message_description)).text
        assert actual_text == expected_text, pytest.fail(f"Incorrect checkout success message description. Expected = {expected_text}, Actual = {actual_text}")









