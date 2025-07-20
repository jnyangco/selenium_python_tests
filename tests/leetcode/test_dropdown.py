import allure
import pytest
from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.leetcode
@pytest.mark.dropdown
@allure.feature("Leetcode: Dropdown")
class TestDropdown(BaseTest):

    @allure.title("Leetcode: Testing dropdown methods")
    def test_dropdown_methods(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.click_select_button()

        leetcode.verify_dropdown_option_list()
        leetcode.verify_dropdown_select_by_visible_text("Banana", "You have selected Banana")

        leetcode.verify_dropdown_select_multiple("Iron Man", "You have selected Iron Man")

        # option_list = "Apple", "Mango", "Orange", "Banana", "Pine Apple"
        leetcode.verify_dropdown_option_list(["Apple", "Mango", "Orange", "Banana", "Pine Apple"])


        # leetcode.wait_seconds(4)

