pipeline {
    agent any
    
    parameters{
        string(name: 'VERSION', defaultValue:'', description:'version to deploy on production')
        choice(name: 'VERSION', choices:['1.1.0', '1.2.0', '1.3.0'], description:'')
        booleanParam(name:'executeTests', defaultValue: true, description:'')
    }

    environment{
        NEW_VERSION = '1.3.0'
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            when{
                expression{
                    param.executeTests
                }
            }
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                }
        }
    }

    post {
        always {
            echo "Pipeline completed!"
        }
        failure {
            echo "post action if build failed."
        }
    }

}
