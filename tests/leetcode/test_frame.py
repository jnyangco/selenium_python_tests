import allure
import pytest
from pages.leetcode.leetcode_page import LeetcodePage
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from utils.data_utils import get_data as data
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.leetcode
@pytest.mark.frame
@allure.feature("Leetcode: Frame")
class TestFrame:

    @allure.title("Leetcode: Testing frame methods")
    def test_frame_methods(self, driver):

        leetcode = LeetcodePage(driver)
        leetcode.open_leetcode_site()

        leetcode.click_alert_button()


        leetcode.wait_seconds(2)

