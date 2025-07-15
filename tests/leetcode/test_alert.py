import allure
import pytest
from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from core.base.base_test import BaseTest


@pytest.mark.leetcode
@pytest.mark.alert
@allure.feature("Leetcode: Button")
class TestAlert(BaseTest):

    @allure.title("Leetcode: Testing alert methods")
    def test_alert_methods(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.click_dialog_button()

        leetcode.verify_alert_accept("Hey! Welcome to LetCode")
        leetcode.verify_alert_confirm()
        leetcode.verify_alert_dismiss()
        leetcode.verify_alert_textbox("John Doe")
        leetcode.verify_alert_modern("Modern Alert - Some people address me as sweet alert as well")

        leetcode.wait_seconds(2)

