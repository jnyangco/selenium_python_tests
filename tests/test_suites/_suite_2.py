# TEST SUITE - using UNITTEST
import unittest

# Import test classes
from tests_archived.TC001_login_test_backup_v3_1 import LoginTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create test suite combining all test classes
SmokeTest = unittest.TestSuite([tc1])

# Run Test Suite
# unittest.TextTestRunner(verbosity=2).run(SmokeTest)
unittest.TextTestRunner().run(SmokeTest)