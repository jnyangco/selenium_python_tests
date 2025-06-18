# base/base_test.py
"""
@package base

Base Test class implementation
It implements common functionality for all test classes throughout the application

This class needs to be inherited by all test classes
This should not be used by creating object instances

Example:
    class TestLogin(BaseTest):
        def test_login(self):
            self.log.info("Test started")
"""
import allure
from utils.logger_utils import get_logger


class BaseTest:
    """Base class for all test classes"""

    # note: previous implementation is declaring the logger and print method name in each method
    # log = logging.getLogger(__name__)
    # log.info(f"Starting test: {inspect.currentframe().f_code.co_name}")

    def setup_method(self, method):
        """Setup method called before each test method"""
        self.log.info(f"===== Starting Test: {method.__name__} =====")

    @property
    def log(self):
        """Lazy-loaded logger property"""
        if not hasattr(self, '_log'):
            self._log = get_logger(self.__class__.__name__)
        return self._log


    # ===========================================================
    # Custom Assert functions with allure.step

    @allure.step("Verify {element_name} text is equal to {expected_text}")
    def assert_text_equal(self, actual_text, expected_text, element_name):
        """Assert that two text values are equal"""
        error_message = f"[{element_name}] text mismatch: expected '{expected_text}', actual '{actual_text}'"
        assert actual_text == expected_text, error_message

        # attach useful information to allure report (i.e: query, text, etc)
        # allure.attach(f"Text assertion passed: '{actual_text}' equals '{expected_text}'",
        #               name="Assertion Result", attachment_type=allure.attachment_type.TEXT)


    @allure.step("Verify {element_name} is displayed")
    def assert_element_displayed(self, is_element_displayed, element_name):
        assert is_element_displayed, f"[{element_name}] is not displayed"


    @allure.step("Verify elements are displayed: {elements_dictionary}")
    def assert_elements_displayed(self, elements_dictionary):
        for element_name, status in elements_dictionary:
            assert status, f"'{element_name}' is not displayed"

