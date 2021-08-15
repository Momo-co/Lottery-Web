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
        stage('Debug Docker-Hub'){
            steps{
                sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
            }
        }
        stage('Debug Docker-Compose'){
            steps{
                sh "docker-compose build --parallel"
            }
        }
    }

}