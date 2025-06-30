pipeline {
  agent any

  environment {
    APP_NAME = "fastapi-crud"
    DOCKER_IMAGE = "vipunsanjana/fastapi-crud:one"
    REGISTRY_CREDENTIALS = credentials('dockerhub-creds')
    GIT_REPO_NAME = "Fastapi-K8s-Jenkins-AgroCD-EC2-SonarQube-Docker"
    GIT_USER_NAME = "vipunsanjana"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build and Push Docker Image') {
      steps {
        script {
          // Build Docker image (Dockerfile installs dependencies)
          sh "docker build -t ${DOCKER_IMAGE} ."

          def dockerImage = docker.image("${DOCKER_IMAGE}")

          // Login & push image to Docker Hub
          docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
            dockerImage.push()
          }
        }
      }
    }

    stage('Update Deployment File') {
      environment {
        GIT_REPO_NAME = "Fastapi-K8s-Jenkins-AgroCD-EC2-SonarQube-Docker"
        GIT_USER_NAME = "vipunsanjana"
      }
      steps {
        withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
          sh '''
            git config user.email "vipunsanjana34@gmail.com"
            git config user.name "vipunsanjana"
            sed -i "s/replaceImageTag/one/g" k8s/deployment.yaml
            git add k8s/deployment.yaml
            git commit -m "Update deployment to image tag one"
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
