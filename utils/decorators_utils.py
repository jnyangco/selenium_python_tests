# utils/decorators_utils.py
import functools
import allure
import sys
from utils.screenshot_utils import take_screenshot
import time
import inspect
from contextlib import contextmanager
from utils.logger_utils import get_logger



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


def allure_step(step_description):
    """
    Enhanced decorator that combines @allure.step and self.log.info with parameter support

    Usage:
        @allure_step("Customer dropdown is displayed")
        def is_customer_dropdown_visible(self):
            return self.is_element_displayed(self.CUSTOMER_DROPDOWN)

        @allure_step("Login as customer: {customer_name}")
        def login_as_customer(self, customer_name):
            # Implementation
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Get function signature for parameter mapping
            sig = inspect.signature(func)
            bound_args = sig.bind(self, *args, **kwargs)
            bound_args.apply_defaults()

            # Create formatted step description
            try:
                # Try to format with parameters (excluding 'self')
                format_args = {k: v for k, v in bound_args.arguments.items() if k != 'self'}
                formatted_description = step_description.format(**format_args)
            except (KeyError, ValueError):
                # If formatting fails, use original description
                formatted_description = step_description

            # Automatically log the step
            if hasattr(self, 'log'):
                self.log.info(formatted_description)

            # Use allure step with formatted description
            with allure.step(formatted_description):
                return func(self, *args, **kwargs)

        return wrapper

    return decorator


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


# ==============================================================
@contextmanager
def step(description):
    """
    Simple context manager for creating allure steps with logging

    Usage:
        with step("Login with valid credentials"):
            login_page.login(username, password)
    """
    # Use centralized logger
    log = get_logger(__name__)
    log.info(description)

    # Create allure step
    with allure.step(description):
        yield