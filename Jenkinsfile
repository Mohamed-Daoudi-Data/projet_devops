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
                    try {
                        docker.withRegistry('https://registry.hub.docker.com/', DOCKER_CREDENTIALS_ID) {
                            docker.image("${DOCKER_IMAGE}:${env.BUILD_NUMBER}").push()
                        }
                        echo 'Image pushed successfully'
                        // Ici, vous pouvez ajouter une notification de succès, par exemple un email ou une notification Slack
                    } catch (Exception e) {
                        echo "Failed to push the Docker image"
                        // Gérer l'erreur comme vous le souhaitez ici, par exemple envoyer une notification d'échec
                        throw e // Rethrow l'exception pour marquer le build comme échoué
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