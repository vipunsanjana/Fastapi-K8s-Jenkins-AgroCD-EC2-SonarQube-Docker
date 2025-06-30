
pipeline {
  agent {
    docker {
      image 'vipunsanjana/python-docker:3.11'
      args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  environment {
    APP_NAME = "fastapi-crud"
    DOCKER_IMAGE = "vipunsanjana/fastapi-crud:one"
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
        sh '''
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
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
