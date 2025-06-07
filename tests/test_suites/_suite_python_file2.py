# TEST SUITE - using PYTHON FILE
# Run using TAGS -> i.e: "-m login" -> Add fixture to def: pytest.mark.login
# cmd: python tests/_suite_python_file2.py

import pytest

# ***NEED TO FIX -> other test open browser even deselected
pytest.main([
    "-m", "login",                  # usings tags to run
    "--browser", "chrome",          # browser
    "-n", "auto",                   # parallel run
    ])


# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)
# "-m", "login" -> useful as @tags to group tests



