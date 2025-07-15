import allure
import pytest
from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.leetcode
@pytest.mark.button
@allure.feature("Leetcode: Button")
class TestButton(BaseTest):

    @allure.title("Leetcode: Testing button methods")
    def test_button_methods(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.click_click_button()
        leetcode.click_goto_home_button()
        leetcode.verify_current_url("https://letcode.in/")
        leetcode.navigate_back()

        leetcode.verify_button_location()

        leetcode.verify_button_color("#2A9D90")

        leetcode.verify_button_size()

        leetcode.verify_button_is_disabled()

        leetcode.verify_button_click_and_hold("Button Hold!", "Button has been long pressed")

        # leetcode.wait_seconds(5)

