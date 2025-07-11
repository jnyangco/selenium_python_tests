pipeline {
    agent none
    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))  // ← Added: Keep only 10 builds
        timeout(time: 2, unit: 'HOURS')                 // ← Added: 2-hour timeout safety
    }

    parameters {
        // Basic Parameters
        choice(choices: ['docker', 'local'], description: 'Test environment', name: 'ENVIRONMENT')
        choice(choices: ['chrome', 'firefox', 'edge'], description: 'Browser', name: 'BROWSER')
        choice(choices: ['develop', 'main', 'staging'], description: 'Branch', name: 'BRANCH_NAME')
        choice(choices: ['24', 'auto', '4', '8', '12', '16'], description: 'Parallel workers', name: 'PARALLEL_WORKERS')

        // Test Suite Selection
        booleanParam(defaultValue: true, description: 'Run SauceDemo tests', name: 'RUN_SAUCEDEMO')
        booleanParam(defaultValue: true, description: 'Run OrangeHRM tests', name: 'RUN_ORANGEHRM')
        booleanParam(defaultValue: true, description: 'Run Leetcode tests', name: 'RUN_LEETCODE')
        booleanParam(defaultValue: true, description: 'Run Banking tests', name: 'RUN_BANKING')
    }

    stages {
        stage('Setup') {
            agent any
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

Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Started: ${new Date()}
                    """
                }
            }
        }

        stage('Run Tests in True Parallel') {
            parallel {
                stage('SauceDemo Tests') {
                    agent any
                    when { expression { params.RUN_SAUCEDEMO } }
                    steps {
                        script {
                            echo "🍅 SauceDemo starting on agent: ${env.NODE_NAME} at: ${new Date()}"
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                build job: 'Selenium_Python_Tests_Saucedemo'
                            }
                            echo "🍅 SauceDemo finished on agent: ${env.NODE_NAME} at: ${new Date()}"
                        }
                    }
                    post {
                        failure {
                            echo "❌ SauceDemo tests failed - check job logs"
                        }
                        success {
                            echo "✅ SauceDemo tests passed"
                        }
                    }
                }

                stage('OrangeHRM Tests') {
                    agent any
                    when { expression { params.RUN_ORANGEHRM } }
                    steps {
                        script {
                            echo "🍊 OrangeHRM starting on agent: ${env.NODE_NAME} at: ${new Date()}"
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                build job: 'Selenium_Python_Tests_Orangehrm'
                            }
                            echo "🍊 OrangeHRM finished on agent: ${env.NODE_NAME} at: ${new Date()}"
                        }
                    }
                    post {
                        failure {
                            echo "❌ OrangeHRM tests failed - check job logs"
                        }
                        success {
                            echo "✅ OrangeHRM tests passed"
                        }
                    }
                }

                stage('Leetcode Tests') {
                    agent any
                    when { expression { params.RUN_LEETCODE } }
                    steps {
                        script {
                            echo "💻 Leetcode starting on agent: ${env.NODE_NAME} at: ${new Date()}"
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                build job: 'Selenium_Python_Tests_Leetcode'
                            }
                            echo "💻 Leetcode finished on agent: ${env.NODE_NAME} at: ${new Date()}"
                        }
                    }
                    post {
                        failure {
                            echo "❌ Leetcode tests failed - check job logs"
                        }
                        success {
                            echo "✅ Leetcode tests passed"
                        }
                    }
                }

                stage('Banking Tests') {
                    agent any
                    when { expression { params.RUN_BANKING } }
                    steps {
                        script {
                            echo "🏦 Banking starting on agent: ${env.NODE_NAME} at: ${new Date()}"
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                build job: 'Selenium_Python_Tests_Banking', parameters: [
                                    string(name: 'BRANCH_NAME', value: params.BRANCH_NAME),
                                    string(name: 'BROWSER', value: params.BROWSER),
                                    string(name: 'ENVIRONMENT', value: params.ENVIRONMENT),
                                    string(name: 'PARALLEL_WORKERS', value: params.PARALLEL_WORKERS),
                                    booleanParam(name: 'HEADLESS', value: false),
                                    string(name: 'TEST_PATH', value: 'tests/banking/')
                                ]
                            }
                            echo "🏦 Banking finished on agent: ${env.NODE_NAME} at: ${new Date()}"
                        }
                    }
                    post {
                        failure {
                            echo "❌ Banking tests failed - check job logs"
                        }
                        success {
                            echo "✅ Banking tests passed"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Calculate execution summary
                def executedJobs = []
                if (params.RUN_SAUCEDEMO) executedJobs << 'SauceDemo'
                if (params.RUN_ORANGEHRM) executedJobs << 'OrangeHRM'
                if (params.RUN_LEETCODE) executedJobs << 'Leetcode'
                if (params.RUN_BANKING) executedJobs << 'Banking'

                echo """
📊 Build Summary:
=================
Job: ${env.JOB_NAME} #${env.BUILD_NUMBER}
Result: ${currentBuild.result ?: 'SUCCESS'}
Duration: ${currentBuild.durationString}
Started: ${currentBuild.startTimeInMillis ? new Date(currentBuild.startTimeInMillis) : 'Unknown'}
Finished: ${new Date()}

Test Suites Executed: ${executedJobs.join(', ') ?: 'None'}
Total Selected: ${executedJobs.size()} out of 4 available

Configuration:
- Environment: ${params.ENVIRONMENT}
- Browser: ${params.BROWSER}
- Branch: ${params.BRANCH_NAME}
- Workers: ${params.PARALLEL_WORKERS}

Individual Results:
SauceDemo: ${params.RUN_SAUCEDEMO ? 'Executed (Non-param)' : 'Skipped'}
OrangeHRM: ${params.RUN_ORANGEHRM ? 'Executed (Non-param)' : 'Skipped'}
Leetcode: ${params.RUN_LEETCODE ? 'Executed (Non-param)' : 'Skipped'}
Banking: ${params.RUN_BANKING ? 'Executed (Parameterized)' : 'Skipped'}
=================
                """
            }
        }

        success {
            script {
                echo """
✅ All selected tests completed successfully!
Duration: ${currentBuild.durationString}
Environment: ${params.ENVIRONMENT}
Browser: ${params.BROWSER}

🎉 Parallel execution working perfectly with 12 executors!
                """
            }
        }

        failure {
            script {
                echo """
❌ Some tests failed!
Duration: ${currentBuild.durationString}

🔍 Next Steps:
1. Check individual job console logs for details
2. Review screenshots in failed job artifacts
3. Check test reports for specific failure details

Environment: ${params.ENVIRONMENT}
Browser: ${params.BROWSER}
                """
            }
        }

        unstable {
            script {
                echo """
⚠️ Tests completed with some failures.
Duration: ${currentBuild.durationString}

Some test suites failed but execution continued.
Review individual job results for details.

Environment: ${params.ENVIRONMENT}
Browser: ${params.BROWSER}
                """
            }
        }
    }
}