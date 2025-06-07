```markdown
# Pytest Configuration Guide

## Overview
This document explains the pytest configuration options used in our framework.

## pytest.ini Configuration

Our `pytest.ini` file contains default options that are applied to every test run:

### addopts Configuration
```ini
addopts =
    -v                              # Verbose output
    -s                              # Show print statements
    --tb=short                      # Short traceback format
    --strict-markers                # Only allow declared markers
    --clean-alluredir               # Clean Allure directory before run
    --alluredir=reports/allure-results    # Allure report directory
    --html=reports/report.html      # HTML report file
    --self-contained-html           # Embed CSS/JS in HTML report



# ============================================================================
Option Details
-v (verbose)
Purpose: Shows detailed test execution information
Example Output:
tests/saucedemo/test_login.py::TestLogin::test_valid_login PASSED
-s (no capture)
Purpose: Displays print statements and logs in real-time
When to use:

✅ Development and debugging
❌ CI/CD (can be too verbose)

--tb=short
Purpose: Shows concise error messages for failed tests
Benefit: Cleaner output focused on actual errors
--strict-markers
Purpose: Only allows markers declared in pytest.ini
Benefit: Catches typos in marker names early
Overriding Default Options
You can override addopts for specific runs:
bash# Quiet mode (overrides -v -s)
pytest -q tests/

# Full tracebacks (overrides --tb=short)
pytest --tb=long tests/

# Add parallel execution
pytest -n auto tests/


****************************************************************************************
# ================================ DETAILED DESCRIPTION ================================

"""
PURPOSE: Only allows markers that are declared in pytest.ini
WITHOUT: Unknown markers show warnings but tests continue
WITH:    Unknown markers cause tests to FAIL

EXAMPLE:
@pytest.mark.typo_smoke  # Typo in 'smoke'
def test_login():
    pass

WITHOUT --strict-markers:
⚠️  Warning: Unknown pytest.mark.typo_smoke - is this a typo?
✅ Test continues and passes

WITH --strict-markers:
❌ ERRORS: 'typo_smoke' not found in `markers` configuration option
❌ Test fails immediately

BENEFIT: Catches typos in marker names, enforces consistency
"""

# -v (--verbose)
"""
PURPOSE: Shows detailed test execution information
WITHOUT -v: test_login.py .                           ✓
WITH -v:    test_login.py::test_valid_login PASSED    ✓
BENEFIT: Better visibility of which tests are running and their status
"""

# -s (--capture=no)
"""
PURPOSE: Disables output capture, shows print statements and logs in real-time
WITHOUT -s: print() statements are hidden during test execution
WITH -s:    print() statements appear immediately
BENEFIT: Great for debugging - you can see your log.info() and print() statements
"""

# --tb=short
"""
PURPOSE: Controls traceback (error) format when tests fail
OPTIONS:
  --tb=long    : Full detailed traceback (default)
  --tb=short   : Shortened traceback (less verbose)
  --tb=line    : One line per failure
  --tb=no      : No traceback at all
EXAMPLE FAILURE OUTPUT:
SHORT:
    assert actual_text == expected_text
    AssertionError: Text mismatch: Expected = 'Login', Actual = 'Sign In'
LONG (default):
    def test_login():
        login_page = LoginPage(driver)
>       assert actual_text == expected_text
        AssertionError: Text mismatch: Expected = 'Login', Actual = 'Sign In'
        /Users/user/project/test_login.py:25: AssertionError
BENEFIT: Cleaner, more focused error messages
"""

# --clean-alluredir
"""
PURPOSE: Cleans the Allure results directory before each test run
WITHOUT: Old test results accumulate, may cause confusion
WITH:    Fresh results for each run

BEHAVIOR:
1. Deletes all files in reports/allure-results/
2. Runs tests
3. Creates new result files

BENEFIT: Ensures reports only show current test run results
"""

# --alluredir=reports/allure-results
"""
PURPOSE: Generates Allure test results in specified directory
CREATES: JSON files that Allure uses to generate beautiful reports

DIRECTORY STRUCTURE:
reports/
└── allure-results/
    ├── result1.json
    ├── result2.json
    ├── attachment1.png
    └── ...

USAGE AFTER TESTS:
allure serve reports/allure-results    # Opens interactive report
allure generate reports/allure-results # Generates static HTML

BENEFIT: Rich, interactive test reports with screenshots, steps, history
"""

# --html=reports/report.html
"""
PURPOSE: Generates HTML test report using pytest-html plugin
CREATES: Single HTML file with test results

REPORT INCLUDES:
- Test summary (passed/failed/skipped)
- Test details with execution time
- Environment information
- Failed test details with error messages

ACCESS: Open reports/report.html in browser

BENEFIT: Simple, self-contained HTML report for sharing results
"""

# --self-contained-html
"""
PURPOSE: Embeds CSS and JavaScript directly in HTML report
WITHOUT: HTML report links to external CSS/JS files
WITH:    Everything embedded in single HTML file

STRUCTURE:
WITHOUT --self-contained-html:
report.html
assets/
├── style.css
└── main.js

WITH --self-contained-html:
report.html (contains everything)

BENEFIT: Single file can be shared via email/Slack without missing assets
"""

# ;--env (commented out)
"""
PURPOSE: The semicolon (;) comments out this option
IF ENABLED: Would add --env as default argument to all pytest runs

POSSIBLE MEANINGS:
1. Custom plugin option (if you have a custom --env plugin)
2. Placeholder for future environment configuration
3. Previously used option that's now disabled

CURRENT STATUS: Disabled/ignored
"""


# ============================================================================
# PRACTICAL IMPACT ON YOUR TEST EXECUTION
# ============================================================================

def practical_impact_examples():
    """Examples of how these options affect your test execution"""

    # COMMAND EQUIVALENCE:
    # Instead of typing this long command every time:
    """
    pytest tests/saucedemo/test_login_saucedemo.py \
        -v \
        -s \
        --tb=short \
        --strict-markers \
        --alluredir=reports/allure-results \
        --clean-alluredir \
        --html=reports/report.html \
        --self-contained-html
    """

    # You can just type:
    """
    pytest tests/saucedemo/test_login_saucedemo.py
    """

    # And get all the benefits automatically!