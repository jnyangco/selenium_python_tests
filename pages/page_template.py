import allure
from selenium.webdriver.common.by import By
from core.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from utils.data_utils import get_data as data
from utils.decorators_utils import allure_step



class PageTemplate(BasePage):

    # ============================================================================
    # LOCATORS - All locators from all banking pages
    # ============================================================================
    # Edit Page
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Customer Login']")
    BANK_MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Bank Manager Login']")



    # ============================================================================
    # HEADER PAGE METHODS
    # ============================================================================
    @allure_step("Open banking website")
    def open_leetcode_site(self):
        url = data("leetcode", "base_url")
        self.open_url(url)