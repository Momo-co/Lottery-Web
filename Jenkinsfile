pipeline{
    agent any
    environment{
        DATABASE_URI= credentials("DATABASE_URI")
    }
    stages{
        stage('Debug'){
            steps{
                sh "docker-compose config"
            }
        }
    }

}