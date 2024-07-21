pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *') // Poll SCM every 30 minutes
    stages {
        stage('run backend server') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'nohup python3 rest_app.py&'
                }
            }
        }
        
        stage('run frontend server') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'nohup python3 web_app.py&'
                }
            }
        }
        
        stage('run frontend_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python3 frontend_testing.py'
                }
            }
        }
        
        stage('run backend_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python3 backend_testing.py'
                }
            }
        }
        
        stage('run combined_testing') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python3 combined_testing.py'
                }
            }
        }
        
        stage('run clean_environment') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    //sh 'python3 ${WORKSPACE}/build_test_file.py'
                    sh 'python3 clean_environment.py'
                }
            }
        }
    }
}
