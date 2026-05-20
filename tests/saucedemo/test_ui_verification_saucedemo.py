import allure
import pytest
from pages.saucedemo.login_page_saucedemo import LoginPageSaucedemo
from pages.saucedemo.product_page_saucedemo import ProductPageSaucedemo
from utils.data_utils import get_data as data
from utils.logger_utils import get_logger

log = get_logger(__name__)

@pytest.mark.saucedemo
@pytest.mark.ui
@allure.feature("Saucedemo: User Interface")
class TestUIVerificationSaucedemo:

    @allure.title("SauceDemo: Verify Hamburger List")
    def test_hamburger_menu_list(self, driver, config):

        log.info("Step: Open SauceDemo Website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()

        log.info("Step: Login to website")
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Click hamburger menu")
        product_page = ProductPageSaucedemo(driver)
        product_page.click_hamburger_menu()

        log.info("Step: Verify hamburger menu list")
        actual_menu_list = product_page.get_hamburger_menu_list()
        expected_menu_list = ["All Items", "About", "Logout", "Reset App State"]
        assert actual_menu_list == expected_menu_list, (
            f"Incorrect menu list displayed. "
            f"Expected '{expected_menu_list}', but found '{actual_menu_list}'"
        )


    @allure.title("SauceDemo: Verify Product Cards Count")
    def test_product_cards_count(self, driver, config):

        log.info("Step: Login to website")
        login_page = LoginPageSaucedemo(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        log.info("Step: Verify total product cards displayed")
        products_page = ProductPageSaucedemo(driver)
        expected_count = 6
        actual_count = products_page.get_product_cards_count()
        assert actual_count == expected_count, (f"Incorrect product cards count. "
                                                f"Expected {expected_count}, but found {actual_count}")

