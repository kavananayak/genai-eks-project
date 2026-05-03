# GenAI Application Deployment on EKS with CI/CD

## Project Overview
This project demonstrates an end-to-end DevOps pipeline for deploying a GenAI-enabled application on AWS using Kubernetes.

The system includes:
- A backend API with GenAI capability
- Containerization using Docker
- Deployment on Amazon EKS
- CI/CD automation using GitHub Actions
- Secure API key handling using Kubernetes Secrets

---

## Architecture Flow

User to Flask API to OpenAI to Response  
Docker to ECR to EKS  
GitHub to GitHub Actions to CI/CD  

---

## Components Explained

### Application (Flask with GenAI)
The application provides:
- A health endpoint to verify service status
- A generate endpoint to produce AI responses

The API accepts user input, sends it to the OpenAI service, and returns the generated response.

---

### GenAI Integration
The application integrates with the OpenAI API to generate responses dynamically.  
Flask acts as an API layer between the user and the AI service.

---

### Docker
The application is packaged into a Docker container to ensure consistent execution across environments.

---

### Amazon ECR
Amazon Elastic Container Registry is used to store Docker images securely.  
EKS pulls the latest image from ECR during deployment.

---

### Amazon EKS
Amazon Elastic Kubernetes Service is used to run and manage the containerized application.  
It handles pod scheduling, scaling, and cluster management.

---

### Kubernetes Service
A LoadBalancer service is used to expose the application externally.  
It creates an AWS load balancer and provides a public endpoint.

---

### Kubernetes Secrets
The OpenAI API key is stored securely using Kubernetes Secrets.  
The secret is injected into the application as an environment variable.

---

### GitHub Actions
GitHub Actions is used to automate the CI/CD pipeline.

The pipeline performs the following:
- Builds Docker image  
- Pushes image to ECR  
- Creates or updates Kubernetes Secret  
- Deploys application to EKS  

---

## End-to-End Workflow

1. Developer pushes code to GitHub  
2. GitHub Actions pipeline is triggered  
3. Docker image is built and pushed to ECR  
4. Kubernetes Secret is created or updated  
5. Application is deployed to EKS  
6. LoadBalancer exposes the application  
7. Users access the API  

---

## Challenges and Solutions

Pod Pending Issue  
Cause: Insufficient node capacity  
Solution: Increased node group size  

Docker Build Failure  
Cause: Missing Dockerfile  
Solution: Added and committed Dockerfile  

Secret Exposure Issue  
Cause: API key was committed to repository  
Solution: Removed key and used Kubernetes Secrets  

API Quota Error  
Cause: No active OpenAI billing  
Solution: Add billing or usage credits  

---

## Key Learnings

- Difference between build-time and runtime configuration  
- Importance of secure secret management  
- Kubernetes requires redeployment to use updated images  
- Debugging using pod logs is essential  
- CI/CD pipelines reduce manual effort  

---

## Why This Project Matters

This project demonstrates real-world DevOps practices:
- Cloud-native deployment  
- Secure API integration  
- Automated pipelines  
- Scalable infrastructure  

---

## Interview Explanation

I built a GenAI-enabled application integrated with OpenAI APIs, containerized it using Docker, deployed it on EKS, and automated the pipeline using GitHub Actions. I also implemented secure secret management using Kubernetes Secrets.

---

## Future Enhancements

- Add Horizontal Pod Autoscaler  
- Use Helm for deployment  
- Implement blue-green deployment  
- Add monitoring tools  
- Use IAM roles instead of static credentials  

---

## Cost Note

AWS services such as EKS and LoadBalancer incur cost.  
OpenAI API usage also incurs cost.  
Resources should be cleaned up after testing.

---

## Cleanup

eksctl delete cluster --name genai-cluster --region ap-south-1

---

## Summary

This project demonstrates:
- End-to-end DevOps pipeline  
- GenAI integration in applications  
- Kubernetes deployment on AWS  
- CI/CD automation  
- Secure handling of sensitive data  