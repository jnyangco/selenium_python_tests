import time
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import driver
# from base.selenium_driver import SeleniumDriver
from utils import custom_logger as cl
import logging
from base.base_page import BasePage
from utils.report_status import ReportStatus


class OrangeHrmPage:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://opensource-demo.orangehrmlive.com/"
        self.wait = WebDriverWait(driver, 10)

    _username_textbox = (By.XPATH, "//input[@name='username']")
    _password_textbox = (By.XPATH, "//input[@name='password']")

    @allure.step("Open OrangeHRM Website")
    def open_orangehrm_website(self):
        self.driver.get(self.base_url)










