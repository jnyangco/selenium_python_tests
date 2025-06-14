# ======================================================================================================================
# STEP 1: CREATE simple_context.py utils

# utils/simple_context.py
"""
Simple Context Manager with dot notation access

Usage:
    from utils.simple_context import context
    
    # Set values
    context.generated_employee_id = 12345
    context.product_price = 29.99
    context.username = "test_user"
    
    # Get values
    employee_id = context.generated_employee_id
    price = context.product_price
"""

import threading


class SimpleContext:
    """Simple context manager with dot notation access"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Singleton pattern to ensure single instance"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(SimpleContext, cls).__new__(cls)
        return cls._instance
    
    def clear(self):
        """Clear all context variables"""
        attrs_to_remove = []
        for attr in dir(self):
            if not attr.startswith('_') and not callable(getattr(self, attr)):
                attrs_to_remove.append(attr)
        
        for attr in attrs_to_remove:
            delattr(self, attr)


# Create global context instance
context = SimpleContext()






# ======================================================================================================================
# STEP 2: Update basepage
# base/base_page.py (Add this import and one line to your existing BasePage class)

# Add this import at the top
from utils.simple_context import context

class BasePage:
    """Base class for all page objects with simple context support"""

    def __init__(self, driver):
        """ Init BasePage class with simple context support """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger(self.__class__.__name__)
        self.screenshot_util = ScreenshotUtils(driver)
        
        # Add this single line to make context available
        self.context = context

    # ... rest of your existing BasePage methods remain unchanged ...


# ======================================================================================================================
# STEP 3: Sample Usage:
# Example 1: Page class using self.context
# pages/orangehrm/employee_page.py
from base.base_page import BasePage

class EmployeePage(BasePage):
    
    def create_employee(self):
        # Store value in context
        self.context.generated_employee_id = int(self.get_text(self._employee_id_locator))
        self.context.employee_name = self.get_text(self._employee_name_locator)
    
    def search_employee(self):
        # Use value from context
        self.enter_text(self._search_field, str(self.context.generated_employee_id))


# Example 2: Page class using direct import
# pages/saucedemo/product_page.py  
from base.base_page import BasePage
from utils.simple_context import context

class ProductPage(BasePage):
    
    def add_product_to_cart(self):
        # Store values in context
        context.product_price = float(self.get_text(self._price_locator).replace('$', ''))
        context.product_name = self.get_text(self._product_name_locator)
        context.cart_count = int(self.get_text(self._cart_badge))
    
    def verify_cart(self):
        # Use values from context
        expected_price = context.product_price
        expected_name = context.product_name
        # Your verification logic here...


# Example 3: Test class usage
# tests/test_employee.py
import pytest
from pages.orangehrm.employee_page import EmployeePage
from utils.simple_context import context

class TestEmployee:
    
    def test_create_and_search_employee(self, driver):
        employee_page = EmployeePage(driver)
        
        # Step 1: Create employee (stores ID in context)
        employee_page.create_employee()
        
        # Step 2: Search using stored ID  
        employee_page.search_employee()
        
        # Step 3: Verify using context
        assert context.generated_employee_id is not None
        print(f"Employee ID: {context.generated_employee_id}")
        
        # Optional: Clear context at end
        context.clear()


# Example 4: Multiple variables
from utils.simple_context import context

# Set multiple values
context.username = "admin"
context.password = "secret123"
context.employee_id = 12345
context.product_price = 29.99
context.order_total = 149.99

# Use anywhere in your code
login_page.login(context.username, context.password)
employee_page.search_by_id(context.employee_id) 
cart_page.verify_total(context.order_total)

