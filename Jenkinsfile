pipeline{
    agent any
    environment{
        DATABASE_URI= credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS= credentials("DOCKERHUB_CREDENTIALS")
        SECRET_KEY= credentials("DOCKERHUB_CREDENTIALS")
        USER= credentials("DOCKERHUB_CREDENTIALS")
    }
    stages{
        stage('Install Dependencies'){
            steps{
                sh "bash scripts/setup.sh"
            }
        }
        stage('Test App'){
            steps{
                sh "bash scripts/test.sh"
            }
        }
        stage('Build Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('Deploy Stack'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
    }

}