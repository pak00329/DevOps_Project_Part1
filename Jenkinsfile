pipeline {
    agent any

    stages {
        stage('Run web_') {
            steps {
                script{
                    // Get some code from a GitHub repository
                    //echo "workspace directory is ${workspace}"
                    sh 'python3 ${WORKSPACE}/build_test_file.py'
                }

            }

            
            }
        }
    }
