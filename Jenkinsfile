pipeline {
  agent any

  environment {
    APP_NAME = "fastapi-crud"
    DOCKER_IMAGE = "vipunsanjana/fastapi-crud"
    IMAGE_TAG = "one"
    //SONAR_URL = "http://34.201.116.83:9000"
    FULL_IMAGE = "${DOCKER_IMAGE}:${IMAGE_TAG}"
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
    
    // stage('Static Code Analysis') {
    //   steps {
    //     withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_AUTH_TOKEN')]) {
    //       script {
    //         sh '''
    //           sonar-scanner \
    //             -Dsonar.projectKey=fastapi-crud \
    //             -Dsonar.sources=app \
    //             -Dsonar.python.version=3.11 \
    //             -Dsonar.host.url=${SONAR_URL} \
    //             -Dsonar.login=${SONAR_AUTH_TOKEN}
    //         '''
    //       }
    //     }
    //   }
    // }

    stage('Build Docker Image') {
      steps {
        script {
          sh "docker build -t ${FULL_IMAGE} ."
        }
      }
    }

    stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh '''
                            echo "Logging in to Docker Hub..."
                            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                            docker push ${FULL_IMAGE}
                            echo "Docker image ${FULL_IMAGE} pushed successfully."
                        '''
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
            sed -i "s/replaceImageTag/${IMAGE_TAG}/g" k8/deployment.yaml
            git add k8/deployment.yaml
            git commit -m "Update deployment to image tag ${IMAGE_TAG}"
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
