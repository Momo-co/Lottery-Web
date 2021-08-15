pipeline{
    agent any
    environment{
        DATABASE_URI= credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS= credentials("DOCKERHUB_CREDENTIALS")
        SECRET_KEY= credentials("SECRET_KEY")
        USER= credentials("USER")
    }
    stages{
        stage('Setup'){
            sh "bash scripts/setup.sh"
        }
        stage('Test App'){
            sh "bash scripts/test.sh"
        }
        stage('Build Image'){
            sh "bash scripts/build.sh"
        }
        stage('Deploy Stack'){
            sh "bash scripts/deploy.sh"
        }
    }

}