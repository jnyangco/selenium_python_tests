pipeline {
    agent any
    options { timestamps() }

    parameters {
        // Basic Parameters
        choice(choices: ['docker', 'local'], description: 'Test environment', name: 'ENVIRONMENT')
        choice(choices: ['chrome', 'firefox', 'edge'], description: 'Browser', name: 'BROWSER')
        choice(choices: ['main', 'develop', 'staging'], description: 'Branch', name: 'BRANCH_NAME')
        choice(choices: ['auto', '4', '8', '12', '16', '24'], description: 'Parallel workers', name: 'PARALLEL_WORKERS')

        // Test Suite Selection (Simple)
        booleanParam(defaultValue: true, description: 'Run SauceDemo tests', name: 'RUN_SAUCEDEMO')
        booleanParam(defaultValue: true, description: 'Run OrangeHRM tests', name: 'RUN_ORANGEHRM')
        booleanParam(defaultValue: true, description: 'Run Banking tests', name: 'RUN_BANKING')
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
                    """
                }
            }
        }

        stage('Run Tests') {
            parallel {
                stage('SauceDemo Tests') {
                    when { expression { params.RUN_SAUCEDEMO } }
                    steps {
                        script {
                            echo '🍅 Running SauceDemo Tests (Non-parameterized)...'
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                // Non-parameterized job - no parameters passed
                                build job: 'Selenium_Python_Tests_Saucedemo'  // ← Change to your actual job name
                            }
                        }
                    }
                }

                stage('OrangeHRM Tests') {
                    when { expression { params.RUN_ORANGEHRM } }
                    steps {
                        script {
                            echo '🍊 Running OrangeHRM Tests (Non-parameterized)...'
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                // Non-parameterized job - no parameters passed
                                build job: 'OrangeHRM_Tests'  // ← Change to your actual job name
                            }
                        }
                    }
                }

                stage('Banking Tests') {
                    when { expression { params.RUN_BANKING } }
                    steps {
                        script {
                            echo '🏦 Running Banking Tests (Parameterized)...'
                            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                                // Parameterized job - passes parameters from orchestrator
                                build job: 'Banking_Tests', parameters: [  // ← Change to your actual job name
                                    string(name: 'BRANCH_NAME', value: params.BRANCH_NAME),
                                    string(name: 'BROWSER', value: params.BROWSER),
                                    string(name: 'ENVIRONMENT', value: params.ENVIRONMENT),
                                    string(name: 'PARALLEL_WORKERS', value: params.PARALLEL_WORKERS),
                                    booleanParam(name: 'HEADLESS', value: false),
                                    string(name: 'TEST_PATH', value: 'tests/banking/')
                                ]
                            }
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
                Banking: ${params.RUN_BANKING ? 'Executed (Parameterized)' : 'Skipped'}
                =================
            """
        }
    }
}