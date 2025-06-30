# FastAPI CRUD App

A modular FastAPI application demonstrating CRUD operations on items, designed for production-grade DevOps pipelines with Kubernetes, Jenkins, Argo CD, and SonarQube.

---

## 🚀 Features

- ✅ RESTful CRUD API for item management (`/items`)
- ✅ Modular structure with FastAPI + Pydantic
- ✅ Dockerized using virtual environments inside container
- ✅ Jenkins pipeline with SonarQube static code analysis
- ✅ Kubernetes-native deployment using Argo CD
- ✅ Hosted on AWS EC2 with Minikube cluster
- ✅ Swagger UI available at `/docs`

---

## 📦 Technologies Used

- **FastAPI** – Python-based web framework
- **Pydantic** – Data validation
- **Docker** – Containerization
- **Jenkins** – CI pipeline
- **SonarQube** – Static code quality checks
- **Kubernetes (Minikube)** – Container orchestration
- **Argo CD** – GitOps deployment
- **AWS EC2 (Ubuntu)** – Hosting environment

---

## 🧱 Project Structure

- fastapi-crud/
- ├── app/
- │   ├── main.py                # Entry point for FastAPI app
- │   ├── models.py              # Pydantic data models
- │   ├── db.py                  # In-memory DB or database logic
- │   └── routes.py              # API route definitions
- ├── requirements.txt           # Python dependencies
- ├── Dockerfile                 # Docker build file (with venv support)
- ├── Jenkinsfile                # Jenkins pipeline definition
- ├── k8s/
- │   ├── deployment.yaml        # Kubernetes Deployment manifest
- │   └── service.yaml           # Kubernetes Service manifest
- ├── .gitignore                 # Git ignore rules
- ├── .dockerignore              # Docker build ignore rules
- └── README.md                  # Project documentation

---

## 🖥️ How the Pipeline Works

1. **Developer** pushes to the `main` branch.
2. **Jenkins** (on EC2) is triggered:
   - Runs tests and lints
   - Performs static code analysis via **SonarQube**
   - Builds Docker image and pushes to container registry
3. **Argo CD** automatically syncs Kubernetes manifests from Git
4. App is deployed on **Minikube cluster** inside EC2.
5. Access API via:  
   `http://<your-ec2-public-ip>:<node-port>/docs`

---

## 🔧 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | `/items/`        | Create a new item   |
| GET    | `/items/{id}`    | Get item by ID      |
| PUT    | `/items/{id}`    | Update existing item|
| DELETE | `/items/{id}`    | Delete item by ID   |

Swagger UI:  
➡️ `http://<your-ec2-ip>:<node-port>/docs`

---

## 🐳 Docker Commands (Local Test)

```bash
docker build -t fastapi-crud .
docker run -p 8000:8000 fastapi-crud
