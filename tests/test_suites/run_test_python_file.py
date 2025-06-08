# TEST SUITE - using PYTHON FILE
# Run using TAGS -> i.e: "-m login" -> Add fixture to def: pytest.mark.login
# cmd run: python tests/run_test_python_file.py

# NOTE: "-m", "login" -> run test cases using with tags @pytest.mark.<custom_mark_name>
# "-m", "login" -> useful as @tags to group tests

import pytest

# ***NEED TO FIX -> other test open browser even deselected
pytest.main([
    "-m", "test",                  # usings tags to run
    "--browser", "chrome",          # browser
    "-n", "auto",                   # parallel run
    ])

