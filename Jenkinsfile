pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                agent {
                    label 'master'
                }
            }
            steps {
                sh 'pwd'
            }
        }
    }
}
