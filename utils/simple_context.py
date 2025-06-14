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