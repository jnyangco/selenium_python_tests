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