pipeline{
    agent any
    environment{
        DATABASE_URI=...
    }
    stages{
        stage('Debug'){
            steps{
                sh "docker-compose config"
            }
        }
    }

}