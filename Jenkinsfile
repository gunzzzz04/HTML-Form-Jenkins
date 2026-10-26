pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Configure Pipeline script from SCM with your GitHub repository.
                checkout scm
            }
        }
        stage('Verify HTML Form') {
            steps {
                bat 'python --version'
                bat 'python -m unittest discover -s tests -p "test_*.py" -v'
            }
        }
    }
    post {
        success { echo 'HTML form checks passed.' }
        failure { echo 'Pipeline failed. Review the console output and test failures.' }
    }
}
