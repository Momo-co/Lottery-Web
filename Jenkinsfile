pipeline{
    agent any
    environment{
        DATABASE_URI= credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS= credentials("DOCKERHUB_CREDENTIALS")
        SECRET_KEY= credentials("SECRET_KEY")
        USER= credentials("USER")
    }
    stages{
        stage('Debug '){
            steps{
                sh "docker-compose config"
            }
        }
        stage('Build Docker-Compose'){
            steps{
                sh "docker-compose build --parallel"
            }
        }
    }

}