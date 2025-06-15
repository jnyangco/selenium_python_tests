# import logging
# import os
# import shutil
# import subprocess
# from email.policy import default

import pytest
from core.driver.driver_factory import DriverFactory
from config.test_config import TestConfig
from utils.logger_utils import setup_logger, get_logger  # import logger
from utils.screenshot_utils import ScreenshotUtils


# Initialize logger at the very beginning
setup_logger()
logger = get_logger(__name__)


@pytest.fixture(scope="function")
def driver(request):
    """Create and yield WebDriver instance"""
    log = get_logger(__name__)

    config = TestConfig()

    # Get parameters from command line run
    # browser = request.config.getoption("--browser").lower()
    # os_type = request.config.getoption("--os_type").lower()
    # env = request.config.getoption("--env").lower()

    browser = request.config.getoption("--browser", default="chrome").lower() # point to config default value
    os_type = request.config.getoption("--os_type", default="False") # point to config default value
    env = request.config.getoption("--env", default="local").lower() # point to config default value


    log.info(f"--env = {env}")
    if env == "docker":
        # Create driver - webdriver.Remote()
        driver = DriverFactory.create_driver(
            # browser_name=config.BROWSER,
            browser_name=browser,
            headless=True
        )

    else:
        # Create driver - webdriver.Chrome()
        driver = DriverFactory.create_driver(
            # browser_name=config.BROWSER,
            browser_name=browser,
            headless=config.HEADLESS
        )

    # Set implicit wait
    driver.implicitly_wait(config.IMPLICIT_WAIT)

    yield driver

    # Take screenshot on failure
    # NOT WORKING
    # if hasattr(pytest, "_test_failed") and pytest._test_failed:
    #     screenshot_util = ScreenshotUtils(driver)
    #     screenshot_util.take_screenshot("test_failure")

    # Suite driver
    driver.quit()


@pytest.fixture(scope="function")
def config():
    """Return test configuration"""
    return TestConfig()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to add screenshot on test failure"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        pytest._test_failed = True
    else:
        pytest._test_failed = False


def pytest_addoption(parser):
    """Add CLI option for selecting the browser."""
    # parser.addoption("--browser", action="store", default="chrome", help="Type of browser to use: 'chrome' or 'firefox'")
    # parser.addoption("--os_type", action="store", default="", help="Type of operating system: 'mac', 'windows', 'linux'")
    # parser.addoption("--env", action="store", default="local", help="Where to run the tests: 'local' or 'docker'")

    parser.addoption("--browser", action="store", help="Type of browser to use: 'chrome' or 'firefox'")
    parser.addoption("--os_type", action="store", help="Type of operating system: 'mac', 'windows', 'linux'")
    parser.addoption("--env", action="store", help="Where to run the tests: 'local' or 'docker'")