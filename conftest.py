import logging
import os
import shutil
import subprocess
from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import utils.custom_logger as cl

# Docker
# deprecated in Selenium 4
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# NEW ---
import allure
from base.driver_factory import DriverFactory
from config.config import TestConfig
from utils.logger import setup_logger
from utils.screenshot_utils import ScreenshotUtils

logger = setup_logger()

# log = cl.custom_logger(logging.INFO)
# log.info("")

@pytest.fixture(scope="function")
def driver(request):
    """Create and yield WebDriver instance"""
    config = TestConfig()


    # Get parameters from command line run
    browser = request.config.getoption("--browser").lower()
    os_type = request.config.getoption("--os_type").lower()
    env = request.config.getoption("--env").lower()

    print(f">>>>> ENV = {env}")
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
    if hasattr(pytest, "_test_failed") and pytest._test_failed:
        screenshot_util = ScreenshotUtils(driver)
        screenshot_util.take_screenshot("test_failure")

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
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser to use: 'chrome' or 'firefox'")
    parser.addoption("--os_type", action="store", default="", help="Type of operating system: 'mac', 'windows', 'linux'")
    parser.addoption("--env", action="store", default="local", help="Where to run the tests: 'local' or 'docker'")



# old code under def driver() method ------------------------------------------------------------
    '''
    # Get parameters from command line run
    browser = request.config.getoption("--browser").lower()
    os_type = request.config.getoption("--os_type").lower()
    env = request.config.getoption("--env").lower()

    # Chrome Options
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized") # Maximize browser
    # chrome_options.add_argument("--disable-infobars")  # Disable infobar
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    # chrome_options.add_argument("--headless")  # Run headless (optional)
    # chrome_options = chrome_options.to_capabilities()


    if env == 'docker':
        # Docker Selenium Grid Configuration
        SELENIUM_GRID_URL = "http://localhost:4444/wd/hub"

        # Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize browser
        chrome_options.add_argument("--disable-infobars")  # Disable infobar
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--headless")  # Run headless (optional)

        # Initiate Webdriver (remote)
        driver = webdriver.Remote(
            command_executor=SELENIUM_GRID_URL,
            options=chrome_options
        )
    else: # local
        # Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize browser
        driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)

    # Initialize the WebDriver (use Chrome in this example)
    # log.info(">>> driver = webdriver.Chrome()")
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    # driver.maximize_window()

    # wait = WebDriverWait(driver, 10)

    yield driver
    # log.info(">>> driver.quit()")
    driver.quit()
    '''

# old code parameter option for CLI run ------------------------------------------------------------

# --envi qa1 --browser chrome --report True --headless False
'''
def pytest_addoption(parser):
    """Add CLI option for selecting the browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser to use: 'chrome' or 'firefox'")
    parser.addoption("--os_type", action="store", default="", help="Type of operating system: 'mac', 'windows', 'linux'")
    parser.addoption("--env", action="store", default="local", help="Where to run the tests: 'local' or 'docker'")
'''


# Generate Allure Report when execution is completed
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     """Run allure serve after all tests are completed."""
#     allure_results_dir = "reports/allure-results"
#     try:
#         print("\nGenerating Allure report...")
#         subprocess.run(["allure", "serve", allure_results_dir], check=True)
#     except FileNotFoundError:
#         print("Error: 'allure' command not found. Ensure Allure is installed and available in PATH.")
#     except Exception as e:
#         print("")
#         # print(f"Failed to generate Allure report: {e}")


# Delete reports/allure-results before running the test
# @pytest.fixture(scope="session", autouse=True)
# def clear_allure_results():
#     """Clear the allure-results directory before the test session starts."""
#     allure_results_dir = "reports/allure-results"
#
#     if os.path.exists(allure_results_dir):
#         try:
#             subprocess.run(["rm", "-rf", allure_results_dir], check=True)
#             print(f"Cleared: {allure_results_dir}")
#         except subprocess.CalledProcessError as e:
#             print(f"Error clearing {allure_results_dir}: {e}")
#     else:
#         print(f"Directory not found: {allure_results_dir}")