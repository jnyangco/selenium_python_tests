// Jenkinsfile.smoke - Quick smoke test pipeline
pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13.3'
        VENV_NAME = '.venv'
        BROWSER = 'chrome'
        ENV = 'docker'
    }

    stages {
        stage('Quick Setup') {
            steps {
                script {
                    echo "🚀 Quick Test Setup..."
                    sh '''
                        python3 -m venv ${VENV_NAME}
                        source ${VENV_NAME}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Start Selenium Grid') {
            steps {
                script {
                    echo "🐳 Starting Selenium Grid..."
                    sh '''
                        // docker-compose down || true
                        // docker-compose up -d
                        // timeout 30 bash -c 'until curl -sSf http://localhost:4444/wd/hub/status > /dev/null; do sleep 2; done'
                    '''
                }
            }
        }

        stage('Smoke Tests') {
            parallel {
                stage('Login Smoke Tests') {
                    steps {
                        script {
                            sh '''
                                . ${VENV_NAME}/bin/activate
                                pytest -m "smoke and login" \
                                    --browser=${BROWSER} \
                                    --env=${ENV} \
                                    -v \
                                    --alluredir=reports/allure-results/smoke-login \
                                    --html=reports/smoke_login_report.html \
                                    --self-contained-html
                            '''
                        }
                    }
                }

//                 stage('UI Smoke Tests') {
//                     steps {
//                         script {
//                             sh '''
//                                 . ${VENV_NAME}/bin/activate
//                                 pytest -m "smoke and ui" \
//                                     --browser=${BROWSER} \
//                                     --env=${ENV} \
//                                     -v \
//                                     --alluredir=reports/allure-results/smoke-ui \
//                                     --html=reports/smoke_ui_report.html \
//                                     --self-contained-html
//                             '''
//                         }
//                     }
//                 }

            }
        }
    }

    post {
        always {
            script {
                // Publish reports
//                 publishHTML([
//                     allowMissing: false,
//                     alwaysLinkToLastBuild: true,
//                     keepAll: true,
//                     reportDir: 'reports',
//                     reportFiles: '*.html',
//                     reportName: 'Smoke Test Reports'
//                 ])

                // Clean up
                sh 'docker-compose down || true'
                sh 'rm -rf ${VENV_NAME}'
            }
        }
        failure {
//             emailext (
//                 subject: "🚨 SMOKE TESTS FAILED: ${env.JOB_NAME}",
//                 body: "Critical smoke tests failed! Immediate attention required.",
//                 to: "team@company.com"
//             )
        }
    }
}