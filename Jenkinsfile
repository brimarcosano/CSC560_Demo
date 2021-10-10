pipeline {
    agent { docker { image 'ruby' } }
    stages {
        stage('build') {
            steps {
                sh 'ruby --version'
            }
        }
    }
    post {
        always {
            junit 'build/reports/**/*.xml'
        }
    }
}
