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
