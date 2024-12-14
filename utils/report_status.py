# In the tutorial -> the python filename is "teststatus", classname is "TestStatus"
"""
@package utils

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utils.custom_logger as cl
import logging
# from base.selenium_driver import SeleniumDriver
from traceback import print_stack

from base.base_page import BasePage

# class ReportStatus(SeleniumDriver):
class ReportStatus(BasePage):

    # log = cl.customLogger(logging.INFO)
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Init CheckPoint class
        """
        super(ReportStatus, self).__init__(driver)
        self.resultList = []


    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    print(f"IF 1: > set result = {result}")
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                    print(f"RESULT LIST = {self.resultList}")
                else:
                    print(f"ELSE 1: set result = {result}")
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + result_message)
                    self.screenshot(result_message)
                    print(f"RESULT LIST = {self.resultList}")
            else:
                print(f"ELSE 2: set result = {result}")
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + result_message)
                self.screenshot(result_message)
                print(f"RESULT LIST = {self.resultList}")
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenshot(result_message)
            print_stack()
            print(f"RESULT LIST = {self.resultList}")


    # CHECK IF TRUE or FALSE
    # mark (assert) -> if Pass (append PASS to the list), if Fail (append FAIL to the list)
    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)


    # CHECK if TRUE or FALSE
    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)

        print(f"self.resultList = {self.resultList}")
        if "FAIL" in self.resultList:
            self.log.error(test_name + " ### TEST CASE FAILED ###")
            self.resultList.clear()
            assert True == False, result_message  # this it to force failed (since we knew test is failed "FAIL" appended in resultlist)
        else:
            self.log.info(test_name + " ### TEST CASE PASSED ###")
            self.resultList.clear()
            assert True == True