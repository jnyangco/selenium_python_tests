import allure
import pytest
from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.leetcode
@pytest.mark.input
@allure.feature("Leetcode: Input")
class TestInput(BaseTest):

    @allure.title("Leetcode: Testing input methods")
    def test_input_methods(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()
        leetcode.click_input_button()

        leetcode.verify_full_name_placeholder_text("Enter first & last name")
        leetcode.enter_text_to_full_name_textbox("John Doe")
        leetcode.verify_text_inside_the_textbox("ortonikc")
        leetcode.clear_textbox()
        leetcode.verify_textbox_is_disabled()
        leetcode.verify_textbox_is_read_only()

