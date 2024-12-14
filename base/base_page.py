"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
import traceback
# from base.selenium_driver import SeleniumDriver
from traceback import print_stack

import allure

from utils.util import Util

from utils import custom_logger as cl
import logging

from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# for reports
import time
import os

from utils.config_reader import read_config

class BasePage:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init BasePage class

        Returns:
            None
        """
        # super(BasePage, self).__init__(driver)
        self.driver = driver
        self.base_url = read_config("url", "base_url")
        self.util = Util()


    # positional argument -> by default it will open the base_url
    # if url is provided, it will open the provided url
    def open_url(self, url_path=""):
        url = self.base_url + url_path
        self.driver.get(url)


    def get_title(self):
        return self.driver.title


    # (LOCATOR, LOCATOR_TYPE)
    # def get_element(self, locator, locator_type="xpath"):
    def get_element(self, locator):
        element = None
        try:
            # locator_type = locator_type.lower()
            # by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(*locator)
            # NOTE: * -> is used to unpack the locator values (By.ID, "button[@id='login']

            # print("Element found with locator: " +locator + " and locator_type: " +locator_type)

            # Temporary Commented Out
            # self.log.info("Element found with locator: " +str(locator))
        except:
            # print("Element not found with locator: " +locator + " and locator_type: " +locator_type)
            self.log.info("Element not found with locator: " + str(locator))
        return element


    def get_element_list(self, locator):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            # locator_type = locator_type.lower()
            # by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(*locator)
            self.log.info("Element list found with locator: " + str(locator))
        except:
            self.log.info("Element list not found with locator: " + str(locator))
        return element







    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title

        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.get_title()
            print(">>> actual page title = {}".format(actual_title))
            print(">>> expected page title = {}".format(title_to_verify))
            return self.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False


    # def element_click(self, locator, locator_type="xpath"):
    def element_click(self, locator=""):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.get_element(locator)
            element.click()
            # print("Clicked on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Clicked on element with locator: " + str(locator))
        except:
            # print("Cannot click on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot click on the element with locator: " + str(locator))
            print_stack()


    def send_text(self, text, locator=""):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.get_element(locator)
            element.send_keys(text)
            # print("Send text on element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Send text on element with locator: " + str(locator))
        except:
            # print("Cannot send text on the element with locator: " + locator + " locator Type: " + locator_type)
            self.log.info("Cannot send text on the element with locator: " + str(locator))
            print_stack()


    def get_text(self, locator="", info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            self.log.debug("In locator condition")
            element = self.get_element(locator)

            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    # def is_element_present(self, locator, locator_type="xpath"):
    def is_element_present(self, locator=""):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            # element = self.driver.find_element(by_type, locator)
            element = self.get_element(locator)
            if element is not None:
                # print("Element Found")
                # self.log.info("Element Found")
                self.log.info("Element present with locator: " + str(locator))
                return True
            else:
                # print("Element not found")
                # self.log.info("Element not found")
                self.log.info("Element NOT present with locator: " + str(locator))
                return False
        except:
            # print("Element not found")
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator=""):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            element = self.get_element(locator)
            if element is not None:
                is_displayed = element.is_displayed()  # is_displayed = True
                self.log.info("Element is displayed with locator: " + str(locator))
            else:
                self.log.info("Element not displayed with locator: " + str(locator))
            return is_displayed
        except:
            print("Element not found")
            return False


    # check list of elements
    def element_presence_check(self, locator):
        try:
            element_list = self.driver.find_elements(*locator)
            if len(element_list) > 0:
                # print("Element Found")
                self.log.info("Element Found")
                return True
            else:
                # print("Element not found")
                self.log.info("Element not found")
                return False
        except:
            # print("Element not found")
            self.log.info("Element not found")
            return False


    # RETURN ELEMENT
    def wait_for_element(self, locator, timeout=10, poll_frequency=0.5):
        element = None
        try:
            # by_type = self.get_by_type(locator_type)
            # print("Waiting for maximum :: " + str(timeout) +
            #       " :: seconds for element to be clickable")
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # element = wait.until(EC.element_to_be_clickable((locator, "stopFilter_stops-0"))) # not working
            # element = wait.until(EC.element_to_be_clickable(locator)) # this is also working
            element = wait.until(EC.visibility_of_element_located(locator))
            # print("Element appeared on the web page")
            self.log.info("Element appeared on the web page")
        except:
            # print("Element not appeared on the web page")
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def web_scroll(self, direction="down"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def screenshot(self, result_message):
        """
        Takes the screenshot of the current open web
        """
        print()
        filename = result_message + "." + str(round(time.time() * 1000)) + ".png" #png is more compressed / smaller file
        screenshot_directory = "../reports/"
        relative_filename = screenshot_directory + filename  # this is the filepath

        current_directory = os.path.dirname(__file__)

        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            # if "reports" folder not exist, create a folder
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred ###")
            print_stack()

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            actual_text: Actual Text
            expected_text: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False


    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text match

        Parameters:
            actual_text: Actual Text
            expected_text: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False


    def verify_list_match(self, expected_list, actual_list):
        """
        Verify two list matches

        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        return set(expected_list) == set(actual_list)


    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True


    # @allure.step("Wait for seconds")
    def wait_seconds(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info != "":
            # self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
            self.log.info("Wait :: '" + str(sec) + "' seconds." + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()


