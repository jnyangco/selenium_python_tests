"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_webdriver_instance()
"""
import traceback
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

import logging
import platform
import os

class DriverFactory:
    """Factory class for creating WebDriver instances"""


    # def __init__(self, browser):
    #     """
    #     Inits DriverFactory class
    #
    #     Returns:
    #         None
    #     """
    #     self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        # Solution 1:
        # MAC
        chromedriver = "/User/jerome/Documents/selenium/drivers/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        # WINDOWS
        chromedriver = "C:/User/jerome/Documents/selenium/drivers/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        # Solution 2:
        PREFERRED: Set the path on the machine where browser will be executed
    """

    @staticmethod
    @allure.step("Creating {browser_name} driver")
    def create_driver(browser_name="chrome", headless=False):
        """Create and return WebDriver instance"""
        log = logging.getLogger(__name__)
        log.info(f"Creating {browser_name} driver")

        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                print(f">>>>> CHROME HEADLESS >>>>>")
                options.add_argument("--headless") # Run headless (optional)
                options.add_argument("--start-maximized")  # Maximize browser
                options.add_argument("--disable-infobars")  # Disable infobar
                options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
                options.add_argument("--no-sandbox")  # Bypass OS security model
                # options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")

                selenium_grid_url = "http://localhost:4444/wd/hub"
                driver = webdriver.Remote(
                    command_executor=selenium_grid_url,
                    options=options
                )
            else:
                print(f">>>>> CHROME NOT HEADLESS >>>>>")
                driver = webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

        elif browser_name.lower() == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"Browser {browser_name} not supported")

        driver.maximize_window()
        log.info(f"{browser_name} driver created successfully")
        return driver



    # def get_driver_instance(self):
    #     """
    #    Get WebDriver Instance based on the browser configuration
    #
    #     Returns:
    #         'WebDriver Instance'
    #     """
    #
    #     # baseURL = "https://letskodeit.teachable.com/"
    #     # baseURL = "https://opensource-demo.orangehrmlive.com"
    #
    #     if self.browser == "chrome":
    #         driver = webdriver.Chrome()
    #     elif self.browser == "firefox":
    #         driver = webdriver.Firefox()
    #     elif self.browser == "iexplorer":
    #         driver = webdriver.Ie()
    #     else:
    #         raise ValueError(f"Unsupported browser: {self.browser}")
    #
    #
    #     # # Setting Driver Implicit Time out for An Element
    #     # driver.implicitly_wait(5)
    #     #
    #     # # Maximize the window
    #     driver.maximize_window()
    #
    #     # Loading browser with App URL
    #     # driver.get(baseURL)
    #     return driver