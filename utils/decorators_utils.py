# utils/decorators_utils.py
import functools
import allure
from utils.screenshot_utils import take_screenshot
import time


def screenshot_on_failure(func):
    """Take screenshot on test failure"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            take_screenshot(self.driver, f"failure_{func.__name__}")
            raise
    return wrapper


def log_step(func):
    """Log method execution as Allure step"""
    @functools.wraps(func)
    @allure.step("{func.__name__}")
    def wrapper(self, *args, **kwargs):
        # self.logger.info(f"Executing: {func.__name__}")
        self.logger.info(f"Step: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper


def retry(max_attempts=3, delay=1):
    """Retry decorator for flaky operations"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator