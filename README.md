# 🚀 GenAI EKS Deployment with CI/CD

## 📌 Project Overview
This project demonstrates a complete **end-to-end DevOps pipeline** using AWS and Kubernetes.

The objective is to take an application from:
**code → container → cloud deployment → public access**,  
and automate the entire workflow using CI/CD.

---

## 🧠 Architecture Flow

Developer → GitHub → GitHub Actions → ECR → EKS → LoadBalancer → User

---

## 🧩 Components Explained

### 🟢 Application (Flask API)
A simple backend service exposing a `/health` endpoint.

- Acts as a placeholder for a GenAI service  
- Lightweight and easy to deploy  
- Can be extended to integrate real AI APIs  

---

### 🐳 Docker (Containerization)
The application is packaged into a Docker container.

**Why it's used:**
- Ensures consistent runtime across environments  
- Eliminates dependency issues  
- Required for Kubernetes deployments  

---

### 📦 Amazon ECR (Elastic Container Registry)
A private Docker image registry in AWS.

**Role:**
- Stores built Docker images  
- Acts as a bridge between CI/CD and Kubernetes  
- EKS pulls images from here  

---

### ☸️ Amazon EKS (Kubernetes)
Managed Kubernetes service used to run the application.

**Responsibilities:**
- Runs containers as pods  
- Handles scaling and scheduling  
- Maintains cluster health  

---

### ⚙️ Kubernetes Deployment
Defines how the application should run.

**Controls:**
- Number of replicas  
- Container image  
- Pod configuration  

---

### 🌐 Kubernetes Service (LoadBalancer)
Exposes the application to the internet.

**What it does:**
- Creates an AWS Load Balancer  
- Routes external traffic to pods  
- Provides a public endpoint  

---

### 🔁 GitHub Actions (CI/CD Automation)
Automates the entire DevOps workflow.

**What it replaces:**
- Manual Docker build  
- Manual image push  
- Manual Kubernetes deployment  

**What it does:**
- Builds Docker image on code push  
- Pushes image to ECR  
- Deploys application to EKS  

---

## 🔄 End-to-End Workflow

1. Developer pushes code to GitHub  
2. GitHub Actions pipeline triggers automatically  
3. Docker image is built  
4. Image is pushed to ECR  
5. Kubernetes deployment is updated  
6. EKS pulls the latest image  
7. Application becomes available via LoadBalancer  

---

## 🚧 Challenges & Solutions

### ❌ Pod Pending Issue
Pods were stuck in `Pending` state.

**Cause:**
- Insufficient node capacity (t2.micro instances)

**Solution:**
- Scaled node group to increase capacity  

---

### ❌ CI/CD Docker Build Failure
Pipeline failed due to missing or empty Dockerfile.

**Solution:**
- Ensured Dockerfile was properly committed in GitHub  

---

### ❌ ECR Authentication Issue
Image push initially failed.

**Solution:**
- Configured IAM roles and AWS authentication correctly  

---

## 🎯 Key Learnings

- Difference between manual deployment and CI/CD  
- How Docker, ECR, and EKS integrate  
- Kubernetes scheduling depends on node capacity  
- GitHub Actions automates DevOps workflows  
- IAM roles are critical in AWS architecture  

---

## 💡 Why This Project Matters

This project reflects real-world DevOps practices:

- Containerized applications  
- Cloud-native deployment  
- Automated pipelines  
- Scalable infrastructure  

---

## 🎯 Interview Explanation

> I built a containerized application using Docker, pushed the image to AWS ECR, deployed it on EKS using Kubernetes, and automated the entire pipeline using GitHub Actions.

---

## 🚀 Future Enhancements

- Integrate real GenAI APIs (OpenAI / Bedrock)  
- Add Horizontal Pod Autoscaler (HPA)  
- Use Helm for deployment  
- Implement Blue-Green or Canary deployments  
- Replace static AWS keys with IAM roles (OIDC)  

---

## ⚠️ Cost Note

EKS clusters and LoadBalancers incur cost.  
Always delete resources after testing.

---

## 🧹 Cleanup

To avoid charges, delete the cluster:

eksctl delete cluster --name genai-cluster --region ap-south-1

---

## 👨‍💻 Summary

This project demonstrates:

- End-to-end DevOps pipeline  
- Kubernetes deployment on AWS  
- CI/CD automation using GitHub Actions  
- Real-world troubleshooting and scaling  

---