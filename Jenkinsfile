pipeline {
    agent any

    stages {
       
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the container with docker-compose
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Spark Job') {
            steps {
                script {
                    // Tail the logs of the Spark job to ensure it's running
                    sh 'docker-compose logs -f'
                }
            }
        }
    }

    post {
    	success {
            script {
                // Notify success to Slack
                slackSend channel: '#spark-alerts', color: 'good', message: "Build SUCCESSFUL: ${env.JOB_NAME} [${env.BUILD_NUMBER}] (${env.BUILD_URL})"
            }
        }
        failure {
            script {
                // Notify failure to Slack
                slackSend channel: '#spark-alerts', color: 'danger', message: "Build FAILED: ${env.JOB_NAME} [${env.BUILD_NUMBER}] (${env.BUILD_URL})"
            }
        }
        always {
            script {
                // Stop and remove containers after the job
                sh 'docker-compose down'
            }
        }
    }
}
