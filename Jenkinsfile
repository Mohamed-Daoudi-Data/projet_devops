pipeline {
    agent any
    
    environment {
        // Nom de l'image Docker, remplacez avec votre nom réel d'image sur Docker Hub ou autre registre
        DOCKER_IMAGE = 'bottle-application'
        // ID des credentials à utiliser pour se connecter au registre Docker, à configurer dans Jenkins
        DOCKER_CREDENTIALS_ID = '123456789'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Récupération du code depuis le SCM configuré
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Construction de l'image Docker avec un tag incluant le numéro de build Jenkins
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Unit Tests') {
            steps {
                // Exécuter les tests unitaires ici, en supposant que vous avez un script ou une commande pour cela
                bat 'echo "Exécuter les commandes de test ici"'
                // Par exemple : sh './run-tests.sh'
            }
        }
        
        stage('Push Image') {
            when {
                // Condition pour pousser l'image, par exemple seulement sur la branche principale
                branch 'main'
            }
            steps {
                script {
                    // Connexion au registre Docker et poussée de l'image
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
                // Déploiement de l'image sur l'environnement cible, ajustez selon votre environnement
                bat 'echo "Exécuter les commandes de déploiement ici"'
                // Par exemple : sh 'kubectl rollout restart deployment/monapp'
            }
        }
    }
    
    post {
        always {
            // Nettoyer les ressources, par exemple les images Docker non taguées
            cleanWs()
        }
        success {
            // Actions à réaliser si le pipeline réussit
            echo 'Le build et le déploiement ont réussi !'
        }
        failure {
            // Actions en cas d'échec du pipeline
            echo 'Le build ou le déploiement ont échoué.'
        }
    }
}