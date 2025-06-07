# TEST SUITE - using PYTHON FILE
# Run test_suite.py python file
# cmd: python tests/_suite_python_file1.py

import pytest

pytest.main([
    "tests/test_login.py",             # using python files to run
    "tests/test_login_header.py",    # using python files to run
    "--browser", "chrome",                   # browser
    "-n", "auto",                            # parallel run
    # "-m", "regression",                          # usings tags to run
    "-s", "-v",                                     # print, verbose
    # "--alluredir=reports/allure_report"  # for allure report
    ])



# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)
# "-m", "login" -> useful as @tags to group tests
# can run specific file + tag (i.e: tests/test_login.py + -m smoke"


