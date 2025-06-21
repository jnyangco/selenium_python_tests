# utils/faker_utils.py
"""
Faker utility module for generating random test data

This module provides functions to generate random data for testing purposes
using the Faker library. It includes functions for names, emails, addresses,
and other common test data needs.

Usage:
    from utils.faker_utils import generate_random_fullname, generate_random_email

    name = generate_random_fullname()
    email = generate_random_email()
"""

from faker import Faker
import random
import string


class FakerUtils:
    """Utility class for generating random test data using Faker"""

    def __init__(self, locale='en_US'):
        """
        Initialize FakerUtils with specified locale

        Args:
            locale (str): Locale for data generation (default: 'en_US')
        """
        self.fake = Faker(locale)
        # Faker.seed(0)  # *** FOR REPRODUCIBLE GENERATED RANDOM RESULTS IN TESTS

    def generate_random_fullname(self):
        """
        Generate a random full name

        Returns:
            str: Random full name (first + last name)

        Example:
            "John Smith"
        """
        return self.fake.name()

    def generate_random_first_name(self):
        """
        Generate a random first name

        Returns:
            str: Random first name

        Example:
            "John"
        """
        return self.fake.first_name()

    def generate_random_last_name(self):
        """
        Generate a random last name

        Returns:
            str: Random last name

        Example:
            "Smith"
        """
        return self.fake.last_name()

    def generate_random_email(self, domain=None):
        """
        Generate a random email address

        Args:
            domain (str, optional): Custom domain for email

        Returns:
            str: Random email address

        Example:
            "john.smith@example.com"
        """
        if domain:
            username = self.fake.user_name()
            return f"{username}@{domain}"
        return self.fake.email()

    def generate_random_phone(self):
        """
        Generate a random phone number

        Returns:
            str: Random phone number

        Example:
            "+1-555-123-4567"
        """
        return self.fake.phone_number()

    def generate_random_address(self):
        """
        Generate a random address

        Returns:
            dict: Dictionary containing address components

        Example:
            {
                'street': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'zipcode': '10001',
                'full_address': '123 Main St, New York, NY 10001'
            }
        """
        return {
            'street': self.fake.street_address(),
            'city': self.fake.city(),
            'state': self.fake.state_abbr(),
            'zipcode': self.fake.zipcode(),
            'full_address': self.fake.address().replace('\n', ', ')
        }

    def generate_random_company(self):
        """
        Generate a random company name

        Returns:
            str: Random company name

        Example:
            "Tech Solutions Inc"
        """
        return self.fake.company()

    def generate_random_username(self):
        """
        Generate a random username

        Returns:
            str: Random username

        Example:
            "user123"
        """
        return self.fake.user_name()

    def generate_random_password(self, length=12, include_symbols=True):
        """
        Generate a random password

        Args:
            length (int): Password length (default: 12)
            include_symbols (bool): Include symbols in password (default: True)

        Returns:
            str: Random password

        Example:
            "Abc123!@#"
        """
        if include_symbols:
            return self.fake.password(
                length=length,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True
            )
        else:
            return self.fake.password(
                length=length,
                special_chars=False,
                digits=True,
                upper_case=True,
                lower_case=True
            )

    def generate_random_text(self, max_nb_chars=200):
        """
        Generate random text

        Args:
            max_nb_chars (int): Maximum number of characters (default: 200)

        Returns:
            str: Random text

        Example:
            "Lorem ipsum dolor sit amet..."
        """
        return self.fake.text(max_nb_chars=max_nb_chars)

    def generate_random_date(self, start_date='-30y', end_date='today'):
        """
        Generate a random date

        Args:
            start_date (str): Start date (default: '-30y' for 30 years ago)
            end_date (str): End date (default: 'today')

        Returns:
            str: Random date in YYYY-MM-DD format

        Example:
            "1995-06-15"
        """
        date_obj = self.fake.date_between(start_date=start_date, end_date=end_date)
        return date_obj.strftime('%Y-%m-%d')

    def generate_random_credit_card(self):
        """
        Generate random credit card information

        Returns:
            dict: Dictionary containing credit card info

        Example:
            {
                'number': '4111111111111111',
                'expire': '12/25',
                'security_code': '123'
            }
        """
        return {
            'number': self.fake.credit_card_number(),
            'expire': self.fake.credit_card_expire(),
            'security_code': self.fake.credit_card_security_code()
        }

    def generate_random_postal_code(self):
        """
        Generate a random postal code

        Returns:
            str: Random Postal code

        Example:
            "11234"
        """
        return self.fake.postalcode()





# ==================================================================
# Create a default instance for convenience functions
_faker_utils = FakerUtils()


# Convenience functions for easy import and use
def generate_random_fullname():
    """Generate a random full name"""
    return _faker_utils.generate_random_fullname()


def generate_random_first_name():
    """Generate a random first name"""
    return _faker_utils.generate_random_first_name()


def generate_random_last_name():
    """Generate a random last name"""
    return _faker_utils.generate_random_last_name()


def generate_random_email(domain=None):
    """Generate a random email address"""
    return _faker_utils.generate_random_email(domain)


def generate_random_phone():
    """Generate a random phone number"""
    return _faker_utils.generate_random_phone()


def generate_random_address():
    """Generate a random address"""
    return _faker_utils.generate_random_address()


def generate_random_company():
    """Generate a random company name"""
    return _faker_utils.generate_random_company()


def generate_random_username():
    """Generate a random username"""
    return _faker_utils.generate_random_username()


def generate_random_password(length=12, include_symbols=True):
    """Generate a random password"""
    return _faker_utils.generate_random_password(length, include_symbols)


def generate_random_employee_data():
    """
    Generate complete random employee data for testing

    Returns:
        dict: Dictionary containing all employee information

    Example:
        {
            'first_name': 'John',
            'last_name': 'Smith',
            'full_name': 'John Smith',
            'email': 'john.smith@company.com',
            'phone': '+1-555-123-4567',
            'username': 'jsmith123',
            'password': 'TempPass123!',
            'employee_id': 'EMP001234'
        }
    """
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()

    return {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f"{first_name} {last_name}",
        'email': f"{first_name.lower()}.{last_name.lower()}@company.com",
        'phone': generate_random_phone(),
        'username': f"{first_name[0].lower()}{last_name.lower()}{random.randint(100, 999)}",
        'password': generate_random_password(10, include_symbols=False) + "!",
        'employee_id': f"EMP{random.randint(100000, 999999)}"
    }


def generate_random_customer_data():
    """
    Generate complete random customer data for testing

    Returns:
        dict: Dictionary containing all customer information
    """
    address = generate_random_address()

    return {
        'first_name': generate_random_first_name(),
        'last_name': generate_random_last_name(),
        'full_name': generate_random_fullname(),
        'email': generate_random_email(),
        'phone': generate_random_phone(),
        'address': address,
        'company': generate_random_company()
    }

def generate_random_postal_code():
    """Generate a random postal code"""
    return _faker_utils.generate_random_postal_code()


# Example usage and testing
"""
if __name__ == "__main__":
    print("=== Faker Utils Demo ===")

    # Basic name generation
    print(f"Random Full Name: {generate_random_fullname()}")
    print(f"Random First Name: {generate_random_first_name()}")
    print(f"Random Last Name: {generate_random_last_name()}")

    # Contact information
    print(f"Random Email: {generate_random_email()}")
    print(f"Random Phone: {generate_random_phone()}")

    # Complete employee data
    print("\n=== Random Employee Data ===")
    employee = generate_random_employee_data()
    for key, value in employee.items():
        print(f"{key}: {value}")

    # Complete customer data
    print("\n=== Random Customer Data ===")
    customer = generate_random_customer_data()
    for key, value in customer.items():
        if key == 'address':
            print(f"{key}: {value['full_address']}")
        else:
            print(f"{key}: {value}")
"""