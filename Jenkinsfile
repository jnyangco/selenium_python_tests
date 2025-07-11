pipeline {
    agent none
    stages {
        stage('Test Parallel') {
            parallel {
                stage('Test A') {
                    agent any
                    steps {
                        echo "🅰️ Starting at: ${new Date()}"
                        sleep(20)
                        echo "🅰️ Finished at: ${new Date()}"
                    }
                }
                stage('Test B') {
                    agent any
                    steps {
                        echo "🅱️ Starting at: ${new Date()}"
                        sleep(20)
                        echo "🅱️ Finished at: ${new Date()}"
                    }
                }
            }
        }
    }
}