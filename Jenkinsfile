pipeline {
  agent any
  environment {
    APP_NAME = "fastapi-crud"
    DOCKER_IMAGE = "vipunsanjana/fastapi-crud:1"
    REGISTRY_CREDENTIALS = credentials('docker-cred')
    GIT_REPO_NAME = "Fastapi-K8s-Jenkins-AgroCD-EC2-SonarQube-Docker"
    GIT_USER_NAME = "vipunsanjana"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install Dependencies') {
      steps {
        script {
          docker.image('python:3.11-slim').inside('--user root') {
            sh '''
              pip install --upgrade pip
              pip install -r requirements.txt
            '''
          }
        }
      }
    }

    stage('Build and Push Docker Image') {
      steps {
        script {
          sh "docker build -t ${DOCKER_IMAGE} ."
          def dockerImage = docker.image("${DOCKER_IMAGE}")
          docker.withRegistry('https://index.docker.io/v1/', 'docker-cred') {
            dockerImage.push()
          }
        }
      }
    }

    stage('Update Deployment File') {
      steps {
        withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
          sh '''
            git config user.email "vipunsanjana34@gmail.com"
            git config user.name "vipunsanjana"
            sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" k8s/deployment.yaml
            git add k8s/deployment.yaml
            git commit -m "Update deployment to image tag ${BUILD_NUMBER}"
            git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
          '''
        }
      }
    }
  }

  post {
    success {
      echo "✅ Build, scan, and deploy pipeline finished successfully."
    }
    failure {
      echo "❌ Pipeline failed. Check the error logs."
    }
  }
}
