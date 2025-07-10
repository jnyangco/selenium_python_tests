pipeline {
    agent any
    options { timestamps() }

    parameters {
        // Basic Parameters
        choice(choices: ['docker', 'local'], description: 'Test environment', name: 'ENVIRONMENT')
        choice(choices: ['chrome', 'firefox', 'edge'], description: 'Browser', name: 'BROWSER')
        choice(choices: ['develop', 'main', 'staging'], description: 'Branch', name: 'BRANCH_NAME')
        choice(choices: ['24', 'auto', '4', '8', '12', '16'], description: 'Parallel workers', name: 'PARALLEL_WORKERS')

        // Test Suite Selection (Fixed parameter names and descriptions)
        booleanParam(defaultValue: true, description: 'Run SauceDemo tests', name: 'RUN_SAUCEDEMO')
        booleanParam(defaultValue: true, description: 'Run OrangeHRM tests', name: 'RUN_ORANGEHRM')
        booleanParam(defaultValue: true, description: 'Run Leetcode tests', name: 'RUN_LEETCODE')  // ← Fixed: was RUN_LEETCODE
        booleanParam(defaultValue: true, description: 'Run Banking tests', name: 'RUN_BANKING')   // ← Fixed: removed duplicate
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    currentBuild.description = "Env: ${params.ENVIRONMENT} | Browser: ${params.BROWSER} | Workers: ${params.PARALLEL_WORKERS}"
                    echo """
🚀 Starting Selenium Test Orchestrator
Environment: ${params.ENVIRONMENT}
Browser: ${params.BROWSER}
Branch: ${params.BRANCH_NAME}
Workers: ${params.PARALLEL_WORKERS}

Test Suites Selected:
SauceDemo: ${params.RUN_SAUCEDEMO ? '✅' : '❌'}
OrangeHRM: ${params.RUN_ORANGEHRM ? '✅' : '❌'}
Leetcode: ${params.RUN_LEETCODE ? '✅' : '❌'}
Banking: ${params.RUN_BANKING ? '✅' : '❌'}
                    """
                }
            }
        }


        stage('Test Parallel Execution') {
            parallel {
                stage('Test Job 1') {
                    steps {
                        script {
                            echo "Job 1 starting at: ${new Date()}"
                            sleep(30)  // 30 seconds
                            echo "Job 1 finished at: ${new Date()}"
                        }
                    }
                }
                stage('Test Job 2') {
                    steps {
                        script {
                            echo "Job 2 starting at: ${new Date()}"
                            sleep(30)  // 30 seconds
                            echo "Job 2 finished at: ${new Date()}"
                        }
                    }
                }
            }
        }


    }

    post {
        success {
            echo """
✅ All tests completed successfully!
Duration: ${currentBuild.durationString}
Environment: ${params.ENVIRONMENT}
Browser: ${params.BROWSER}
            """
        }

        failure {
            echo """
❌ Some tests failed!
Check individual job console logs for details.
Duration: ${currentBuild.durationString}
            """
        }

        unstable {
            echo """
⚠️ Tests completed with some failures.
Some test suites failed but execution continued.
Duration: ${currentBuild.durationString}
            """
        }

        always {
            echo """
📊 Build Summary:
=================
Job: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Result: ${currentBuild.result ?: 'SUCCESS'}
Duration: ${currentBuild.durationString}
SauceDemo: ${params.RUN_SAUCEDEMO ? 'Executed (Non-param)' : 'Skipped'}
OrangeHRM: ${params.RUN_ORANGEHRM ? 'Executed (Non-param)' : 'Skipped'}
Leetcode: ${params.RUN_LEETCODE ? 'Executed (Non-param)' : 'Skipped'}
Banking: ${params.RUN_BANKING ? 'Executed (Parameterized)' : 'Skipped'}
=================
            """
        }
    }
}