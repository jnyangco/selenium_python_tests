# TEST SUITE - using UNITTEST
import unittest

# Import test classes
from tests_archived.TC001_login_test_backup_v3_1 import LoginTest
# from tests.login.test_login_invalid import LoginNegativeTest
# from tests.dashboard.TC001_dashboard_ui_verification import DashboardUIVerification

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginNegativeTest)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(DashboardUIVerification)

# Create test suite combining all test classes
# SmokeTest = unittest.TestSuite([tc1, tc2, tc3])
SmokeTest = unittest.TestSuite([tc1])

# Run Test Suite
# unittest.TextTestRunner(verbosity=2).run(SmokeTest)
unittest.TextTestRunner().run(SmokeTest)