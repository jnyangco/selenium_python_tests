# Jenkins Job Setup Guide

# =========================================================
1. chmod +x jenkins/jobs/run_banking_job.sh
2. add the code inside the run_banking_job.sh
3. create jenkins job with the following:
General Section: ✅ Check "This project is parameterized"

Add String Parameters:
BRANCH_NAME: develop, etc...
BROWSER: chrome, firefox, edge, safari
ENVIRONMENT: docker, local
PARALLEL_WORKERS: 24, auto, 4, 8, 12, 16, 20
HEADLESS: checkbox - true/false

4. Step 3: Configure Source Code
Source Code Management:
✅ Select Git
Repository URL: [your-git-repository-url]
Branch Specifier: */${BRANCH_NAME}
Credentials: Select your Git credentials

5. Step 4: Configure Build Script
Build Section:
Click "Add build step"
Select "Execute shell"
Enter this script:

# IMPORTANT
bash#!/bin/bash
set -e
chmod +x jenkins/jobs/run_[testsuite]_job.sh
./jenkins/jobs/run_[testsuite]_job.sh


# =========================================================
This guide explains how to create and configure Jenkins jobs to use the shell scripts in this repository.

## Prerequisites

- Jenkins server with access to this Git repository
- Git credentials configured in Jenkins
- Python 3 and pip available on Jenkins agents

## Creating a New Jenkins Job

### Step 1: Create the Job

1. **Log into Jenkins** and go to the dashboard
2. **Click "New Item"**
3. **Enter job name**: `Selenium_Python_Tests_[TestSuite]`
   - Example: `Selenium_Python_Tests_Banking`
4. **Select "Freestyle project"**
5. **Click "OK"**

### Step 2: Configure Parameters

In the job configuration page:

#### General Section:
- ✅ Check **"This project is parameterized"**

#### Add String Parameters:
| Parameter Name | Default Value | Description |
|----------------|---------------|-------------|
| `BRANCH_NAME` | `develop` | Git branch to test |
| `BROWSER` | `chrome` | Browser (chrome/firefox/edge) |
| `ENVIRONMENT` | `docker` | Test environment (docker/local) |
| `PARALLEL_WORKERS` | `auto` | Parallel workers (auto/1/4/8/12/16/24) |

#### Add Boolean Parameter:
| Parameter Name | Default Value | Description |
|----------------|---------------|-------------|
| `HEADLESS` | `false` | Run in headless mode |

### Step 3: Configure Source Code

#### Source Code Management:
- ✅ Select **Git**
- **Repository URL**: `[your-git-repository-url]`
- **Branch Specifier**: `*/${BRANCH_NAME}`
- **Credentials**: Select your Git credentials

### Step 4: Configure Build Script

#### Build Section:
1. **Click "Add build step"**
2. **Select "Execute shell"**
3. **Enter this script**:

```bash
#!/bin/bash
set -e
chmod +x jenkins/jobs/run_[testsuite]_job.sh
./jenkins/jobs/run_[testsuite]_job.sh
```

**Replace `[testsuite]` with your actual test suite name:**
- Banking: `jenkins/jobs/run_banking_job.sh`
- SauceDemo: `jenkins/jobs/run_saucedemo_job.sh`
- OrangeHRM: `jenkins/jobs/run_orangehrm_job.sh`
- Leetcode: `jenkins/jobs/run_leetcode_job.sh`

### Step 5: Configure Post-Build Actions

#### Archive Artifacts:
- **Files to archive**: `reports/**/*`
- ✅ Check **"Archive artifacts only if build is successful"**

#### Publish HTML Reports:
- **HTML directory to archive**: `reports`
- **Index page**: `report.html`
- **Report title**: `[TestSuite] Test Report`

### Step 6: Save and Test

1. **Click "Save"**
2. **Click "Build with Parameters"**
3. **Verify parameters appear correctly**
4. **Run a test build**

## Available Test Suites

| Test Suite | Script Path | Test Markers |
|------------|-------------|--------------|
| Banking | `jenkins/jobs/run_banking_job.sh` | `banking` |
| SauceDemo | `jenkins/jobs/run_saucedemo_job.sh` | `saucedemo` |
| OrangeHRM | `jenkins/jobs/run_orangehrm_job.sh` | `orangehrm` |
| Leetcode | `jenkins/jobs/run_leetcode_job.sh` | `leetcode` |

## Jenkins Build Script Template

For any new test suite, use this template in the Jenkins job build section:

```bash
#!/bin/bash
set -e
chmod +x jenkins/jobs/run_[testsuite]_job.sh
./jenkins/jobs/run_[testsuite]_job.sh
```

## Running Jobs

### Standalone Execution:
1. Go to the specific job page
2. Click "Build with Parameters"
3. Set your desired parameters
4. Click "Build"

### Orchestrator Execution:
- Jobs are automatically called by the main orchestrator pipeline
- Parameters are passed from the orchestrator to individual jobs

## Troubleshooting

### Common Issues:

**Script not executable:**
```bash
# Fix: Ensure chmod +x is in the Jenkins build script
chmod +x jenkins/jobs/run_banking_job.sh
```

**Parameters not available:**
- Verify "This project is parameterized" is checked
- Ensure all 5 parameters are configured correctly

**Git branch issues:**
- Check branch specifier is `*/${BRANCH_NAME}`
- Verify Git credentials are configured

**Reports not archiving:**
- Ensure post-build actions are configured
- Check `reports/` directory is created by the test script

### Testing Locally:

Before running in Jenkins, test scripts locally:

```bash
# Set environment variables
export BRANCH_NAME="develop"
export BROWSER="chrome"
export ENVIRONMENT="local"
export PARALLEL_WORKERS="1"
export HEADLESS="false"

# Run script
chmod +x jenkins/jobs/run_banking_job.sh
./jenkins/jobs/run_banking_job.sh
```

## Best Practices

1. **Test locally first** before running in Jenkins
2. **Use descriptive job names** that include the test suite
3. **Set sensible defaults** for parameters
4. **Archive artifacts** for debugging failed tests
5. **Keep scripts simple** and focused on single test suites

## Configuration Summary

Each Jenkins job should have:
- ✅ 5 parameters (4 string + 1 boolean)
- ✅ Git source with parameterized branch
- ✅ Simple 3-line build script
- ✅ Post-build artifact archiving
- ✅ HTML report publishing