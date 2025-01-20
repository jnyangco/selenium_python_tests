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


log = cl.custom_logger(logging.INFO)
# log.info("")

@pytest.fixture(scope="function")
def driver(request):

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


# --envi qa1 --browser chrome --report True --headless False
def pytest_addoption(parser):
    """Add CLI option for selecting the browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser to use: 'chrome' or 'firefox'")
    parser.addoption("--os_type", action="store", default="", help="Type of operating system: 'mac', 'windows', 'linux'")
    parser.addoption("--env", action="store", default="local", help="Where to run the tests: 'local' or 'docker'")



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