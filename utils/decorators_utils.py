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


# def allure_step(step_description):
#     """
#     Simple decorator that combines @allure.step and self.log.info
#     Usage:
#         @allure_step("Customer dropdown is displayed")
#         def is_customer_dropdown_visible(self):
#             return self.is_element_displayed(self.CUSTOMER_DROPDOWN)
#     """
#     def decorator(func):
#         @allure.step(step_description)
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             # Automatically log the step
#             if hasattr(self, 'log'):
#                 self.log.info(step_description)
#
#             # Execute the original function
#             return func(self, *args, **kwargs)
#         return wrapper
#     return decorator




# def log_step(func):
#     """Log method execution as Allure step"""
#     @functools.wraps(func)
#     @allure.step("{func.__name__}")
#     def wrapper(self, *args, **kwargs):
#         # self.logger.info(f"Executing: {func.__name__}")
#         self.logger.info(f"Step: {func.__name__}")
#         return func(self, *args, **kwargs)
#     return wrapper

# *** adds both logging and Allure step in one place:
# def log_step(step_description):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             msg = step_description.format(*args, **kwargs)
#             self.log.info(msg)
#             with allure.step(msg):
#                 return func(self, *args, **kwargs)
#         return wrapper
#     return decorator


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