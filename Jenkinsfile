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