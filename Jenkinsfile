pipeline {
  agent any
  
  triggers {
    pollSCM('H/2 * * * *')
  }
  
  environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
    DOCKER_IMAGE = "${env.DOCKERHUB_CREDENTIALS_USR}/jenkins-python-game"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          def sha = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
          def img = "${env.DOCKER_IMAGE}:${sha}"
          sh "docker build -t ${img} ."
          sh "docker tag ${img} ${env.DOCKER_IMAGE}:latest"
          env.IMAGE = img
        }
      }
    }

    stage('Run tests') {
      steps {
        script {
          sh "docker run --rm ${env.IMAGE} python -m pytest tests/ -v"
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push $IMAGE'
          sh 'docker push ${env.DOCKER_IMAGE}:latest'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'README.md', fingerprint: true
    }
  }
}
