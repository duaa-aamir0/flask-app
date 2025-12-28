pipeline {
    agent any
    
    parameters {
        choice(
            name: 'VERSION',
            choices: ['1.1.0', '1.2.0', '1.3.0'],
            description: 'Version to deploy on production'
        )
        booleanParam(
            name: 'executeTests',
            defaultValue: true,
            description: 'Run tests before deploy'
        )
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Test') {
            when {
                expression {
                    params.executeTests
                }
            }
            steps {
                echo 'Testing...'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying version ${params.VERSION}..."
            }
        }
    }

    post {
        always {
            echo "Pipeline completed!"
        }
        failure {
            echo "Post action: build failed."
        }
    }
}
