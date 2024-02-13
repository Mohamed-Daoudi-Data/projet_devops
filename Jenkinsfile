pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'bottle-application'
        DOCKER_CREDENTIALS_ID = '123456789'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Unit Tests') {
            steps {
                bat 'echo "Exécuter les commandes de test ici"'
            }
        }
        
        stage('Push Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                bat 'echo "Exécuter les commandes de déploiement ici"'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Le build et le déploiement ont réussi !'
        }
        failure {
            echo 'Le build ou le déploiement ont échoué.'
        }
    }
}