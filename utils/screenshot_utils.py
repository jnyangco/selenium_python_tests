import os
import allure
from datetime import datetime
from config.test_config import TestConfig


class ScreenshotUtils:
    """Utility class for taking screenshots"""

    def __init__(self, driver):
        self.driver = driver
        self.config = TestConfig()
        self.screenshots_dir = self.config.SCREENSHOTS_DIR

        # Create screenshots directory if it doesn't exist
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    # @allure.step("Taking screenshot: {name}")
    def capture_screenshot(self, name="screenshot"):
        """Take screenshot and attach to Allure report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshots_dir, filename)

        self.driver.save_screenshot(filepath)

        # Attach to Allure report
        with open(filepath, "rb") as file:
            allure.attach(file.read(), name=filename, attachment_type=allure.attachment_type.PNG)

        return filepath


def take_screenshot(driver, name="screenshot"):
    """Standalone function to take screenshot"""
    screenshot_util = ScreenshotUtils(driver)
    return screenshot_util.capture_screenshot(name)