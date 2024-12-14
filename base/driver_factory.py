"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_webdriver_instance()
"""
import traceback
from selenium import webdriver

class DriverFactory:

    def __init__(self, browser):
        """
        Inits DriverFactory class

        Returns:
            None
        """
        self.browser = browser
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


    def get_driver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        # baseURL = "https://letskodeit.teachable.com/"
        # baseURL = "https://opensource-demo.orangehrmlive.com"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")


        # # Setting Driver Implicit Time out for An Element
        # driver.implicitly_wait(5)
        #
        # # Maximize the window
        # driver.maximize_window()
        
        # Loading browser with App URL
        # driver.get(baseURL)
        return driver