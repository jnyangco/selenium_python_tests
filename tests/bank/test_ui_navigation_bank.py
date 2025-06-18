import allure
import pytest

from pages.bank.header_page_bank import HeaderPageBank
from utils.data_utils import get_data as data
import time
from core.base.base_test import BaseTest
from pages.bank.home_page_bank import HomePageBank
from utils.decorators_utils import screenshot_on_failure


@pytest.mark.bank
# @pytest.mark.login
@allure.feature("Bank: UI & Navigation")
class TestUINavigationBank(BaseTest):

    @allure.title("Bank: Verify home page elements are displayed")
    def test_home_page_elements_bank(self, driver):

        # use assert helper in base test
        home_page = HomePageBank(driver)
        home_page.open_bank_website()
        homepage_element_status = home_page.get_display_status_home_page_elements().items()
        for element, status in homepage_element_status:
            assert status, f"Element '{element}' is not displayed"

        # use assert helper in base test
        header_page = HeaderPageBank(driver)
        header_page_element_status = header_page.get_display_status_header_elements().items()
        for element, status in header_page_element_status:
            assert status, f"Element '{element}' is not displayed"

        # use assert helper in base test
        header_text = header_page.get_header_text()
        assert header_text == "XYZ Bank", f"Text mismatch: Expected = 'XYZ Bank', Actual = '{header_text}'"


    @allure.title("Verify bank home page title")
    def test_home_page_title_bank(self, driver):
        home_page = HomePageBank(driver)
        home_page.open_bank_website()

        page_title = home_page.get_bank_page_title()
        assert page_title == "XYZ Bank", f"Incorrect page title. Expected = 'XYZ Bank', Actual = '{page_title}'"













