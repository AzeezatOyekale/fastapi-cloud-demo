# FastAPI Cloud Demo

A simple FastAPI application containerized with Docker and deployed on AWS.

## Features
- REST API with health check
- Dockerized for easy deployment
- Cloud-ready architecture

## Endpoints
- GET `/` – Service status
- GET `/health` – Health check

## Tech Stack
- FastAPI
- Docker
- AWS EC2
- Python 3.10

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

## Live Deployment

The application is deployed on Render:

- Base URL: https://your-service-name.onrender.com
- Health Check: https://your-service-name.onrender.com/health

### AWS Deployment (Documented)
This application is AWS-ready and can be deployed on EC2 using Docker.
Steps include:
- EC2 provisioning (Ubuntu)
- Security group configuration
- Docker installation
- Container build and run

(Full AWS deployment steps available on request)


