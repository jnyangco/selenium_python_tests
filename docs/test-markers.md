```markdown
# Test Markers Guide

## Overview
Test markers allow you to group and selectively run tests based on categories.

## Available Markers

### Test Types
- `smoke`: Critical functionality tests
- `regression`: Full test suite
- `sanity`: Basic functionality checks

### Applications
- `saucedemo`: SauceDemo application tests
- `orangehrm`: OrangeHRM application tests

### Features
- `login`: Login functionality tests
- `checkout`: Checkout process tests
- `product`: Product-related tests

### Priority
- `critical`: P0 priority tests
- `high`: P1 priority tests
- `medium`: P2 priority tests
- `low`: P3 priority tests

## Usage Examples

### Single Marker
```python
@pytest.mark.smoke
def test_login_valid_credentials(driver):
    pass


Multiple Markers
python@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.critical
@pytest.mark.saucedemo
def test_login_functionality(driver):
    pass
Class-Level Markers
python@pytest.mark.regression
@pytest.mark.saucedemo
class TestLoginSaucedemo(BaseTest):
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        pass
Running Tests with Markers
Basic Usage
bashpytest -m smoke                    # All smoke tests
pytest -m regression               # All regression tests
pytest -m saucedemo               # All SauceDemo tests
Advanced Combinations
bashpytest -m "smoke and saucedemo"           # Smoke tests for SauceDemo
pytest -m "login and not flaky"           # Login tests that aren't flaky
pytest -m "critical or high"              # High priority tests
pytest -m "not slow"                      # Exclude slow tests
Best Practices

Always declare markers in pytest.ini
Use descriptive marker names
Document marker purposes
Combine markers logically
Use --strict-markers to catch typos