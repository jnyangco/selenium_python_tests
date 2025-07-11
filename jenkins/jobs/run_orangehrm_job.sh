#!/bin/bash
# scripts/jobs/run_orangehrm_job.sh - Simple Orangehrm Job Script
set -e

# Export PATH
export PATH=$PATH:/usr/local/bin

# Display build parameters
echo "=== Build Parameters ==="
echo "Branch: ${BRANCH_NAME}"
echo "Browser: ${BROWSER}"
echo "Environment: ${ENVIRONMENT}"
echo "Parallel Workers: ${PARALLEL_WORKERS}"
echo "Headless Mode: ${HEADLESS}"
echo "========================="

echo "=== Setting up Python virtual environment ==="
python3 -m venv .venv
source .venv/bin/activate
which python
python --version

echo "=== Installing dependencies ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Creating reports directory ==="
mkdir -p reports/allure-results
mkdir -p reports/screenshots

echo "=== Preparing test execution ==="
# Determine parallel workers
if [ "$PARALLEL_WORKERS" = "auto" ]; then
    WORKERS_FLAG="-n auto"
else
    WORKERS_FLAG="-n $PARALLEL_WORKERS"
fi

# Build pytest command
PYTEST_CMD="pytest -s -v"
PYTEST_CMD="$PYTEST_CMD --env $ENVIRONMENT"
PYTEST_CMD="$PYTEST_CMD --alluredir=reports/allure-results"
PYTEST_CMD="$PYTEST_CMD --clean-alluredir"
PYTEST_CMD="$PYTEST_CMD --browser=$BROWSER"

# Add parallel workers if more than 1
if [ "$PARALLEL_WORKERS" != "1" ]; then
    PYTEST_CMD="$PYTEST_CMD $WORKERS_FLAG"
fi




# ***************************************
# ***** SPECIFY TEST MARKERS / TAGS *****
PYTEST_CMD="$PYTEST_CMD -m orangehrm"
# ***************************************

echo "=== Running Selenium tests with command ==="
# Execute the command
eval $PYTEST_CMD

echo "=== Test execution completed ==="
ls -la reports/allure-results/

# Generate summary
echo "=== Test Summary ==="
echo "Tests executed on: $(date)"
echo "Branch: ${BRANCH_NAME}"
echo "Browser: ${BROWSER}"
echo "Environment: ${ENVIRONMENT}"
echo "Parallel Workers: ${PARALLEL_WORKERS}"
echo "Test Markers: orangehrm"
echo "===================="