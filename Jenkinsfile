pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'nohup python web_app.py'
                }
            }
        }
        
        stage('run frontend server') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'nohup python web_app.py'
                }
            }
        }
        
        stage('run frontend_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python frontend_testing.py'
                }
            }
        }
        
        stage('run backend_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python backend_testing.py'
                }
            }
        }
        
        stage('run combined_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python combined_testing.py'
                }
            }
        }
        
        stage('run clean_environment') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python clean_environment.py'
                }
            }
        }
    }
}
